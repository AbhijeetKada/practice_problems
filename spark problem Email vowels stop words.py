import os
import re

from pyspark.sql import SparkSession
from pyspark.sql.catalog import Column
from pyspark.sql.functions import split, col, lit


def data_read(spark):
    data_frame = spark.read. \
        format("jdbc"). \
        option("url", "jdbc:mysql://localhost:3306/upskill_sales"). \
        option("driver", "com.mysql.cj.jdbc.Driver"). \
        option("dbtable", "email_data"). \
        option("user", "root"). \
        option("password", "sangola@123"). \
        load()

    vowels = ['a', 'e', 'i', 'o', 'u']
    stop_words = ['the', 'is']

    sp = data_frame.withColumn('email_id', split(data_frame['email_id'], '')). \
        withColumn("email_body", split(data_frame['email_body'], " "))
    splt = sp.select("email_id")

    spltb = sp.select("email_body")
    max_val = splt.select('email_id').collect()[0].asDict()['email_id']
    print(max_val)
    body_val = spltb.select('email_body').collect()[0].asDict()['email_body']

    # vowel = [x for x in max_val if x in vowels]
    # st_word = [x for x in body_val if x in stop_words]

    final = data_frame.withColumn("email_id", data_frame['email_id']). \
        withColumn("vowels_in_email_id", [x for x in max_val if x in vowels]). \
        withColumn("stop_words_in_body", [x for x in body_val if x in stop_words])
    final.show()







    # vow = data_frame.select(split(col("email_id"),"")).alias("email_id")
    #
    # final = [x for x in vow if x in vowels]
    # stop = data_frame.select(split(col("email_body"), " ")).alias("email_body")
    #
    # data_frame.withColumn("email_id").\
    #     withColumn("vowels_in_email_id",final).\
    #     withColumn("stop_words_in_body",stop)
    #
    # data_frame.show()

    # rd = data_frame.rdd
    # count = rd.map(lambda l: (l, len(re.findall('[aeiou]', l))))
    # count.collect()
    # rd.collect()
    # final=[x for x in rd.collect() if x in vowels]
    # print(final)
    # df = data_frame['email_id']
    # df.show()


if __name__ == '__main__':
    parent_path = os.path.abspath('..')
    spark = SparkSession \
        .builder.config("spark.jars",
                        r"C:\Users\Public\AbhijeetKadam\projects\Internal\SalesData\mysql-connector-java-8.0.22.jar") \
        .master("local") \
        .getOrCreate()
    data_read(spark)
