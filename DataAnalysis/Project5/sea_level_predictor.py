import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter('Year', 'CSIRO Adjusted Sea Level', data = df)

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Define the range of years up to 2050 and the corresponding predicted sea levels
    years = pd.Series(range(df['Year'].min(), 2051))
    sea_levels = res.slope * years + res.intercept

    plt.plot(years, sea_levels, 'r-')

    # Create second line of best fit
    # Create a modified dataframe containing only the data from the year 2000 through the most recent year
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    # Define the range of years up to 2050 and the corresponding predicted sea levels
    years_recent = pd.Series(range(df_recent['Year'].min(), 2051))
    sea_levels_recent = res_recent.slope * years_recent + res_recent.intercept
    
    plt.plot(years_recent, sea_levels_recent, 'b-')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()