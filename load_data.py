import pandas as pd

df_bank = pd.read_csv('./data/bank.csv')

# drop 'duration' column
df_bank = df_bank.drop('duration', axis=1)

#print bank info
print('Shape of the dataset:', df_bank.shape)
print('\nInfo of the dataset:')
print(df_bank.head())

print(f"Class Distribution:\n{df_bank['deposit'].value_counts()}")

print(f"Missing values in each column:\n{df_bank.isnull().sum()}")