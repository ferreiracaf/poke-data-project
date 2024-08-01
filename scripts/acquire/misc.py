from pyspark.sql.types import StructType, StructField, StringType, IntegerType, ArrayType, BooleanType, MapType

# Definindo o esquema explicitamente
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("base_experience", IntegerType(), True),
    StructField("height", IntegerType(), True),
    StructField("weight", IntegerType(), True),
    StructField("is_default", BooleanType(), True),
    StructField("order", IntegerType(), True),
    StructField("location_area_encounters", StringType(), True),
    StructField("abilities", ArrayType(
        StructType([
            StructField("is_hidden", BooleanType(), True),
            StructField("slot", IntegerType(), True),
            StructField("ability", StructType([
                StructField("name", StringType(), True),
                StructField("url", StringType(), True)
            ]), True)
        ])
    ), True),
    StructField("forms", ArrayType(
        StructType([
            StructField("name", StringType(), True),
            StructField("url", StringType(), True)
        ])
    ), True),
    StructField("game_indices", ArrayType(
        StructType([
            StructField("game_index", IntegerType(), True),
            StructField("version", StructType([
                StructField("name", StringType(), True),
                StructField("url", StringType(), True)
            ]), True)
        ])
    ), True),
    StructField("held_items", ArrayType(
        StructType([
            StructField("item", StructType([
                StructField("name", StringType(), True),
                StructField("url", StringType(), True)
            ]), True),
            StructField("version_details", ArrayType(
                StructType([
                    StructField("rarity", IntegerType(), True),
                    StructField("version", StructType([
                        StructField("name", StringType(), True),
                        StructField("url", StringType(), True)
                    ]), True)
                ])
            ), True)
        ])
    ), True),
    StructField("moves", ArrayType(
        StructType([
            StructField("move", StructType([
                StructField("name", StringType(), True),
                StructField("url", StringType(), True)
            ]), True),
            StructField("version_group_details", ArrayType(
                StructType([
                    StructField("level_learned_at", IntegerType(), True),
                    StructField("move_learn_method", StructType([
                        StructField("name", StringType(), True),
                        StructField("url", StringType(), True)
                    ]), True),
                    StructField("version_group", StructType([
                        StructField("name", StringType(), True),
                        StructField("url", StringType(), True)
                    ]), True)
                ])
            ), True)
        ])
    ), True),
    StructField("species", StructType([
        StructField("name", StringType(), True),
        StructField("url", StringType(), True)
    ]), True),
    StructField("sprites", StructType([
        StructField("front_default", StringType(), True)
    ]), True),
    StructField("stats", ArrayType(
        StructType([
            StructField("base_stat", IntegerType(), True),
            StructField("effort", IntegerType(), True),
            StructField("stat", StructType([
                StructField("name", StringType(), True),
                StructField("url", StringType(), True)
            ]), True)
        ])
    ), True),
    StructField("types", ArrayType(
        StructType([
            StructField("slot", IntegerType(), True),
            StructField("type", StructType([
                StructField("name", StringType(), True),
                StructField("url", StringType(), True)
            ]), True)
        ])
    ), True)
])