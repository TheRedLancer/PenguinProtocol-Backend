CREATE TABLE LOCATION (
    lid INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL
);

CREATE TABLE REVIEW (
    rid INTEGER PRIMARY KEY,
    uid INTEGER NOT NULL,
    date INTEGER NOT NULL,
    location TEXT NOT NULL,
    text TEXT NOT NULL,
    stars INTEGER NOT NULL CHECK (stars >= 1 AND stars <= 5),
    price INTEGER NOT NULL CHECK (price >= 1 AND price <= 3)
);

CREATE TABLE PROGRAM (
    pid INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    school TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL
);

CREATE TABLE USER (
    uid INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    sem_attend TEXT NOT NULL,
    program INTEGER,
    FOREIGN KEY (program) REFERENCES PROGRAM(pid)
);