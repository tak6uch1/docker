CREATE TABLE address_book (name varchar(255), address varchar(255));
GRANT ALL ON address_book TO dbuser;
INSERT INTO address_book(
            name,   address)
    VALUES ('User', 'Tokyo Japan'),
           ('John', 'Calif US');
