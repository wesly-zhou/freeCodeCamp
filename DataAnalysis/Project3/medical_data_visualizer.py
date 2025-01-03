import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data from medical_examination.csv
df = pd.read_csv('medical_examination.csv')

# Add an overweight column to the dataframe, calculating the patient's BMI by dividing their weight in kilograms by the square of their height in meters,
# and assigning them to be overweight if the value is greater than 25. 0 for not overweight and 1 for overweight.
df['overweight'] = ((df['weight'] / (df['height'] / 100) ** 2) > 25).astype(int)

# Normalize the data values for cholestorl and glucose, where 0 is always good and 1 is always bad. If the value of gluclose or cholesterol is 1, assign
# the value to be 0, otherwise 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
    """
    Function to draw a categorical plot. Shows the counts of good and bad outcomes for the cholesterol, gluc, alco, active, and smoke variables for patients 
    with cardio and no cardio in different panels.
    """
    # Create a dataframe for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature with the column name as total.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # Draws the catplot using sns.catplot
    graph = sns.catplot(df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar')
    fig = graph.fig
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
