import pandas as pd
import pickle
import os

BOOKS_CSV = "./data/Books.csv"
RATINGS_CSV = "./data/Ratings.csv"
USERS_CSV = "./data/Users.csv"


def save_samples(users, ratings, books):
    pickle_dir = 'data_samples'
    if not os.path.exists(pickle_dir):
        os.makedirs(pickle_dir)

    users.to_pickle(os.path.join(pickle_dir, 'users_sample.pkl'))
    ratings.to_pickle(os.path.join(pickle_dir, 'ratings_filtered.pkl'))
    books.to_pickle(os.path.join(pickle_dir, 'books_filtered.pkl'))


def get_saved_samples():
    # Paths to the pickle files
    users_pickle_path = 'data_samples/users_sample.pkl'
    ratings_pickle_path = 'data_samples/ratings_filtered.pkl'
    books_pickle_path = 'data_samples/books_filtered.pkl'
    
    # Load the data from the pickle files
    users_sample = pd.read_pickle(users_pickle_path)
    ratings_filtered = pd.read_pickle(ratings_pickle_path)
    books_filtered = pd.read_pickle(books_pickle_path)
    
    return users_sample, ratings_filtered, books_filtered


def get_data_samples(fraction = 0.1, save = True):
    if fraction>1 or fraction<0:
        fraction = 0.1

    users = pd.read_csv('./data/Users.csv')
    ratings = pd.read_csv('./data/Ratings.csv')
    books = pd.read_csv('./data/Books.csv')

    users_sample = users.sample(frac=fraction)  

    ratings_filtered = ratings[ratings['User-ID'].isin(users_sample['User-ID'])]

    books_filtered = books[books['ISBN'].isin(ratings_filtered['ISBN'])]

    # Verificación de tamaños después del filtrado
    print(f"Users: {users_sample.shape[0]} entries after sampling")
    print(f"Ratings: {ratings_filtered.shape[0]} entries after filtering")
    print(f"Books: {books_filtered.shape[0]} entries after filtering")

    if save:
        save_samples(users_sample, ratings_filtered, books_filtered)
    
    return users_sample, ratings_filtered, books_filtered


if __name__ == "__main__":
    get_data_samples()