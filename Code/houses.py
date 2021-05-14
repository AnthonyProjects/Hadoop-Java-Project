# initialize Spark Session
import os
import sys
from pyspark.sql.functions import col
top_dir = os.path.abspath(os.path.join(os.getcwd(), "../"))
if top_dir not in sys.path:
    sys.path.append(top_dir)

from init_spark import init_spark
spark = init_spark()
spark

house_csv= spark.read.csv("/data/house-prices/house-sales-full.csv", header=True, inferSchema=True)
house_sales_simplified = spark.read.csv("/data/house-prices/house-sales-simplified.csv", header=True, inferSchema=True)
house_sales_sample = spark.read.csv("/data/house-prices/house-sales-sample.csv", header=True, inferSchema=True)


house_parquet= spark.read.parquet("./house-parquet")
house_parquet.show()

house_parquet.groupBy("SalePrice").count().orderBy("count", ascending=False).show()
house_parquet.groupBy("PropertyType", "SalePrice").count().orderBy("count", ascending=False).show()
house_parquet.join(house_sales_simplified).join(house_sales_sample)
house_parquet.groupBy('SalePrice', 'Date').count().orderBy("count", ascending=False).limit(50).toPandas().plot.bar(figsize=(20,10))
house_parquet.groupBy("LandVal","SqFtLot", "YrBuilt").sum("SalePrice").show()

# filter based on zip code, SqFtFinBasement, and YrRenovated 
house_parquet.filter(("ZipCode != -1 and SqFtFinBasement !=0 and YrRenovated != 0")).groupBy("PropertyID","DocumentID", "SqFtFinBasement", "YrRenovated", "ZipCode" ).sum("SalePrice").show()


total_square_feet = house_parquet.select(((col("SqFtLot") + col("SqFtTotLiving") + col("SqFtFinBasement"))).alias("Total Square Feet"))
total_square_feet.show()

# calculate total square feet of houses and then average
total_sq_ft = house_parquet.withColumn("Total Square Feet", col("SqFtTotLiving") + col("SqFtFinBasement")).select(['Date', 'PropertyType', 'Bathrooms', 'SqFtTotLiving', 'SqFtFinBasement', "Total Square Feet"])
total_sq_ft.groupBy("Total Square Feet").avg().limit(20).toPandas().plot.bar(figsize=(20,10))

# group by the following
house_parquet.groupBy("Date", "PropertyType", "Bathrooms").sum("SalePrice").show()

# group by min and max
house_parquet.groupBy('SalePrice', 'AdjSalePrice').max().show()
house_parquet.groupBy('SalePrice', 'AdjSalePrice').min().show()
