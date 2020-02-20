import pandas as pd
import numpy as np

business_json_path = 'business.json'
df_b = pd.read_json(business_json_path, lines=True)

business_restaur = df_b[df_b['categories'].str.contains('Restaurants', case=False, na=False)]

top_res = business_restaur [business_restaur['stars']>= 4.5]

top_res_cities = top_res['city'].value_counts()

res_cat = top_res[(top_res['city'].isin(['Phoenix','Pittsburgh', 'Charlotte', 'Cleveland', 'Mesa', 'Tempe', 'Madison', 'Missisauga', 'Glendale']))]
#res_cat dataset contains restaurants with more than 4 stars in towns that are similar to cambridge:
#Toronto, Montreal, Phoenix, Pittsburgh, Cleveland, Tempe, Scottsdale, Charlotte

#This gives you a list of the most frequent types of restaurants in 
topres = pd.Series(','.join(res_cat.categories).split()).value_counts()

#This code already dropped the keywords so if you run it again, it wont work
topres = topres.drop(['Restaurants,','&','Food,','Restaurants,Restaurants,','(New),','(Traditional),'])

#All the restaurants in the rescat dataset are restaurants in the above mentioned cities
#with rating of more than 4.5 stars






