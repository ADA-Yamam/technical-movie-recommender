"""
Database Preparation Script

Initializes SQLite database with sample movie data.
This script demonstrates ETL (Extract, Transform, Load) pipeline basics.
"""

import sqlite3
import pandas as pd
from pathlib import Path


def create_database(db_path: str = "movies.db"):
    """
    Create SQLite database and initialize schema.

    Args:
        db_path: Path to the database file
    """
    # Remove existing database if it exists
    db_file = Path(db_path)
    if db_file.exists():
        db_file.unlink()
        print(f"🗑️  Removed existing database: {db_path}")

    # Create connection
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create movies table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            MovieID INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL UNIQUE,
            ReleaseYear INTEGER NOT NULL,
            Rating REAL NOT NULL CHECK(Rating >= 0 AND Rating <= 10)
        )
    """)

    print("✅ Database schema created")
    return conn


def load_sample_data(conn: sqlite3.Connection):
    """
    Load sample movie data into the database.

    Args:
        conn: SQLite database connection
    """
    # Sample movie data
    movies = [
        ("The Shawshank Redemption", 1994, 9.3),
        ("The Godfather", 1972, 9.2),
        ("The Dark Knight", 2008, 9.0),
        ("Pulp Fiction", 1994, 8.9),
        ("Forrest Gump", 1994, 8.8),
        ("Inception", 2010, 8.8),
        ("The Matrix", 1999, 8.7),
        ("Goodfellas", 1990, 8.7),
        ("Interstellar", 2014, 8.6),
        ("The Silence of the Lambs", 1991, 8.6),
        ("Saving Private Ryan", 1998, 8.6),
        ("The Green Mile", 1999, 8.6),
        ("Parasite", 2019, 8.6),
        ("The Usual Suspects", 1995, 8.5),
        ("Gladiator", 2000, 8.5),
    ]

    cursor = conn.cursor()

    # Insert data
    for title, year, rating in movies:
        try:
            cursor.execute(
                "INSERT INTO movies (Title, ReleaseYear, Rating) VALUES (?, ?, ?)",
                (title, year, rating)
            )
        except sqlite3.IntegrityError:
            print(f"⚠️  Movie '{title}' already exists")

    conn.commit()
    print(f"✅ Loaded {len(movies)} movies into database")


def verify_data(conn: sqlite3.Connection):
    """
    Verify the loaded data.

    Args:
        conn: SQLite database connection
    """
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM movies")
    count = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(Rating) FROM movies")
    avg_rating = cursor.fetchone()[0]

    cursor.execute("SELECT MIN(ReleaseYear), MAX(ReleaseYear) FROM movies")
    min_year, max_year = cursor.fetchone()

    print("\n📊 Database Verification:")
    print(f"   Total movies: {count}")
    print(f"   Average rating: {avg_rating:.2f}")
    print(f"   Year range: {min_year} - {max_year}")

    # Display sample data
    print("\n📋 Sample Data:")
    cursor.execute("SELECT * FROM movies LIMIT 5")
    for row in cursor.fetchall():
        print(f"   {row}")


def main():
    """Main execution function."""
    print("🎬 Movie Database Preparation\n")

    db_path = "movies.db"

    # Create database
    conn = create_database(db_path)

    # Load sample data
    load_sample_data(conn)

    # Verify data
    verify_data(conn)

    # Close connection
    conn.close()

    print(f"\n✅ Database preparation complete!")
    print(f"   Database file: {db_path}")
    print(f"   Ready for recommendation system")


if __name__ == "__main__":
    main()
