class Movie:
    def __init__(self, title, genre, rating, duration):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.duration = duration

class Theater:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

class BookingSystem:
    def __init__(self):
        self.theaters = []

    def add_theater(self):
        name = input("Enter theater name: ")
        location = input("Enter theater location: ")
        capacity = int(input("Enter theater capacity: "))
        theater = Theater(name, location, capacity)
        self.theaters.append(theater)

    def add_movie_to_theater(self):
        theater_name = input("Enter theater name to add movie: ")
        for theater in self.theaters:
            if theater.name == theater_name:
                title = input("Enter movie title: ")
                genre = input("Enter movie genre: ")
                rating = input("Enter movie rating: ")
                duration = int(input("Enter movie duration (in minutes): "))
                movie = Movie(title, genre, rating, duration)
                theater.add_movie(movie)
                print(f"Movie '{title}' added to {theater_name}!")
                return
        print(f"Theater '{theater_name}' not found.")

    def display_movies(self):
        for theater in self.theaters:
            print(f"Theater: {theater.name} ({theater.location})")
            print("Movies playing:")
            for movie in theater.movies:
                print(f"- {movie.title} ({movie.genre}) [{movie.rating}] - {movie.duration} min")
            print()

    def book_ticket(self):
        theater_name = input("Enter theater name: ")
        movie_title = input("Enter movie title: ")
        num_tickets = int(input("Enter number of tickets: "))
        for theater in self.theaters:
            if theater.name == theater_name:
                for movie in theater.movies:
                    if movie.title == movie_title:
                        if num_tickets <= theater.capacity:
                            theater.capacity -= num_tickets
                            print(f"Successfully booked {num_tickets} tickets for {movie_title} at {theater_name}!")
                            return
                        else:
                            print("Sorry, the theater is full.")
                            return
                print(f"Movie '{movie_title}' not found in {theater_name}.")
                return
        print(f"Theater '{theater_name}' not found.")

# Sample usage:
booking_system = BookingSystem()

# Add theaters
num_theaters = int(input("Enter number of theaters to add: "))
for _ in range(num_theaters):
    booking_system.add_theater()

# Add movies to theaters
num_movies = int(input("Enter number of movies to add: "))
for _ in range(num_movies):
    booking_system.add_movie_to_theater()

booking_system.display_movies()

booking_system.book_ticket()
