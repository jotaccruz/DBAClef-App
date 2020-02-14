CREATE TABLE #databases
(name nvarchar(250),
db_size nvarchar(50),
owner nvarchar(250),
dbid int,
created datetime,
status nvarchar (500),
compatibility_level nvarchar(5)
);
INSERT INTO #databases
EXEC sp_helpdb