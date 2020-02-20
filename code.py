#Loading dependencies
import pandas as pd
import numpy as np

#Loading the json file and reading into pandas
business_json_path = 'business.json'
df_b = pd.read_json(business_json_path, lines=True)

#Subsetting the YELP dataset to restaurant-only dataset
business_restaur = df_b[df_b['categories'].str.contains('Restaurants', case=False, na=False)]

#Filtering for best performing restaurants i.e restaurants with a 4.5 rating or more - TopTierRestaurant Dataset
top_res = business_restaur [business_restaur['stars']>= 4.5]

#Counting the number of restaurants in each city
top_res_cities = top_res['city'].value_counts()

#res_cat dataset contains restaurants with 4.5 or more ratings in cities that are similar to cambridge, MA
#'Phoenix','Pittsburgh', 'Charlotte', 'Cleveland', 'Mesa', 'Tempe', 'Madison', 'Missisauga', 'Glendale'
res_cat = top_res[(top_res['city'].isin(['Phoenix','Pittsburgh', 'Charlotte', 'Cleveland', 'Mesa', 'Tempe', 'Madison', 'Missisauga', 'Glendale']))]

#Counting the frequency of each type of restaurant in the TopTier restaurant
topres = pd.Series(','.join(res_cat.categories).split()).value_counts()

#Removing the redundant descriptions in the 'categories'
topres = topres.drop(['Restaurants,','&','Food,','Restaurants,Restaurants,','(New),','(Traditional),'])







