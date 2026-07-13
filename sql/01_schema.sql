-- Create the project database.
-- Run this statement while connected to the default postgres database.

CREATE DATABASE bank_customer_churn;


-- Confirm that the database was created successfully.

SELECT datname
FROM pg_database
WHERE datname = 'bank_customer_churn';


-- IMPORTANT:
-- Connect the SQL editor to bank_customer_churn before running the CREATE TABLE statement below.

CREATE TABLE customers (
    customer_id BIGINT PRIMARY KEY,
    credit_score INTEGER NOT NULL,
    country VARCHAR(50) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    age INTEGER NOT NULL,
    tenure INTEGER NOT NULL,
    balance NUMERIC(15, 2) NOT NULL,
    products_number INTEGER NOT NULL,
    credit_card BOOLEAN NOT NULL,
    active_member BOOLEAN NOT NULL,
    estimated_salary NUMERIC(15, 2) NOT NULL,
    churn BOOLEAN NOT NULL
);