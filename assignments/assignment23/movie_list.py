# Movie list
# Author: Anteon Ervin

from movie import Movie

movies_list = (
    Movie("No Time To Die", "Bond has left active service.", ("Daniel Craig", "Ana de Armas", "Rami Malek"),"Thriller","7.4 stars"),
    Movie("The Last Letter from Your Lover", "A pair of interwoven stories set in the past and present",("Shailene Woodley", "Joe Alwyn", "Wendy Nottingham"), "Romance","6.7 stars"),
    Movie("Passing", "Passing follows the unexpected reunion of two high school friend", ("Tessa Thompson", "Ruth Negga", "Andre Holland"), "Drama", "6.6 stars"),
    Movie("Last Night in Soho", "An aspiring fashion designer is mysteriously able to enter the 1960s", ("Thomasin Mckenzie", "Anya Taylor-Joy", "Matt Smith"), "Mystery", "7.2 stars")
    )
    


print("***** Movie Listings *****")

while True:
    command = input("(L)ist all movies, get a movie (D)etails, or (Q)uit ").strip().lower()

    if command == "q":
        break
    if command == "l":
        for movie in movies_list:
            movie.display()
    elif command == "d":
        title = input("Enter Movie Name: ")
        
        for movie in movies_list:
            if movie.is_match(title):
                movie.display()
                
    else:
        print("Invalid command")
print("Goodbye")