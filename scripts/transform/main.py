
from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, lower
from misc import schema as poke_schema
from delta import *


def transform_data(df: DataFrame):
    df = df.drop_duplicates()
    df = df.toDF(*[c.lower() for c in df.columns])
    return df


def main():

    spark = SparkSession.builder \
        .appName("DeltaLakeExample") \
        .getOrCreate()

    bronze_df = spark.read.parquet("data/bronze/pokemons/")
    silver_df = transform_data(bronze_df)
    silver_df.write.partitionBy('capture_date').parquet("data/silver/pokemons/")


if __name__ == "__main__":
    main()
    