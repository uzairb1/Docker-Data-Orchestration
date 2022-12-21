use codetest;

CREATE TABLE places(
    PLACE_ID int not null Auto_Increment,
    CITY varchar(100),
    COUNTY varchar(100),
    COUNTRY varchar(100),
    PRIMARY KEY (PLACE_ID)
)

CREATE TABLE people(
    PERSON_ID int not null Auto_Increment,
    GIVEN_NAME VARCHAR(100),
    FAMILY_NAME VARCHAR(100),
    DATE_OF_BIRTH DATE,
    PRIMARY KEY (PERSON_ID)
)