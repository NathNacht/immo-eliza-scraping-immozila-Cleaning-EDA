import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.io as pio
import seaborn as sns

house_csv = r".\data\cleaned\clean_house.csv"
app_csv = r".\data\cleaned\clean_app.csv"

house = pd.read_csv(house_csv)
app = pd.read_csv(app_csv)
print(house.head(3))
print(app.head(3))
print(house.columns)

df = house

fig = px.bar(df.nunique(), x=df.columns, y=df.nunique(), title='Unique Value Counts by Column',
             labels={'y': 'Unique Values Count'})

# Define callback function for drill-down
def drill_down_callback(trace, points, selector):
    selected_column = trace['x'][0]

    # Create a new DataFrame for the drill-down
    unique_values_df = pd.DataFrame({'Unique Values': df[selected_column].unique()})

    # Create a bar chart for unique values in the selected column
    fig = px.bar(unique_values_df[selected_column].value_counts(), x=unique_values_df[selected_column].value_counts().index,
                 y=unique_values_df[selected_column].value_counts().values,
                 title=f'Unique Values Count - {selected_column}', labels={'y': 'Count'})
    fig.show()

# Attach the drill-down callback to each bar in the initial chart
fig.for_each_trace(lambda t: t.on_click(drill_down_callback))

# Show the initial bar chart
fig.show()