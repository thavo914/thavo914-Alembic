import pandas as pd

# Read JSON from URL
json_url = "https://jsonplaceholder.typicode.com/users"
users_df = pd.read_json(json_url)

# Show the DataFrame
print("Users data from API:")
print(users_df)

# Show schema
print("\nDataFrame Info:")
print(users_df.info())

# Select specific columns
print("\nSelected columns:")
print(users_df[["name", "email", "phone"]])