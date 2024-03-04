import seaborn as sns
import pandas as pd

def heatmap(df):
    sns.heatmap(df.corr(), annot=True)

def regplot(df, xs, ys):
    sns.regplot(data = df, x=xs, y=ys)

def filter_cities(df, *cities):
    result = df[df["locality_name"].isin(cities)]
    return result

def state_of_building(df, *state):
    result = df[df["locality_name"].isin(state)]
    return result

def drop_object_columns(df):
    fdf = df[["price", "number_of_rooms", "living_area", "terrace_area", "garden_area", "surface_of_good", "number_of_facades"]]
    return fdf