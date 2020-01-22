CREATE TABLE #vlfcounts 
(dbname sysname,
vlfcount int); 
EXECUTE master.dbo.get_vlf;