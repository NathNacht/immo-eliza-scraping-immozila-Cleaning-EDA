import pandas as pd

csv_file = "./data/raw/raw_huis_te_koop.csv"
house = pd.read_csv(csv_file, sep=",")

house.info()
house["price"]


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


house.info()