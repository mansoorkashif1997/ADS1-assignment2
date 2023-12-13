import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import stats as stats
import seaborn as sns

def read_data(filename):
    
    df = pd.read_csv(filename,skiprows=[43,44,45,46,47,48],na_values=[".."],index_col=['Country Name', 'Series Name'])

    df_years = df.dropna(axis=1)
    df_years = df_years.drop(df_years.columns[0] ,axis=1)
    #df_countries = pd.DataFrame.transpose(df)
    df_countries = pd.DataFrame.transpose(df_years)

    #df_countries = df_countries.dropna()
    #df_countries = df_countries.drop(df_countries.index[0])

    #df_years = pd.DataFrame.transpose(df_countries)
    df_years = df_years.astype('float64')
    return  df_years, df_countries


filename = "b6224e18-a134-4383-9cd7-1a0ce8b28a0a_Data.csv"  
df_years, df_countries = read_data(filename)


print('dataframes with years as columns:\n',df_years)
print('dataframes with countries as columns:\n',df_countries)


print(df_years.describe())


df_4yearsgap= df_years[['1992', '1996', '2000', '2004', '2008', '2014' ]]
df_4yearsgap[df_4yearsgap.index.get_level_values('Series Name') == 'Arable land (% of land area)'].plot.bar()

plt.title('Population, total of different countries with 4 years gap')



