import pandas as pd
import os

raw_huis_te_koop_path = os.path.join(".", "data", "raw", "raw_huis_te_koop.csv")
raw_apartement_te_koop_path = os.path.join(".", "data", "raw", "raw_apartement_te_koop.csv")

house = pd.read_csv(raw_huis_te_koop_path, sep=",")
app = pd.read_csv(raw_apartement_te_koop_path, sep=",")

# Drops rows where no prices are found
def remove_none_prices(house):
    house.dropna(subset=['price'], inplace=True)    
    return house

# run the program and return back in dataframe
house = remove_none_prices(house)


# function to remove all duplicate rows without looking at property_id
def remove_duplicates(house):
    columns_to_compare = [col for col in house.columns if col != "property_id"]
    house.drop_duplicates(subset=columns_to_compare, keep="first", inplace=True)
    return house

# run function and reassign to same dataframe
house = remove_duplicates(house)


# Removes all rows which are completely empty
def remove_empty(house):
    columns_to_compare = [col for col in house.columns if col != "property_id"]
    #checks completely empty rows
    house.dropna(how='all', inplace=True)
    #checks if property-id is completely empty
    house.dropna(how='all', subset=columns_to_compare, inplace=True)

    return house


# def remove_not_belgium(house):
#     house["postal_code"] = house["postal_code"].str.strip(" ")
#     house = house[house["postal_code"].str.len() <= 4]    
#     return house

house = remove_empty(house)
# house = remove_not_belgium(house)
house.info()

house_unique = house.nunique()
null_counts = house.isnull().sum()
print(house_unique)
print(null_counts)
