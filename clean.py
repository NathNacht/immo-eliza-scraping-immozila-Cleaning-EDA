import pandas as pd
import numpy as np
import seaborn as sns
import os

# Define the file paths using os.path.join to ensure compatibility
raw_huis_te_koop_path = os.path.join(".", "data", "raw", "raw_huis_te_koop.csv")
raw_apartement_te_koop_path = os.path.join(".", "data", "raw", "raw_apartement_te_koop.csv")

house = pd.read_csv(raw_huis_te_koop_path, sep=",")
app = pd.read_csv(raw_apartement_te_koop_path, sep=",")

def removedup_id(df):
    dup = df.duplicated(subset=["property_id"]).sum()
    print("Number of duplicates BEFORE:",dup)
    df.drop_duplicates(subset=["property_id"],keep="first", inplace=True)
    dup = df.duplicated(subset=["property_id"]).sum()
    print("Number of duplicates AFTER:",dup)

def remove_none_prices(df):
    price_empty_before = df["price"].isnull().sum()
    print("Number of records with empty price BEFORE:", price_empty_before)
    df.dropna(subset=['price'], inplace=True)
    price_empty_after = df["price"].isnull().sum()
    print("Number of records with empty price AFTER:", price_empty_after)
    return df




    
print("-------------------------------")
print("TOTAL HOUSE RECORDS:",len(house))
print("TOTAL APP RECORDS:",len(app))
print("-------------------------------")
print("---Removing Duplicates from Houses")
removedup_id(house)
print("---Removing Duplicates from Appartments")
removedup_id(app)
print("-------------------------------")
print("TOTAL HOUSE RECORDS:",len(house))
print("TOTAL APP RECORDS:",len(app))
print("-------------------------------")
print("---Removing records with empty price field from Houses")
remove_none_prices(house)
print("---Removing records with empty price field from Appartements")
remove_none_prices(app)
print("-------------------------------")
print("TOTAL HOUSE RECORDS:",len(house))
print("TOTAL APP RECORDS:",len(app))
print("-------------------------------")



