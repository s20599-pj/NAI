import argparse
import json
import operator

"""
Autorzy: Kamil Romiński, Artur Jankowski
Program pozwala na podstawie przygotowanej liscie filmow i osob zaproponowac jakie filmy wybrana osoba powinna obejrzec i ktore powinna omijac

Wymagania:
 - Przygotowana lista uzytkownikow i filmow w pliku JSON
 - Python3
"""


def build_arg_parser():
    """
    Funckja która obsługuje argumenty podane podczas włączania programu
    :return: obiekt zwierający wszystkie wspierane i podane argumenty
    """
    parser = argparse.ArgumentParser(description="Provide list of movies worth watching and movies that should be avoided")
    parser.add_argument('--user', dest='user', required=True,
                        help='User which should receive recommendation based on json database')
    return parser


def movie_recomendation(dataset, user):
    """
    Funkcja służąca do sprawdzania jakie filmy użytkownik powinien obejrzeć a jakich nie na podstawie danych zawartych w pliku JSON
    :param dataset: parametr danych z pliku JSON
    :param user: użytkownik dla którego będzie robiona weryfikacja
    :return: 2 listy filmowow - polecane i niepolecane
    """
    """Sprawdzenie czy wartosc podana w argumencie programu jest wspierana przez dataset"""
    if user not in dataset:
        raise TypeError('Cannot find ' + user + ' in the dataset')

    watchers = []

    all_movies = []
    not_watched_movies = {}
    """Zbieranie listy wszystich ogladajacych"""
    for watcher in dataset:
        watchers.append(watcher)

    """Przetwarzanie danych z pliku JSON w celu pozniejszego tworzenia propozycji filmow"""
    for watcher in watchers:
        for movie in dataset[watcher]:
            if movie not in all_movies:
                all_movies.append(movie)
            if movie not in dataset[user]:
                if movie not in not_watched_movies:
                    not_watched_movies[movie] = 0
            if movie in not_watched_movies:
                not_watched_movies[movie] += dataset[watcher][movie]

    """Zmienna przechowujaca top5 najlepiej ocenianych filmow ktorych podany uzytkownik nie ogladal"""
    max5 = dict(sorted(not_watched_movies.items(), key=operator.itemgetter(1), reverse=True)[:5])
    """Zmienna przechowujaca top5 najgorzej ocenianych filmow ktorych podany uzytkownik nie ogladal"""
    min5 = dict(sorted(not_watched_movies.items(), key=operator.itemgetter(1))[:5])
    print("5 recommended movies to watch for "+user+":")
    for movie in max5:
        print(" - " + movie)
    print("\n5 movies to be avoided by "+user+":")
    for movie in min5:
        print(" - " + movie)

if __name__ == '__main__':
    """
    Glowny fragment programu wywolujacy wszystkie zaimplementowane funckje
    """
    args = build_arg_parser().parse_args()
    user = args.user

    movies_db = 'movie_ratings.json'
    with open(movies_db, 'r', encoding="utf-8") as f:
        data = json.loads(f.read())

    movie_recomendation(data, user)

