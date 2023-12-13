# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import stats as stats
import seaborn as sns


def read_data(filename):
    """This function reads the file name and returns two dataframes
    One with countries as columns and one with years as colume"""

    df = pd.read_csv(filename, skiprows=[43, 44, 45, 46, 47, 48], na_values=[
                     ".."], index_col=['Country Name', 'Series Name'])

    #Droping NA values and unwanted column
    df_years = df.dropna(axis=1)
    df_years = df_years.drop(df_years.columns[0], axis=1)

    #Tansposing dataframe having year as column to country as column
    df_countries = pd.DataFrame.transpose(df_years)

    #changing dataframe enties from object to float
    df_years = df_years.astype('float64')
    return df_years, df_countries


#callling the function and printing required dataframes
filename = "b6224e18-a134-4383-9cd7-1a0ce8b28a0a_Data.csv"
df_years, df_countries = read_data(filename)

print('dataframes with years as columns:\n', df_years)
print('dataframes with countries as columns:\n', df_countries)

#use of describe method and two other
print(df_years.describe())
print(df_years.mean())
print(df_years.median())


def bar_plot(dataframe):
    """This function takes datafram and make the bar plot"""

    #selcting the years with 5 years gap
    df_5yearsgap = dataframe[['1992', '1997', '2002', '2007', '2014']]

    #restting the index
    df_bar = df_5yearsgap.reset_index('Series Name')

    #acccessing the required indicator and plot them
    df_bar[(df_bar['Series Name'] ==
            'CO2 emissions (metric tons per capita)')].plot.bar()
    plt.title('CO2 emissions (metric tons per capita)')
    df_bar[(df_bar['Series Name'] == 'Urban population')].plot.bar()
    plt.title('Urban population')


bar_plot(df_years)


def line_plot(dataframe):
    """This function takes datafram and make the line plot"""

    #restting the index
    df_yearrset2 = dataframe.reset_index('Series Name')

    #acccessing the required indicator and plot them
    df_yearrset2[(df_yearrset2['Series Name'] ==
                  'Electric power consumption (kWh per capita)')].iloc[:, 1:].T.plot.line()
    plt.legend(loc='upper right', fontsize=5)
    plt.title('Electric power consumption (kWh per capita)')

    df_yearrset2[(df_yearrset2['Series Name'] ==
                  'Arable land (% of land area)')].iloc[:, 1:].T.plot.line()
    plt.legend(loc='upper right', fontsize=5)
    plt.title('Arable land (% of land area)')


line_plot(df_years)


def heat_map(dataframe):
    """This function takes datafram and make the heat map"""

    #restting the index
    df_yearrset = dataframe.reset_index('Country Name')
    #acccessing the required country and correlating its indicator
    country_data = (
        df_yearrset.loc[(df_yearrset['Country Name'] == 'China')]).iloc[:, 1:].T.corr()
    sns.heatmap(heatmap_data, annot=True, cmap='viridis', fmt='g')
    plt.title('China')


heat_map(df_years)
