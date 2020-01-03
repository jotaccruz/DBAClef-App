use master;
IF  NOT EXISTS (
	SELECT name 
		FROM sys.databases 
		WHERE name = N'DBAdmin'
)
BEGIN
	CREATE DATABASE DBAdmin;
	ALTER DATABASE DBAdmin SET RECOVERY SIMPLE;
END;
use DBAdmin;
exec sp_changedbowner sa;
IF  EXISTS (
	SELECT name 
		FROM sys.databases 
		WHERE name = N'DBAdmin'
)
BEGIN
	SELECT 'DBAdmin was created successfully' AS Result
END;


--Stages:
--1. Defaulth Paths
--2. DBAdmin
--2. ServerName
--3. Memory
--4. DBmail
--5. Operator
--6. Alerts
