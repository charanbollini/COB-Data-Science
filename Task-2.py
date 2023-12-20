import pandas as pd
import numpy as np

url="/content/dataset - netflix1.csv"
df=pd.read_csv(url)
df.replace("#",np.nan,inplace=True)
print(df.head())
print(df.isnull().sum())
df.fillna(df.mean(),inplace=True)

from scipy.stats import zscore

z_scores=np.abs(zscore(df.select_dtypes(include=[np.number])))
df_no_outlines=df[(z_scores<3).all(axis=1)]
df_no_outlines.to_csv("cleared_dataset.csv",index=False)import pandas as pd
import numpy as np

url="/content/dataset - netflix1.csv"
df=pd.read_csv(url)
df.replace("#",np.nan,inplace=True)
print(df.head())
print(df.isnull().sum())
df.fillna(df.mean(),inplace=True)

from scipy.stats import zscore

z_scores=np.abs(zscore(df.select_dtypes(include=[np.number])))
df_no_outlines=df[(z_scores<3).all(axis=1)]
df_no_outlines.to_csv("cleared_dataset.csv",index=False)