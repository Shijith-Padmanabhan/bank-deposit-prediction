from sklearn.preprocessing import StandardScaler
from load_data import df_bank

# copying original dataframe
df_bank_ready = df_bank.copy()

scaler = StandardScaler()

num_cols = ['age', 'balance', 'day', 'campaign', 'pdays', 'previous']
df_bank_ready[num_cols] = scaler.fit_transform(df_bank_ready[num_cols])
print("Numerical columns have been scaled using StandardScaler.")

print(df_bank_ready.head())