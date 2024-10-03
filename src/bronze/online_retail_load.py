
import pandas as pd
import duckdb
file_path = '/Users/spicegold/Documents/vscode/data/Online Retail.csv'
df = pd.read_csv(file_path)


print(df.columns)


con = duckdb.connect('/Users/spicegold/Documents/vscode/data/duckdb/warehouse.db')
table_name = 'bronze.online_retail_sales'

con.execute(f"CREATE SCHEMA bronze")
con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM df")


result = con.execute(f"SELECT * FROM {table_name}").fetchdf()
print("\nData in DuckDB:")
print(result)