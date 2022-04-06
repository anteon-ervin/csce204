# Movie list
# Author: Anteon Ervin

from movie import Movie

def get_movies():
    movies = []

    with open("assignments/assignment24/movies.txt") as file:
        for line in file:
            data = line.split(",") 
            title = data[0].strip()
            description = data[1].strip()
            actors = data[2].strip().split('*')
            genre = data[3].strip().lower()
            rating = data[4].strip()
            movies.append(Movie(title, description, actors, genre, rating))
        return movies
    
movies = get_movies()
print("***** Movie Listings *****")

while True:
    command = input("(L)ist all movies, get a movie (D)etails, or (Q)uit ").strip().lower()

    if command == "q":
        break
    if command == "l":
        for movie in movies:
            movie.display()
    elif command == "d":
        title = input("Enter Movie Name: ")
        
        for movie in movies:
            if movie.is_match(title):
                movie.display()
                
    else:
        print("Invalid command")
print("Goodbye")