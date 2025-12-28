
import sqlite3

DB_PATH = "movies.db"


def prepare_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Drop tables if they exist
    cursor.execute("DROP TABLE IF EXISTS MovieGenres")
    cursor.execute("DROP TABLE IF EXISTS Genres")
    cursor.execute("DROP TABLE IF EXISTS Movies")

    # Create Movies table
    cursor.execute("""
    CREATE TABLE Movies (
        MovieID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        ReleaseYear INTEGER,
        Rating REAL
    )
    """)

    # Create Genres table
    cursor.execute("""
    CREATE TABLE Genres (
        GenreID INTEGER PRIMARY KEY AUTOINCREMENT,
        GenreName TEXT NOT NULL
    )
    """)

    # Create MovieGenres table (many-to-many)
    cursor.execute("""
    CREATE TABLE MovieGenres (
        MovieID INTEGER,
        GenreID INTEGER,
        FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
        FOREIGN KEY (GenreID) REFERENCES Genres(GenreID)
    )
    """)

    # Insert Genres
    genres = [
        ("Action",),
        ("Drama",),
        ("Comedy",),
        ("Sci-Fi",),
        ("Thriller",)
    ]
    cursor.executemany(
        "INSERT INTO Genres (GenreName) VALUES (?)",
        genres
    )

    # Insert Movies
    movies = [
        ("Inception", 2010, 8.8),
        ("The Dark Knight", 2008, 9.0),
        ("Interstellar", 2014, 8.6),
        ("The Matrix", 1999, 8.7),
        ("Gladiator", 2000, 8.5)
    ]
    cursor.executemany(
        "INSERT INTO Movies (Title, ReleaseYear, Rating) VALUES (?, ?, ?)",
        movies
    )

    # Link Movies to Genres
    movie_genres = [
        (1, 4),  # Inception -> Sci-Fi
        (2, 1),  # Dark Knight -> Action
        (2, 5),  # Dark Knight -> Thriller
        (3, 4),  # Interstellar -> Sci-Fi
        (4, 4),  # Matrix -> Sci-Fi
        (5, 1),  # Gladiator -> Action
        (5, 2)   # Gladiator -> Drama
    ]
    cursor.executemany(
        "INSERT INTO MovieGenres (MovieID, GenreID) VALUES (?, ?)",
        movie_genres
    )

    conn.commit()
    conn.close()

    print("Database prepared successfully.")


if __name__ == "__main__":
    prepare_database()
cd C:\New folder
python prepare_db.py
