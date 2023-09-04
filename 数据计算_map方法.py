from pyspark import SparkConf,SparkContext
import os

os.environ['PYSPARK_PYTHON'] = "C:\\Users\\28953\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_pys_map")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1,2,3,4,5])

rdd1 = rdd.map(lambda  x : x * 10)
print(rdd1.collect())

sc.stop()