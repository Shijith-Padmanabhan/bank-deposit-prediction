from sklearn.preprocessing import OneHotEncoder
from scale_numeric import df_bank_ready
import pandas as pd

encoder = OneHotEncoder(sparse_output=False)
cat_cols = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'poutcome']

# Encoding categorical columns
df_encoded = pd.DataFrame(encoder.fit_transform(df_bank_ready[cat_cols]))
df_encoded.columns = encoder.get_feature_names_out(cat_cols)

# Replace categorical columns with encoded columns
df_bank_ready = df_bank_ready.drop(cat_cols, axis=1)
df_bank_ready = pd.concat([df_encoded, df_bank_ready],axis = 1)

# Encode target value
df_bank_ready['deposit'] = df_bank_ready['deposit'].apply(lambda x: 1 if x == 'yes' else 0)

print('Shape of the dataset after encoding:', df_bank_ready.shape)
print(df_bank_ready.head())