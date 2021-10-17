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
    program TEXT,
    FOREIGN KEY (program)
        REFERENCES PROGRAM(name)
);

CREATE TABLE IF NOT EXISTS REVIEW (
    rid INTEGER PRIMARY KEY,
    user TEXT NOT NULL,
    date TEXT NOT NULL,
    location TEXT NOT NULL,
    text TEXT NOT NULL,
    stars TEXT NOT NULL,
    price TEXT NOT NULL,
    FOREIGN KEY (user) 
        REFERENCES USER (name),
    FOREIGN KEY (location) 
        REFERENCES LOCATION (name)
);