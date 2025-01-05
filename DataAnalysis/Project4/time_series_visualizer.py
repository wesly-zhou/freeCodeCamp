import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data and set the date column as the index
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])
df.set_index('date', inplace=True)

# Clean data by removing page views in the bottom 2.5% or the top 2.5% of the dataset
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    """
    Draw a line plot showing the number of page views for each date in the dataset.
    """
    fig, ax = plt.subplots(figsize=(18, 6))
    ax.plot(df.index, df['value'], 'r-')

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    """
    Draw a bar plot showing the average number of page views for each month grouped by year.
    """
    # Copy and modify data for monthly bar plot
    # Group the data by year and reshape the data using unstack such that months are columns
    df_bar = df.groupby([df.index.year, df.index.month]).mean().unstack()

    fig, ax = plt.subplots(figsize=(8, 7))
    df_bar.plot(ax = ax, kind='bar')

    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    # Set the legend by explicitly defining the months as labels
    handles, labels = ax.get_legend_handles_labels()
    new_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ax.legend(handles = handles, labels = new_labels, title = 'Months', loc = 'upper left')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
