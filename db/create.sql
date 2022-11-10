-- Feel free to modify this file to match your development goal.
-- Here we only create 3 tables for demo purpose.
 
CREATE TABLE Users (
   id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
   email VARCHAR UNIQUE NOT NULL,
   password VARCHAR(255) NOT NULL,
   firstname VARCHAR(255) NOT NULL,
   lastname VARCHAR(255) NOT NULL,
   seller BOOLEAN DEFAULT FALSE,
   balance FLOAT NOT NULL DEFAULT 0.00,
   address VARCHAR(255) NOT NULL
);
 
CREATE TABLE Products (
   id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
   name VARCHAR(255) UNIQUE NOT NULL,
   -- category VARCHAR(255) UNIQUE NOT NULL,
   description VARCHAR(1024),
   price DECIMAL(12,2) NOT NULL,
   available BOOLEAN DEFAULT FALSE
);
 
CREATE TABLE Purchases (
   id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
   uid INT NOT NULL REFERENCES Users(id),
   pid INT NOT NULL REFERENCES Products(id),
   time_purchased timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
   fulfillment_status BOOLEAN DEFAULT FALSE
);
 
CREATE TABLE Feedback (
   id INT NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
   uid INT,
   pid INT REFERENCES Products(id),
   sid INT REFERENCES Users(id),
   submitted_timestamp timestamp without time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),
   review VARCHAR(1024),
   rating INT
);

CREATE TABLE Carts (
    uid INT NOT NULL REFERENCES Users(id),
    pid INT NOT NULL REFERENCES Products(id),
    quantity INT NOT NULL,
    u_price FLOAT NOT NULL
);

CREATE TABLE Inventory(
   sid INT NOT NULL REFERENCES Users(id),
   pid INT NOT NULL REFERENCES Products(id),
   quantity INT NOT NULL,
   u_price FLOAT NOT NULL  
);
