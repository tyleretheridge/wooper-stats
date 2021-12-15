DROP TABLE IF EXISTS twitch.streams;
DROP SCHEMA IF EXISTS twitch
CREATE SCHEMA twitch;
CREATE TABLE twitch.streams (
    user_id VARCHAR(50),
    user_login VARCHAR(50),
    game_name VARCHAR(50),
    viewer_count INT,
    language VARCHAR,
    is_mature BOOLEAN
)