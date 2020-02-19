#Importing Dependencies
import pandas as pd
import numpy as np

#Loading the dataset
business_json_path = 'business.json'
df_b = pd.read_json(business_json_path, lines=True)

#The OG YELP dataset contains data on other types of businesses including shopping, salons, dental clinics, etc
#Line 11 is to filter dataset for only data from restaurants
business_restaur = df_b[df_b['categories'].str.contains('Restaurants', case=False, na=False)]

#Line 14:  Subsetting estaurants with rating of more than 4.5 stars
top_res = business_restaur [business_restaur['stars']>= 4.5]

#Line 17: To obtain frequencies of restaurants in different cities
top_res_cities = top_res['city'].value_counts()

#Top 11 cities in terms of high number of restaurants are:
#Las Vegas, Toronto, Montreal, Phoenix, Calgary, Pittsburgh, Charlotte, Scottsdale, Cleveland, Mesa, Tempe
#The cities that closely resemble Cambridge are all but Las Vegas and Mesa - considering mainly universities and student crowd

#Line 24: Subsetting dataframe to contain only the above mentioned cities
res_cat = top_res[(top_res['city'].isin(['Toronto', 'MontrÃ©al', 'Scottsdale', 'Charlotte','Phoenix', 'Pittsburgh', 'Cleveland', 'Tempe']))]
#res_cat dataset contains restaurants with more than 4.5 stars in towns that are similar to Cambridge:
#Toronto, Montreal, Phoenix, Pittsburgh, Cleveland, Tempe, Scottsdale, Charlotte

#This gives you a list of the most frequent types of restaurants in the above mentioned cities
topres = pd.Series(','.join(res_cat.categories).split()).value_counts()

#Dropping redundant descriptions in categories
topres = topres.drop(['Restaurants,','&','Food,','Restaurants,Restaurants,','(New),','(Traditional),'])
