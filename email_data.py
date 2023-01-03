import os
import re

from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col


def data_read(spark):
    data_frame = spark.read. \
        format("jdbc"). \
        option("url", "jdbc:mysql://localhost:3306/upskill_sales"). \
        option("driver", "com.mysql.cj.jdbc.Driver"). \
        option("dbtable", "email_data"). \
        option("user", "root"). \
        option("password", "sangola@123"). \
        load()

    vowels = ['a','e','i','o','u']

    # data = data_frame.withColumn(split(col("email_id"),""))
    # data.show()
    rd = data_frame.rdd
    #rd.map(lambda l: (l, len(re.findall('[aeiou]', l)))).collect()

    final=[x for x in rd.collect() if x in vowels]
    print(final)
    # df = data_frame['email_id']
    # df.show()











if __name__ == '__main__':
    parent_path = os.path.abspath('..')
    spark = SparkSession \
        .builder.config("spark.jars",
                        r"C:\Users\Abhijeet Kadam\projects\practice_problems\mysql-connector-java-8.0.22.jar")\
        .master("local") \
        .getOrCreate()
    data_read(spark)
