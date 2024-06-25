CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL
)

CREATE TABLE IF NOT EXISTS reviews (
    id SERIAL PRIMARY KEY,
    movie_id INTEGER,
    review TEXT,
    FOREIGN KEY (movie_id) REFERENCES movies (id)
)
