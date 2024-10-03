import duckdb

con = duckdb.connect('/Users/spicegold/Documents/vscode/data/duckdb/warehouse.db')
bronze_table_name = 'bronze.online_retail_sales'
silver_table_name = 'silver.online_retail_sales'

con.execute(f"CREATE SCHEMA IF NOT EXISTS silver")

con.execute(f"""
CREATE OR REPLACE TABLE {silver_table_name} AS
SELECT
InvoiceNo,
CustomerID,                 
LOWER(Description) as Description,
Cast(InvoiceDate as date) as InvoiceDate,
Cast(InvoiceDate as time) as InvoiceTime,
Quantity,
Country                                                              
FROM {bronze_table_name}"""
).fetchdf()
print("\nData in DuckDB:")
print(result)