CREATE DATABASE booking_db;
CREATE USER booking_admin WITH PASSWORD '1234';
ALTER ROLE booking_admin SET client_encoding TO 'utf8';
ALTER ROLE booking_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE booking_admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE booking_db TO booking_admin;