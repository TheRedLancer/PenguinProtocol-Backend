INSERT INTO LOCATION (lid, name, address, city, country)
    VALUES
        (1, "pizza", "123 South", "Spokane", "WA")
        (2, "tacos", "555 North", "Spokane", "WA")
        (3, "burger", "983 West", "Seattle", "WA")
        (4, "pizza", "123 South", "Los Angeles", "CA");
    
INSERT INTO PROGRAM (pid, name, school, city, country)
    VALUES
        (5, "gu-in-florence", "Gonzaga University", "Spokane", "WA")
        (6, "UW-in-Brazil", "University of Washington", "Seattle", "WA");

INSERT INTO USER (uid, name, sem_attend, program)
    VALUES
        (7, "Zach", "Fall 21", "5")
        (8, "Ariana", "Spring 22", "5")
        (9, "Daniel", "Winter 18", "6")
        (10, "Maddie", "Spring 22", "6")
        (11, "Jaymin", "Summer 19", "5")

INSERT INTO REVIEW (rid, user, date, location, text, stars, price)
    VALUES
        (12, 7, 1634420735, 1, "terrible staff", 1, 3)
        (13, 7, 1634420735, 2, "tasty taco", 5, 2)
        (14, 8, 1653083135, 4, "good pizza", 4, 1)
        (15, 9, 1516398335, 3, "pretty expensive", 3, 3)
        (16, 10, 1652996735, 4, "fun atmosphere", 5, 3)
        (17, 11, 1563572735, 3, "great cheeseburger", 4, 1)
        