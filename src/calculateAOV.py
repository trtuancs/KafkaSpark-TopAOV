import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def calculate_aov():
    spark = SparkSession.builder \
        .master('spark://10.5.0.6:7077') \
        .appName('Show-Top-100-AOV') \
        .config("spark.jars", "../postgresql-42.2.18.jar") \
        .getOrCreate()

    invoice_no = spark.read.format("jdbc"). \
        options(
        url='jdbc:postgresql://10.5.0.5:5432/postgres',
        dbtable='public.invoice_no',
        user='admin',
        password='adminpass',
        driver="org.postgresql.Driver"). \
        load()
    customer = spark.read.format("jdbc"). \
        options(
        url='jdbc:postgresql://10.5.0.5:5432/postgres',
        dbtable='public.customer',
        user='admin',
        password='adminpass',
        driver="org.postgresql.Driver"). \
        load()
    groupby_invoice = invoice_no.groupBy('customer_id').agg(mean('grand_total').alias('aov'))
    customer_aov = groupby_invoice.join(customer, groupby_invoice.customer_id == customer.id, how='inner')
    result = customer_aov.filter(customer_aov.aov > 5000)
    result = result.sort(result.aov.desc()).select('name')
    result.show(10)
    spark.stop()
