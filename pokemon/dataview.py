# -*- coding: utf-8 -*-
"""
Created on 2017/11/21 - the current system date.

__auther__ = 'xiaoliang'
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


print(os.listdir("C:\Rock\RockXu_060921\python\machinelearning\datasets\pokemon"))
data = pd.read_csv("../datasets/pokemon/pokemon.csv")


def data_check():
    print(data.columns)
    print(data.Speed)
    print(data.info())
# data_check()


# correlation map
def corr_map():
    f,ax = plt.subplots(figsize=(18,18))
    sns.heatmap(data.corr(),annot=True, linewidths=.5, fmt=',.1f', ax=ax)
    plt.show()

# corr_map()

# line Plot
# # color = color, label = label, linewidth = width of line, alpha = opacity, grid = grid, linestyle = sytle of line
def line_plot():
    print(type(data.Speed))
    data.Speed.plot(kind='line', color='g',label='Attack',linewidth=1, alpha=.5,grid=True,linestyle=':')
    data.Defense.plot(color='r', label='Defense', linewidth=1, alpha=0.5, grid=True, linestyle='-.')
    plt.legend(loc='upper right')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('Line Plot')
    plt.show()

# line_plot()

# scatter plot

def scatter_plot():
    print(data.Attack)
    print(data.Defense)
    data.plot(kind='scatter', x='Attack',y='Defense',alpha='0.5', color='red')
    plt.xlabel('Attack')
    plt.ylabel('Defense')
    plt.title('Attack Defense Scatter Plot')
    plt.show()

# scatter_plot()


# histogram
def histogram_map():
    data.Speed.plot(kind='hist', bins=50, figsize=(10,10))
    plt.show()

# histogram_map()

def pandas_view():
    series = data['Defense']
    print(type(series))
    data_frame = data[['Defense']]
    print(type(data_frame))
pandas_view()