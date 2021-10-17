INSERT INTO LOCATION (lid, name, address, city, country)
    VALUES
        (1, "pizza", "123 South", "Florence", "Italy"),
        (2, "tacos", "555 North", "Florence", "Italy"),
        (3, "burger", "983 West", "Florence", "Italy"),
        (4, "bbq", "123 South", "Rio", "Brazil");
    
INSERT INTO PROGRAM (pid, name, school, city, country)
    VALUES
        (5, "gu-in-florence", "Gonzaga University", "Florence", "Italy"),
        (6, "UW-in-Brazil", "University of Washington", "Rio", "Brazil");

INSERT INTO USER (uid, name, sem_attend, program)
    VALUES
        (7, "Zach", "Fall 21", "gu-in-florence"),
        (8, "Ariana", "Spring 22", "gu-in-florence"),
        (9, "Daniel", "Winter 18", "UW-in-Brazil"),
        (10, "Maddie", "Spring 22", "UW-in-Brazil"),
        (11, "Jaymin", "Summer 19", "gu-in-florence");

INSERT INTO REVIEW (rid, user, date, location, text, stars, price)
    VALUES
        (12, "Zach", 1634420735, "pizza", "terrible staff", 1, 3),
        (13, "Zach", 1634420735, "tacos", "tasty taco", 5, 2),
        (14, "Ariana", 1653083135, "burger", "good pizza", 4, 1),
        (15, "Daniel", 1516398335, "bbq", "pretty expensive", 3, 3),
        (16, "Maddie", 1652996735, "bbq", "fun atmosphere", 5, 3),
        (17, "Jaymin", 1563572735, "burger", "great fries", 4, 1);
        