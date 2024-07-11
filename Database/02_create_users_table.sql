CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    server_id INTEGER,
    FOREIGN KEY (server_id) REFERENCES servers(id)
    )
