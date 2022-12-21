use codetest;

CREATE TABLE IF NOT EXISTS places(
    PLACE_ID int not null Auto_Increment PRIMARY KEY,
    CITY varchar(100),
    COUNTY varchar(100),
    COUNTRY varchar(100)
)
;
CREATE TABLE IF NOT EXISTS people(
    PERSON_ID int not null Auto_Increment PRIMARY KEY,
    GIVEN_NAME VARCHAR(100),
    FAMILY_NAME VARCHAR(100),
    DATE_OF_BIRTH DATE,
    PLACE_OF_BIRTH VARCHAR(100)
)
;