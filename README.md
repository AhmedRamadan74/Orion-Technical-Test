# Orion-Technical-Test

In this documentation, I will record all the steps I go through in this project, as well as my thoughts on how I solve problems.

### ETL Logic:
•	Data Exploration: After I read the data, I create a for loop to show all info of data like (info, null. Duplicates) and I find there are 90% of rows in (Name,Education and Occupation) missing values . Its supposed I will drop these columns because the missing values are ≥ 60%, However, I can't delete those columns until I first go back to the business requirements and those columns are important, so I will replace the NULL with the value Unknown.

•	Data Transformation: In this process, I begin by creating a copy of the original dataset to ensure that all transformations are performed on a separate working version, preserving the integrity of the source data. I then convert the OrderDate column to a proper Date data type to enable time-based analysis and extract a Year field, which is used to align and compare sales data with forecast data.
Next, I handle data quality issues by replacing missing values with “Unknown” and removing duplicate records to ensure consistency and reliability. I also apply whitespace trimming across all columns to standardize text values and prevent mismatches when establishing relationships between tables. Finally, I create a new Sales column using the formula Quantity × Net_Price to calculate total sales value for each record. This structured approach ensures clean, analysis-ready data suitable for downstream reporting and modeling.

•	Data Loading: Finally Once the data is cleaned and correctly linked through the appropriate columns, it is saved to support building a data model and enabling accurate reporting and visualization






### Data Model Logic:
Now that the data is prepared, it is loaded to create a data model and establish relationships between datasets. A right outer join was used to link the tables based on common columns: Country/Region, Brand, and Year.
To ensure the relationships were correctly established, a validation check was performed. This involved grouping the data in data_model for the year 2009 (matching the forecast dataset) and comparing the aggregated results. After that, the columns data_model.Forecast and forecast.Forecast were compared to verify consistency. A validation function was created to check whether Forecast and Forecast_true values match. Any mismatch was flagged as a failure, indicating an inconsistency in the model.





### key assumptions
1.	Missing values: 
I assumed missing categorical values represent unknown information and can be safely replaced with ‘Unknown’

2.	Dropping vs keeping columns :
I assumed these columns are business-important despite high missing rate.

3.	Sales calculation
I assumed sales amount is correctly calculated by multiplying quantity by net price.

4.	Date handling
I assumed OrderDate is the correct field for time-based analysis and yearly comparison.

5.	Forecast alignment
I assumed forecast and sales can be compared using Year as the common granularity.

------------------------------------------------------------------------------------------------------------

## Dashboard 

<img width="1325" height="726" alt="image" src="https://github.com/user-attachments/assets/628e21a9-59ac-4ec8-867b-4a8eae3bdab5" />

