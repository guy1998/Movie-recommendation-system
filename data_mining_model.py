import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_title_from_index(df, index):
    return df[df.index == index]["title"].values[0]


def get_index_from_title(df, title):
    return df[df.title == title]["index"].values[0]


def generate_movie_list(df, indices):
    movie_list = []
    for index in indices:
        movie_list.append(get_title_from_index(df, index[0]))
    return movie_list


def fill_nan_values(movies_data, selected_features):
    for feature in selected_features:
        movies_data[feature] = movies_data[feature].fillna('')
    return movies_data


def construct_similarity_matrix(movies_data):
    selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
    movies_data = fill_nan_values(movies_data, selected_features)
    combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combined_features)
    similarity = cosine_similarity(feature_vectors)
    return similarity


def find_list_of_similar_movies(title):
    df = pd.read_csv('movie_dataset.csv')
    similarity_matrix = construct_similarity_matrix(df)
    index = get_index_from_title(df, title)
    similarity_score = list(enumerate(similarity_matrix[index]))
    sorted_similar_movies_indices = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    return generate_movie_list(df, sorted_similar_movies_indices)[:10]

