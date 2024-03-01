import pandas as pd
import numpy as np
import seaborn as sns
import os

# Define the file paths using os.path.join to ensure compatibility
raw_huis_te_koop_path = os.path.join(".", "data", "raw", "raw_huis_te_koop.csv")
raw_apartement_te_koop_path = os.path.join(".", "data", "raw", "raw_apartement_te_koop.csv")

#open a the file from bpost and lowercase all location names
bpost_codes = pd.read_csv("data/raw/zipcodes_alpha_nl_new.csv", delimiter=";")
bpost_codes[['Plaatsnaam', 'Hoofdgemeente', 'Provincie']] = bpost_codes[['Plaatsnaam', 'Hoofdgemeente', 'Provincie']].apply(lambda x: x.astype(str).str.lower())

#open a the file from georef and lowercase all location names
georef = pd.read_csv("data/raw/georef-belgium-postal-codes.csv", delimiter=";")
georef[['Sub-municipality name (French)','Sub-municipality name (Dutch)', 'Sub-municipality name (German)']] = georef[['Sub-municipality name (French)','Sub-municipality name (Dutch)', 'Sub-municipality name (German)']].apply(lambda x: x.str.lower())
georef_with_nl = georef[~georef['Sub-municipality name (Dutch)'].isna()] #drop NaN from the Dutch values

house = pd.read_csv(raw_huis_te_koop_path, sep=",")
app = pd.read_csv(raw_apartement_te_koop_path, sep=",")


def strip_all_columns(df):
    cl = []
    for columns in df:
        cl.append(columns)
    return cl


def strip(df):
    cl = strip_all_columns(df)
    for column_name in cl:
        if df[column_name].dtype == 'object':  # Check if the column contains object (string) values
            df.loc[:, column_name] = df[column_name].str.strip()
    return df


def removedup_id(df):
    """
    Remove duplicate records based on property_id
    """
    dup = df.duplicated(subset=["property_id"]).sum()
    print("Number of duplicates BEFORE:",dup)
    df.drop_duplicates(subset=["property_id"],keep="first", inplace=True)
    dup = df.duplicated(subset=["property_id"]).sum()
    print("Number of duplicates AFTER:",dup)


def remove_none_prices(df):
    """
    Remove records with empty price field
    """
    price_empty_before = df["price"].isnull().sum()
    print("Number of records with empty price BEFORE:", price_empty_before)
    df.dropna(subset=['price'], inplace=True)
    price_empty_after = df["price"].isnull().sum()
    print("Number of records with empty price AFTER:", price_empty_after)
    return df


def remove_dup_no_id(df):
    """
    Function to remove all duplicate rows without looking at property_id
    """ 
    columns_to_compare = [col for col in df.columns if col != "property_id"]
    df.drop_duplicates(subset=columns_to_compare, keep="first", inplace=True)
    return df


def remove_street_nr(df):
    """
    Function to remove street_name and house_number columns
    """
    df.drop(["street_name", "house_number"], axis="columns", inplace= True)
    return df


def remove_empty(df):
    """
    Function to remove completely empty rows (where only property_id is filled in)
    """
    columns_to_compare = [col for col in df.columns if col != "property_id"]
    #checks completely empty rows
    df.dropna(how='all', inplace=True)
    #checks if property-id is completely empty
    df.dropna(how='all', subset=columns_to_compare, inplace=True)
    return df

def remove_house_in_app(df):
    df = df[~df["property_type"].isin(["HOUSE", "HOUSE_GROUP"])]
    return df


def remove_app_in_house(df):
    df = df[df["property_type"].isin(["HOUSE", "HOUSE_GROUP"])]
    return df

def open_and_lowercase(df):
    """
    The function lowercases all locality names to avoid ambiguity
    """
    df["locality_name"] = df["locality_name"].str.lower()
    return df

def drop_non_belgian(df):
    """
    The function checks if postal codes are in Belgium to remove non-belgian properties
    """
    df['is_belgian'] = df['postal_code'].astype(str).isin(bpost_codes['Postcode'].astype(str))

    df.loc[df['is_belgian']==False]

    df = df.drop(df[df['is_belgian'] == False].index)
    return df

def get_dutch_locality_name(current_locality_name):
    """
    The function translates the locality name into Dutch in case it exists
    """
    name_loc = georef_with_nl.loc[(georef_with_nl["Sub-municipality name (French)"] == current_locality_name) | (georef_with_nl["Sub-municipality name (German)"] == current_locality_name)]
    if not name_loc.empty:
        return(name_loc["Sub-municipality name (Dutch)"].iloc[0])
    else:
        return current_locality_name

def change_locality_name(df):
    df["locality_name"] = df["locality_name"].apply(get_dutch_locality_name)
    return df



print("-------------------------------")
print("TOTAL HOUSE RECORDS:",len(house))
print("TOTAL APP RECORDS:",len(app))
print("-------------------------------")
print("---Stripping blancs from all columns")
house = strip(house)
app = strip(app)    
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
print("---Removing Duplicates from Houses that have the same property_id")
remove_dup_no_id(house)
print("---Removing Duplicates from Appartments that have the same property_id")
remove_dup_no_id(app)
print("-------------------------------")
print("TOTAL HOUSE RECORDS:",len(house))
print("TOTAL APP RECORDS:",len(app))
print("-------------------------------")
print("---Removing Streetnames and House Numbers")
remove_street_nr(house)
remove_street_nr(app)
print("-------------------------------")
print("TOTAL HOUSE RECORDS:",len(house))
print("TOTAL APP RECORDS:",len(app))
print("-------------------------------")
print("---Removing Empty records that only have property_id")
remove_empty(house)
remove_empty(app)
print("-------------------------------")
print("TOTAL HOUSE RECORDS:",len(house))
print("TOTAL APP RECORDS:",len(app))
print("-------------------------------")
house = remove_app_in_house(house)
app = remove_house_in_app(app)
print("-------------------------------")
print("---Removing House in Appartments")
print("---Removing Appartments in Houses")
print("TOTAL HOUSE RECORDS:",len(house))
print("TOTAL APP RECORDS:",len(app))
print("-------------------------------")

house.to_csv("./data/cleaned/clean_house.csv", sep=',', index=False, encoding='utf-8') 
app.to_csv("./data/cleaned/clean_app.csv", sep=',', index=False, encoding='utf-8')   