import pandas as pd

reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

country = reviews.groupby(['country']).points.agg([len, "mean"]).round(decimal=1)
country = country.rename(columns={"country": 'country','len':"count", 'mean': "points"})
                      
country.to_csv("date/reviews-per-country.csv")