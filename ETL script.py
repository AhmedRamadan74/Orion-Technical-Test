#Improt libraries
import numpy as np 
import pandas as pd 
import json

#Read Json File 
sales= pd.read_json(r'D:/Data Science and Data Analysis/Jobs/Orion/data/Sales.json')
forecast= pd.read_json(r'D:/Data Science and Data Analysis/Jobs/Orion/data/forecast.json')

# =============================================================================================================================
#1)Data Exploration

#   >>>Create for loop to show all info of data one time like(Sum and Percentage of Nulls and Sum and Percentage of duplicates)
all_data={
          'sales': sales ,
           'forecast' : forecast
            }

for name,data in all_data.items():
    print(f'Data is {name}')
    #Show info
    data.info()
    print('*'*50)

    #show all Null as sum
    print(f"Sum of Nulls in {name}")
    print(data.isnull().sum()) 
    print('*'*50)

    #show all Null as Percentage
    print(f"Percentage of Nulls in {name}")
    print(round(data.isnull().mean()*100)) 
    print('*'*50)

    #Show sum of duplicates
    duplicated = data.duplicated().sum() 
    print(f'Sum of duplicates in {name} = {duplicated} ')
    #show percentage of duplicates
    print(f'Percentage of duplicates in {name} = {  
                                        round((duplicated / len(data))*100,1)
                                        }' , "%"
         ) 
    print('')     
    print('='*100)

# =============================================================================================================================
#2)Data Transformation

#   >>>First, take a copy of the original sales data to modify it.
sales_clean=sales.copy()

#   >>>Change datatype of OrderDate to date
sales_clean.OrderDate= pd.to_datetime(sales_clean.OrderDate)

#   >>>Parse years to i can compere between year of forecast 
sales_clean["Year"]=sales_clean.OrderDate.dt.year

#   >>>The percentage of nulls in the Name,Education and Occupation columns is 90%.Its supposed I will drop these columns 
#   >>>because the missing values are ≥ 60%, However, I can't delete those columns until I first go back to the business requirements
#   >>>and those columns are important, so I will replace the NULL with the value Unknown.
sales_clean.fillna("Unknown",inplace =True)

#   >>>check of nulls
print('')
print('Check of Nulls after clean')
print(sales_clean.isnull().sum())

#   >>>delete duplicates
sales_clean.drop_duplicates(inplace=True)

#   >>>check of duplicates
print('')
print('Check of Duplicates after clean')
print('='*100)
print( "Duplicates =" , sales_clean.duplicated().sum())

#   >>>check a numbers of rows 
print('')
print('Check numbers of rows after clean')
print('='*100)
print("Numbers of rows" , len(sales_clean))

#   >>>I want to show trim whitespace in all columns to i can modify them to i aviod any errors when i create relationships 
sales_clean.columns = sales_clean.columns.str.strip().str.replace(" ", "_")

#   >>Create the sales columns with this equation Quantity*Net_Price
sales_clean["sales"] = sales_clean.Quantity*sales_clean.Net_Price


# =============================================================================================================================
#3) Data Loading
sales_clean.to_csv("Clean_sales.csv",index=False)
forecast.to_csv("Clean_forecast.csv",index=False)
