from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.appName("ProductCategoryTest").getOrCreate()

# Схемы
schema_products = StructType(
    [
        StructField("product_id", IntegerType(), nullable=False),
        StructField("product_name", StringType(), nullable=False),
    ]
)

schema_categories = StructType(
    [
        StructField("category_id", IntegerType(), nullable=False),
        StructField("category_name", StringType(), nullable=False),
    ]
)

schema_links = StructType(
    [
        StructField("product_id", IntegerType(), nullable=False),
        StructField("category_id", IntegerType(), nullable=False),
    ]
)


# Продукты
products_data = [
    (1, "Молоко"),
    (2, "Хлеб"),
    (3, "Смартфон"),
    (4, "Ноутбук"),
    (5, "Кофе"),
    (6, "Чай"),
    (7, "Монитор"),
]

# Категории
categories_data = [
    (1, "Молочное"),
    (2, "Хлебобулочное"),
    (3, "Электроника"),
    (4, "Напитки"),
    (5, "Гаджеты"),
]

# Связи продукт-категория
links_data = [
    (1, 1),  # Молоко -> Молочное
    (2, 2),  # Хлеб -> Хлебобулочное
    (3, 3),  # Смартфон -> Электроника
    (3, 5),  # Смартфон -> Гаджеты
    (4, 3),  # Ноутбук -> Электроника
    (4, 5),  # Ноутбук -> Гаджеты
    (5, 4),  # Кофе -> Напитки
]

# Создание датафреймов
products_df = spark.createDataFrame(products_data, schema_products)
categories_df = spark.createDataFrame(categories_data, schema_categories)
links_df = spark.createDataFrame(links_data, schema_links)


# Если необходимо вывести одну таблицу с общим результатом
def get_products_and_categories(products_df, categories_df, links_df):
    # Выделяем все продукты
    df_all_prods = products_df.join(
        links_df, products_df.product_id == links_df.product_id, how="left"
    ).select("product_name", "category_id")
    # Добавляем названия категорий, если они есть
    df_result = df_all_prods.join(
        categories_df, df_all_prods.category_id == categories_df.category_id, how="left"
    ).select("product_name", "category_name")
    return df_result


# Если необходимо вывести таблицу и отдельно названия товаров без категорий
def get_products_and_categories2(products_df, categories_df, links_df):
    # Получаем все продукты
    full_result = (
        products_df.join(
            links_df, products_df.product_id == links_df.product_id, how="left"
        )
        .join(
            categories_df, links_df.category_id == categories_df.category_id, how="left"
        )
        .select("product_name", "category_name")
    )

    # Отделяем продукты без категорий
    products_without_categories = full_result.filter("category_name IS NULL").select(
        "product_name"
    )

    # Продукты с категориями
    products_with_categories = full_result.filter("category_name IS NOT NULL")

    # Формируем список названий продуктов без категорий
    product_names_list = [
        row.product_name for row in products_without_categories.collect()
    ]

    return products_with_categories, product_names_list


result = get_products_and_categories(products_df, categories_df, links_df)
result.show()
result_df, prod_names = get_products_and_categories2(
    products_df, categories_df, links_df
)
result_df.show()
print(prod_names)
