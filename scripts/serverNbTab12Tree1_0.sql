CREATE TABLE #dbcc_log 
(Dbname nvarchar(250),
LogSizeMB int,
LogSpaceUsed numeric(4,2),
Stat int);

INSERT INTO #dbcc_log 
EXEC ('DBCC SQLPERF(logspace)');