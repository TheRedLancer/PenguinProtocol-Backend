CREATE TABLE IF NOT EXISTS LOCATION (
    lid INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS PROGRAM (
    pid INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    school TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS USER (
    uid INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    sem_attend TEXT NOT NULL,
    program INTEGER,
    FOREIGN KEY (program) 
        REFERENCES PROGRAM(pid)
);

CREATE TABLE IF NOT EXISTS REVIEW (
    rid INTEGER PRIMARY KEY,
    user INTEGER NOT NULL,
    date INTEGER NOT NULL,
    location TEXT NOT NULL,
    text TEXT NOT NULL,
    stars INTEGER NOT NULL CHECK (stars >= 1 AND stars <= 5),
    price INTEGER NOT NULL CHECK (price >= 1 AND price <= 3),
    FOREIGN KEY (user) 
        REFERENCES USER (uid),
    FOREIGN KEY (location) 
        REFERENCES LOCATION (lid)
);