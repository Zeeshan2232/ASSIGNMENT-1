

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
import warnings
df = pd.read_csv("data.csv", sep=",")

df.head()

def create_simple_line_plot_mean_price_over_time(df):
    """
    Create a simple line plot of mean price vs. year built.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.

    Returns:
    None
    """
    # Exclude rows with 0 values in 'yr_built'
    df = df[(df['yr_built'] != 0)]

    # Group the data by 'yr_built' and calculate the mean 'price' for each year
    mean_price_by_year_built = df.groupby('yr_built')['price'].mean()

    # Create a line plot of mean 'price' vs. 'yr_built'
    plt.figure(figsize=(10, 6))
    plt.plot(mean_price_by_year_built.index, mean_price_by_year_built.values, linestyle='-', color='b', label='Mean Price')
    plt.xlabel('Year Built')
    plt.ylabel('Mean Price (in USD)')
    plt.title('Mean Price vs. Year Built')
    plt.legend()
    plt.grid(True)

    # Show the line plot
    plt.show()
    
 #function call   
create_simple_line_plot_mean_price_over_time(df)



def create_stacked_bar_plot_bedrooms_on_floor(df):
    """
    Create a stacked bar plot of the distribution of the number of bedrooms on each floor.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.

    Returns:
    None
    """
    plt.figure(figsize=(12, 8))
    bedrooms_on_floor = df.groupby(['floors', 'bedrooms']).size().unstack().fillna(0)
    bedrooms_on_floor.plot(kind='bar', stacked=True, cmap='viridis')
    
    plt.title('Distribution of Bedrooms on Each Floor')
    plt.xlabel('Number of Floors')
    plt.ylabel('Count')
    plt.legend(title='Bedrooms', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()
    
 #function call   
create_stacked_bar_plot_bedrooms_on_floor(df)




def plot_pie_charts(df):
    """
    Create two pie charts showing the distribution of houses based on view (0,1,2,3,4)
    and the distribution of house sales by month.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.

    Returns:
    None
    """
    df["date"] = pd.to_datetime(df["date"])

    # Group by 'waterfront' for the first pie chart
    grouped_waterfront = df.groupby(df["view"])
    waterfront_per_group = grouped_waterfront.size()

    # Group by month for the second pie chart
    grouped_dates = df.groupby(df["date"].dt.month)
    dates_per_group = grouped_dates.size()

    fig, axes = plt.subplots(1, 2, figsize=(12, 4), gridspec_kw={'width_ratios': [1, 1]})

    axes[0].pie(waterfront_per_group, labels=waterfront_per_group.index, autopct="%1.1f%%", colors=None)
    axes[0].legend(loc="upper left")
    axes[0].set_title("Distribution of Houses based on view")

    axes[1].pie(dates_per_group, labels=dates_per_group.index, autopct="%1.1f%%")
    axes[1].legend(loc="upper left")
    axes[1].set_title("Distribution of House Sales by Month")

    plt.tight_layout()
    plt.show()

# Example usage:
plot_pie_charts(df)





