from data.load import load_data
from processing.clean import clean_data

df = load_data()
df = clean_data(df)

print(df.dtypes)