import duckdb

con = duckdb.connect('/Users/spicegold/Documents/vscode/data/duckdb/warehouse.db')
silver_table_name = 'silver.online_retail_sales'

con.execute(f"CREATE SCHEMA gold")



result = con.execute(f"""
SELECT * FROM {silver_table_name}"""
).fetchdf()
print("\nData in DuckDB:")
print(result)


#Use case quetions x 3 
#Answers become fact table fields
#Descriptive facors become dims