import requests
import random
import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from misc import schema as poke_schema
from datetime import *


def capture_10_pokemons():
    to_catch = random.sample(range(1, 150, 1), 10)

    lista = []

    for i in to_catch:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")
        data = response.json()
        lista.append(data)

    return lista

# Função para processar os dados no Spark
def spark_data_processing(lista, date):

    spark = SparkSession.builder \
        .appName("JSON to DataFrame") \
        .getOrCreate()
    
    bronze_layer_path = "data/bronze/pokemons/"

    df = spark.createDataFrame(lista, poke_schema)

    df = df.withColumn('CAPTURE_date', lit(date))
    
    df.write.mode("append").partitionBy('CAPTURE_date').parquet(bronze_layer_path)


def acquire_data(_date: date = date.today()):
    lista = capture_10_pokemons()
    spark_data_processing(lista, _date)


def go_ash():
    month = random.randint(1, 12)

    year = 2024 if month == 1 else 2023

    for _ in range(12):
        day = random.randint(1, 25)

        if month == 12:
            year += 1
        month = month + 1 if month < 12 else 1

        print(date(year, month, day))
        acquire_data(date(year, month, day))


if __name__ == "__main__":
    go_ash()
    