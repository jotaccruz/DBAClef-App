IF OBJECT_ID('tempdb..#IFI') IS NOT NULL 
DROP TABLE #IFI; 
CREATE TABLE #IFI 
(LogDate datetime, 
ProcessInfo nvarchar(250), 
Text nvarchar(500));

INSERT INTO #IFI 
EXEC sys.xp_readerrorlog 0, 1, N'Database Instant File Initialization';