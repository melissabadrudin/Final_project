

### DATA CLEANING TIME

import pandas as pd
import seaborn as sns
df= pd.read_csv('df_from_sql.csv')

#checking for duplicates in the Car_ID column
df.duplicated(subset=['Car_ID']).sum()

#drop the column extra que apareceu como novo Index

df.drop(columns=['Unnamed: 0'],inplace=True )

print(df.dtypes)
print(df.describe)

#check for nulls:
df.isnull().sum()

#check coreelation
correlation = df.corr()
sns.heatmap(correlation)

#remove the cv from the power column
df['Power'] = df['Power'].str.replace('cv', '')
print(df.Power.unique()) #its all numbers so we are good, it worked!
df['Power']=pd.to_numeric(df['Power'])
print(df.dtypes)

## Transform categorical variables with get dummies

#Drop Model pq senao fico com mil colunas literalmetne
df_modeless=df.drop(columns='Model')
df_dummie=pd.get_dummies(df_modeless)
df_dummie.drop(columns=['Car_ID'],inplace=True)

#cleaning done!!!!

df_dummie.to_csv('df_dummie.csv')


