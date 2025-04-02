import pandas as pd
movies_data={"Movie Name":["Inception","3 Idiots","Parasite","The Dark Knight","Dangal","Spirited away","La La Land","Bahubali","Amelia","RaOne"],"Language":["English","Hindi","French","Hindi","Japanese","English","French","Hindi","Hindi","Hindi"],"Genre":["SciFi","Comedy","Thriller","Action","Biography","Animation","Musical","Action","Romance","SciFi"],"Rating":[8.8,8.4,8.6,9.0,8.4,8.6,8.0,8.1,8.3,4.9],"Review":["Excellent","Inspiring","Thriller","Outstanding","Empowering","Magical","Enchanting","Epic","Charming","Good"]}
df=pd.DataFrame(movies_data)
df.to_csv('Movies.csv',index=False)
print("\n\nMovies.csv created")
df=pd.read_csv("Movies.csv")
highest_rated_movie=df.loc[df['Rating'].idxmax()]
print("The movie with the highest rating is :",highest_rated_movie)
hindi_movies=df[df["Language"]=='Hindi']
hindi_movies.to_csv('Hindi_movies.csv',index=False)
print("\n\nDetails of hindi movies have been written to Hindi_movies.csv")