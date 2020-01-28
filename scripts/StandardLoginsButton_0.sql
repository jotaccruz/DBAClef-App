--DROP TABLE #StandardsLogins
CREATE TABLE #StandardsLogins
(NAME nvarchar(400));

INSERT INTO #StandardsLogins (NAME)
VALUES ('TI\GR_DBAAdmin')
INSERT INTO #StandardsLogins (NAME)
VALUES ('TI\solarwinds.sam')
INSERT INTO #StandardsLogins (NAME)
VALUES ('TI\dba.backup');
IF NOT EXISTS(
SELECT
tl.name NAME, 
ISNULL(type_desc,'Missing') TYPE,
CASE is_disabled 
WHEN 0 THEN 'ENABLED'
WHEN 1 THEN 'DISABLED'
END STATUS, 
convert(nvarchar(11), create_date) CREATION, 
default_database_name DB
FROM #StandardsLogins tl
LEFT JOIN master.sys.server_principals l
ON l.name=tl.NAME
WHERE 
l.name = 'ti\solarwinds.sam'
)
BEGIN
CREATE LOGIN "ti\solarwinds.sam" FROM WINDOWS;
GRANT VIEW SERVER STATE TO "ti\solarwinds.sam";
GRANT VIEW ANY DEFINITION TO "ti\solarwinds.sam";
--EXEC sp_adduser @loginame = "ti\solarwinds.sam" ,@name_in_db = "ti\solarwinds.sam";
EXECUTE sp_MSforeachdb 'USE [?]; EXEC sp_adduser @loginame = ''ti\solarwinds.sam'', @name_in_db = ''ti\solarwinds.sam'''
USE msdb;
EXEC sp_addrolemember N'db_datareader', N'ti\solarwinds.sam';
use master;
GRANT EXECUTE ON xp_readerrorlog TO "ti\solarwinds.sam"
END;
IF NOT EXISTS(
SELECT
tl.name NAME, 
ISNULL(type_desc,'Missing') TYPE,
CASE is_disabled 
WHEN 0 THEN 'ENABLED'
WHEN 1 THEN 'DISABLED'
END STATUS, 
convert(nvarchar(11), create_date) CREATION, 
default_database_name DB
FROM #StandardsLogins tl
LEFT JOIN master.sys.server_principals l
ON l.name=tl.NAME
WHERE 
l.name = 'TI\GR_DBAAdmin'
)
BEGIN
CREATE LOGIN "TI\GR_DBAAdmin" FROM WINDOWS;
exec sp_addsrvrolemember "TI\GR_DBAAdmin", 'sysadmin';
END;
IF NOT EXISTS(
SELECT
tl.name NAME, 
ISNULL(type_desc,'Missing') TYPE,
CASE is_disabled 
WHEN 0 THEN 'ENABLED'
WHEN 1 THEN 'DISABLED'
END STATUS, 
convert(nvarchar(11), create_date) CREATION, 
default_database_name DB
FROM #StandardsLogins tl
LEFT JOIN master.sys.server_principals l
ON l.name=tl.NAME
WHERE 
l.name = 'TI\dba.backup'
)
BEGIN
CREATE LOGIN "TI\dba.backup" FROM WINDOWS;
exec sp_addsrvrolemember "TI\dba.backup", 'sysadmin';
END;