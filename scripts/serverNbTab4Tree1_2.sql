CREATE TABLE #DPaths
(Type nvarchar(50),
Location sql_variant, 
Restart integer);
CREATE TABLE #RDPaths
(Type nvarchar(50),
Location sql_variant);
EXECUTE master.dbo.get_defaultpathdb;

CREATE TABLE #DPath
(Type nvarchar(50),
Location nvarchar(250),
Restart integer);
INSERT INTO #DPath
(Type,Location,Restart)
SELECT 
Type,
CONVERT(NVARCHAR(250),Location),
Restart 
FROM #DPaths;
INSERT INTO 
#DPath(Type,Location) 
SELECT Type,CONVERT(NVARCHAR(250),Location) 
FROM #RDPaths 
WHERE Type='BackupDirectory';