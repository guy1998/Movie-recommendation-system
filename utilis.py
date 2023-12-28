import pandas as pd
from data_mining_model import find_list_of_similar_movies

user_id = 0
liked_movies = []


def authenticate(username, password, action, counter_action):
    with open('Database/users.txt', 'r') as file:
        for line in file:
            user = line.split()
            if username == user[1] and password == user[2]:
                global user_id
                user_id = user[0]
                read_liked_movies()
                action()
                return

    counter_action()


def logout(action):
    global user_id
    global liked_movies
    user_id = 0
    liked_movies = []
    action()


def search_movie(title):
    df = pd.read_csv("Database/movie_dataset.csv")
    movie = df[df["title"] == title]
    return movie


def add_liked_movie(title):
    with open('Database/liked_' + str(user_id) + '.txt', 'a') as file:
        if title not in liked_movies:
            file.write(title + "\n")
            liked_movies.append(title)


def read_liked_movies():
    global liked_movies
    with open('Database/liked_' + str(user_id) + '.txt', 'r') as file:
        for line in file:
            liked_movies.append(line[:-1])


def store_recommendation(recommended_movies):
    length = len(liked_movies)
    with open('Database/recommended_' + str(user_id) + '.txt', 'w') as file:
        file.write(str(length) + "\n")
        file.writelines(line + "\n" for line in recommended_movies)


def read_prev_recommendation():
    path = 'Database/recommended_' + str(user_id) + '.txt'
    with open(path, 'r') as file:
        info = []
        for line in file:
            if len(line) > 1:
                info.append(line[:-1])
            else:
                info.append(line)
        return info


def give_recommendation():
    if len(liked_movies) == 0:
        return set()

    prev_info = read_prev_recommendation()
    starting_point = int(prev_info[0])
    previous_recommendation = set(prev_info[1:])
    new_recommendation = previous_recommendation
    print(liked_movies)
    for i in range(starting_point, len(liked_movies)):
        list_of_movies = find_list_of_similar_movies(liked_movies[i])
        new_set = set(list_of_movies)
        new_recommendation = new_recommendation.union(new_set)

    store_recommendation(new_recommendation)
    return new_recommendation


def get_trending():
    result = set()
    for i in range(1, 5):
        if i != user_id:
            with open('Database/liked_' + str(i) + '.txt', 'r') as file:
                for line in file:
                    similar_movies = find_list_of_similar_movies(line[:-1])
                    if len(result) == 0:
                        result = set(similar_movies)
                    else:
                        result.intersection_update(set(similar_movies))
    return result