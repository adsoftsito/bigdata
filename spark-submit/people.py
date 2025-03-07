from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("people")\
        .getOrCreate()

    print("read people.csv ... ")
    path_people="people.csv"
    df_people = spark.read.csv(path_people,header=True,inferSchema=True)
    df_people = df_people.withColumnRenamed("date of birth", "birth")
    df_people.createOrReplaceTempView("people")
    query='DESCRIBE people'
    spark.sql(query).show(20)

    query="""SELECT name, birth FROM people WHERE sex=="male" ORDER BY `birth`"""
    df_people_names = spark.sql(query)
    df_people_names.show(20)

    query='SELECT name, `birth` FROM people WHERE `birth` BETWEEN "1903-01-01" AND "1911-12-31" ORDER BY `birth`'
    df_people_1903_1906 = spark.sql(query)
    df_people_1903_1906.show(20)

    query='SELECT sex,COUNT(sex) FROM people WHERE birth BETWEEN "1903-01-01" AND "1911-12-31" GROUP BY sex'
    df_people_1903_1906_sex = spark.sql(query)
    df_people_1903_1906_sex.show()

    spark.stop()
