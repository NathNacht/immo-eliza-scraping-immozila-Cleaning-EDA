# Immozil(l)a - Cleaning / EDA 
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![vsCode](https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white
)


## 📖 Description
This project is a follow up on the Immoweb webscraping project in https://github.com/NathNacht/immo-eliza-scraping-immozila.

The mission is to clean and analyse the scraped data to gain insights in a more accurately and faster way then competitors with the focus on estimation of the value of properties and pick out those properties that are most valuable.

The original data was split into two datasets. One containing data for houses and the other for apartments. The fields of the raw files are still as follows:


* property_id
* locality_name
* postal_code
* street_name
* house_number
* latitude
* longitude
* property_type (house or apartment)
* property_subtype (bungalow, chalet, mansion, ...)
* price
* type_of_sale (note: exclude life sales)
* number_of_rooms (Number of rooms)
* living_area (Living area (area in m²))
* kitchen_type
* fully_equipped_kitchen (0/1)
* furnished (0/1)
* open_fire (0/1)
* terrace
* terrace_area (area in m² or null if no terrace)
* garden
* garden_area (area in m² or null if no garden)
* surface_of_good
* number_of_facades
* swimming_pool (0/1)
* state_of_building (new, to be renovated, ...)


## 🛠 Installation

* clone the repo
```bash
git clone git@github.com:NathNacht/immo-eliza-scraping-immozila-Cleaning-EDA.git
```

* Install all the libraries in requirements.txt
```bash
pip install -r requirements.txt
```

* Run the script
```bash
$ python3 clean.py
```

* The output will be stored in ./data/cleaned/clean_app.csv and ./data/cleaned/clean_house.csv

## 👾 Cleaning steps
| variable to remove | reason                                    |
|--------------------|-------------------------------------------|
| surface_of_good    | in apartments dataset it is always empty  |
|    property_id     | as all records have a unique property_id  |
|   property_type    | Datasets contain only houses or apartments|
|      terrace       | boolean,we can deduct from terrace surface|
|      garden        | boolean,we can deduct from terrace surface|



## 🚀 Usage



## 🤖 Project File structure
```
├── analyses
│   ├── immozila_analyse.ipynb
│   └── semfunction.py
├── data
│   ├── cleaned
│   │   ├── clean_app.csv
│   │   └── clean_house.csv
│   └── raw
│       └── georef-belgium-postal-codes.csv
│       └── raw_apartement_te_koop.csv
│       └── raw_huis_te_koop.csv
│       └── zipcodes_alpha_nl_new.csv
├── reports
├── .gitignore
├── clean.py
├── README.md
└── requirements.txt
```


## 🔍 Contributors
- [Nathalie Nachtergaele](https://github.com/NathNacht)
- [Jens Dedeyne](https://github.com/DedeyJ)
- [Alfiya Khabibullina](https://github.com/justalphie)
- [Sem Deleersnijder](https://github.com/semdeleer)

## 📜 Timeline

This project was created in 5 days.
