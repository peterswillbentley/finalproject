"""
Name:       William Peters
CS230:      SN2S
Data:       Used cars for sale on Craigslist
URL:        Link to your web application online (see extra credit)
Description:
This program reads used car data from Craigslist.
It calculates displays the average price based on the type of car, paint color, year and manufactuere.
It also breaks down the cars by paint color, drivetrain, and fuel type, all based on state.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from collections import Counter

st.set_option('deprecation.showPyplotGlobalUse', False)

# reading file
cars = pd.read_csv('usedcars.csv')

# retrieving and cleaning unique lists of relevant values
states = cars["state"].unique()
states = [x for x in states if str(x) != 'nan']
states = [x.upper() for x in states]
states.sort()

manufacturers = cars["manufacturer"].unique()
manufacturers = [x for x in manufacturers if str(x) != 'nan']

paint_colors = cars["paint_color"].unique()
paint_colors = [x for x in paint_colors if str(x) != 'nan']

types = cars["type"].unique()
types = [x for x in types if str(x) != 'nan']

years = cars["year"].unique()
years = [x for x in years if str(x) != 'nan']
years.sort()
years = [int(x) for x in years]

# defines categories by which averages will be sorted
categories = (manufacturers, paint_colors, types, years)
labels = ("manufacturer","paint_color","type","year")

# function to calculate averages by category
def average_price(variable,label):
    d ={}
    for x in variable:
        m = cars[cars[label] == x]
        d[x] = m["price"].mean()
    return d

# creates output
def main():
    st.title(f"Welcome to Used Car Market Analysis")

    # Average Prices Bar Charts
    st.subheader('USA Average Prices by Category')
    for x in range(len(categories)):
        ked = average_price(categories[x], labels[x])
        keys = list(ked.keys())
        values = list(ked.values())
        plt.bar(keys, values)
        plt.title(f"Average Price by {labels[x].upper()}")
        if not labels[x] == "year":
            plt.xticks(rotation=75, fontsize = 6)
        st.pyplot()

    state = st.sidebar.selectbox('Select', states)

    # Pie Charts
    st.subheader(f"{state} Pie Charts")
    st.text("Paint Colour")
    # Paint
    paint = cars[cars["state"] == state.lower()]
    paint = paint["paint_color"]
    paint = [x for x in paint if str(x) != 'nan']
    counts = Counter(paint)
    pielabels = list(counts.keys())
    sizes = list(counts.values())

    plt.pie(sizes, labels=pielabels, autopct='%1.2f%%', pctdistance=0.8)
    st.pyplot()

    # Fuel
    st.text("Fuel Type")
    fuel = cars[cars["state"] == state.lower()]
    fuel = fuel["fuel"]
    fuel = [x for x in fuel if str(x) != 'nan']
    counts = Counter(fuel)
    pielabels = list(counts.keys())
    sizes = list(counts.values())

    plt.pie(sizes, labels=pielabels, autopct='%1.2f%%', pctdistance=0.8)
    st.pyplot()

    # Drive Train
    st.text("Drive Train")
    drive = cars[cars["state"] == state.lower()]
    drive = drive["transmission"]
    drive = [x for x in drive if str(x) != 'nan']
    counts = Counter(drive)
    pielabels = list(counts.keys())
    sizes = list(counts.values())

    plt.pie(sizes, labels=pielabels, autopct='%1.2f%%', pctdistance=0.8)
    st.pyplot()

main()

"""

References:
https://upslearn.github.io/Books/concepts.html#2-display
https://stackoverflow.com/questions/31037298/pandas-get-column-average-mean
https://stackoverflow.com/questions/32072076/find-the-unique-values-in-a-column-and-then-sort-them
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/03_subset_data.html
https://www.kite.com/python/answers/how-to-plot-a-bar-chart-using-a-dictionary-in-matplotlib-in-python
https://discuss.streamlit.io/t/libraries-that-are-currently-supported/57/2
https://www.tutorialspoint.com/matplotlib/matplotlib_pie_chart.htm
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html
https://www.w3schools.com/python/python_tuples.asp
https://www.tutorialspoint.com/plot-a-bar-using-matplotlib-using-a-dictionary
https://discuss.streamlit.io/t/can-i-use-streamlit-within-a-pycharm-development-environment/4837
https://stackoverflow.com/questions/21572870/matplotlib-percent-label-position-in-pie-chart
"""
