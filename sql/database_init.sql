CREATE SCHEMA IF NOT EXISTS twitch;
CREATE TABLE IF NOT EXISTS twitch.streams (
    user_id VARCHAR(50),
    user_login VARCHAR(50),
    game_name VARCHAR(50),
    viewer_count INT,
    language VARCHAR,
    stream_date DATETIME
    PRIMARY KEY (user_id)
);
