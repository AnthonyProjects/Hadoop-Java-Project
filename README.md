# Hadoop-Java-Project
* Anthony Borza
* Class Dates: 5/11/2021 - 5/14/2021
* Final Project

Description: 

* The Purpose of this assignment is to apply the Hadoop knowledge that we learned to a data set of our chosing. We will then peform various calculations
  on one of the frameworks learned in class: Hive, Pig, and Spark. The data set that i have chosen for this project is, house prices, and the framework i have chosen
  is spark. A series of graphs and metrics will be displayed to show the aggregate data. 

Framework:

* I will be using the Spark framework to aggregate my dataset. Spark runs on Hadoop and is an analyic data processing tool for large-scale data processing. 

Development Enviroment:

* Windows 10 - 64 bit operating system
* Jupytier Notebook
* Python 3
* Spark 

Results:

* Showed that the following can be accomplished to a dataset in spark:
* Examined Data:
	* Looked over the house-prices csv file and other data in folder
	* Three data set files: house-sales-full.csv, house-sales-simplified.csv, and house-sales-sample.csv can be imported into Juypter Notebook
* Clean and Deal with any missing /invalid data:
	* Ability to filter out -1 from zipcodes, and 0 from basement square footage, and 0 from year renovated
* Do some analytical queries to show some interesting aggregations on your data
	* Ability to groupBy SalePrice and count the number of houses with that sale price
	* Ability to groupBy PropertyType and SalePrice, and Counted the number of houses with those types
	* Joined the three .csv files together using the .join() command
	* Calculated the total Square Feet of all the houses to include: "SqFtLot", "SqFtTotLiving", and "SqFtFinBasement"
	* Calculate total square feet of houses and then average of houses based on bathrooms, total living
	* find the max sales price and adj sale price
	* find the min sales price and adj sale price
* Generate a few "insights" on your data, supported if possible by tables or visualization:
	* Displayed a bar graph of houses grouped by SalePrice and Date
	* Displayed a bar graph to show: Total Square feet, average # of bathrooms, sqft in living, and basement of house
	* Displayed several tables to show results of aggreagated data






