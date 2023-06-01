CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS genre (
    id INTEGER PRIMARY KEY,
    genre_name VARCHAR(50),
    game_id INTEGER
);

CREATE TABLE IF NOT EXISTS studio (
    id INTEGER PRIMARY KEY,
    studio_name VARCHAR(100),
    game_id INTEGER
);

CREATE TABLE IF NOT EXISTS publisher (
    id INTEGER PRIMARY KEY,
    publisher_name VARCHAR(100),
    game_id INTEGER
);

CREATE TABLE IF NOT EXISTS platforms (
    id INTEGER PRIMARY KEY,
    platform_name VARCHAR(100),
    game_id INTEGER
);

CREATE TABLE IF NOT EXISTS release_date (
    id INTEGER PRIMARY KEY,
    date DATE,
    game_id INTEGER
);

CREATE TABLE IF NOT EXISTS desire_to_play (
    id INTEGER PRIMARY KEY,
    desire INTEGER,
    game_id INTEGER
);


-- External Info Tables

CREATE TABLE IF NOT EXISTS completion_time (
    id INTEGER PRIMARY KEY,
    main_story_length TIME,
    full_percent_length TIME,
    game_id INTEGER
);

CREATE TABLE IF NOT EXISTS metacritic (
    id INTEGER PRIMARY KEY,
    critic_score INTEGER,
    user_score INTEGER,
    game_id INTEGER
);

CREATE TABLE IF NOT EXISTS protondb (
    id INTEGER PRIMARY KEY,
    rating INTEGER,
    entry_no INTEGER,
    game_id INTEGER
);