# Movies
# Author : Anteon Ervin


class Movie:
   
    def __init__(self, title, description, actors, genre, rating):
        self.title = title
        self.description = description
        self.actors = actors
        self.genre = genre
        self.rating = rating
        
    def is_match(self, title):
        if self.title == title:
            return True
        else:
            return False
            
    def display(self):
        
                
                print(f"""
*** {self.title} ***
{self.description}
Stars:""")
                for actor in self.actors:
                    print(f'-{actor}')
                print(f"""
Genre: {self.genre}  
Rating: {self.rating}
""")