from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("points")\
        .getOrCreate()

    sc = spark.sparkContext
    sc.version

    print("read 5000_points.txt ... ")
    path_5000 = "5000_points.txt"

    clusterRDD = sc.textFile(path_5000,  minPartitions = 5)
    print("Data : ")
    print(clusterRDD.take(5))

    rdd_split = clusterRDD.map(lambda x: x.split("\t"))
    print("split : ")
    print(rdd_split.take(5))

    rdd_split_int = rdd_split.map(lambda x: [int(x[0]), int(x[1])])
    print("int : ")
    print(rdd_split_int.take(5))

    print("end process ... ")

    spark.stop()
