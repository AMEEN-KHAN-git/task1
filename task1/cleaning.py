import pandas as pd
df = pd.read_csv("marketing_campaign.csv", sep="\t")
print("Top rows and columns of the dataset:\n")
print(df.head())

# Check for missing values
print("\nMissing values in each column:\n")
print(df.isnull().sum())

#dropping duplicate values
print("\nDropping duplicates\n")
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())

#standardizing column text
df['Education'] = df['Education'].str.strip().str.lower()
df['Marital_Status'] = df['Marital_Status'].str.strip().str.lower()
print("\nStandardized columns with text:\n")
print(df[['Education', 'Marital_Status']].head())

#converting date format
df['dt_customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')
print("\nConverted date format:\n")
print(df['dt_customer'].head())

#renaming column headers
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
print("\nRenamed column headers:\n")
print(df.columns.tolist())

#checking and fixing data types
print("\nData types of each column:\n")
print(df.dtypes)
df['income'] = pd.to_numeric(df['income'])
print("\nUpdated data type of needed column(s):\n")
print(df.dtypes)

# Exporting cleaned dataset to CSV
df.to_csv('cleaned_marketing_campaign.csv', index=False)
