IF EXISTS(SELECT name FROM sys.databases WHERE name = 'ifitesting')
DROP DATABASE [ifitesting];
CREATE DATABASE [ifitesting]