# execute:  bash run.sh

from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession\
        .builder\
        .appName("map_filter")\
        .getOrCreate()

    print("map, filter app ... ")
    my_list = [1,2,3,4,5,6,7,8,9]
    squared_my_list = list(map(lambda x: x*x, my_list))
    print("squared list ...")
    print(squared_my_list)

    filtered_my_list = list(filter(lambda x: (x%2 != 0), my_list))
    print("filtered list ...")
    print(filtered_my_list)
    spark.stop()
