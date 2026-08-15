import streamlit as st
import pickle
import joblib

st.title("Movie Recommendation System")

with  open("movies.pickle","rb") as m:
    movies=pickle.load(m)

similarity = joblib.load("similarity.joblib")    

movie_names=movies['title'].values

def  recommend(name_movie):
    movie_index=movies[movies['title'].str.lower() == name_movie.lower()].index[0]
    recommendations = similarity[movie_index]
    movie_list = sorted(enumerate(recommendations),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movies=[]

    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]]['title'])

    return recommend_movies



name_movie=st.selectbox("Enter the Movie Name",movie_names)

if st.button("Recommend"):
    r = recommend(name_movie)

    st.write("The Recommened Movies for you:")

    for i in r:
        st.write(i)
