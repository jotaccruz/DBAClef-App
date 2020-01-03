-- =============================================
-- Create basic stored procedure template
-- =============================================

-- Drop stored procedure if it already exists
USE master;

IF EXISTS (
  SELECT * 
    FROM INFORMATION_SCHEMA.ROUTINES 
   WHERE SPECIFIC_SCHEMA = N'dbo'
     AND SPECIFIC_NAME = N'get_defaultpathdb' 
)
   DROP PROCEDURE dbo.get_defaultpathdb
GO

CREATE PROCEDURE dbo.get_defaultpathdb
	@p1 int = 0, 
	@p2 int = 0
AS
BEGIN
--Default Data directory from Registry
	INSERT INTO #RDPaths
	EXEC master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'Software\Microsoft\MSSQLServer\MSSQLServer',N'DefaultData';
--Default Data directory from the instance itself
	INSERT INTO #DPaths(Type,Location)
	VALUES('DefaultData',LEFT(CONVERT(NVARCHAR(250),SERVERPROPERTY('InstanceDefaultdataPath')),LEN(CONVERT(NVARCHAR(250),SERVERPROPERTY('InstanceDefaultdataPath')))-1));

--Default Log directory from Registry
	INSERT INTO #RDPaths
	EXEC master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'Software\Microsoft\MSSQLServer\MSSQLServer',N'DefaultLog';
--Default Log directory from the instance itself
	INSERT INTO #DPaths(Type,Location)
	VALUES('DefaultLog',LEFT(CONVERT(NVARCHAR(250),SERVERPROPERTY('InstanceDefaultLogPath')),LEN(CONVERT(NVARCHAR(250),SERVERPROPERTY('InstanceDefaultLogPath')))-1));

--Default Backup's directory from Registry
	INSERT INTO #RDPaths
	EXEC master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'Software\Microsoft\MSSQLServer\MSSQLServer',N'BackupDirectory';

--Default Error log's directory from Registry
	INSERT INTO #DPaths(Type,Location)
	VALUES('Error',SERVERPROPERTY('ErrorLogFileName'));

--DataBandera=1 When it is needed to restart the SQLServer service because "Data default directory" has changed at some time.
	DECLARE @Bandera int = 0
	DECLARE @Location nvarchar(250) = ''
	SELECT @Bandera=1,@Location=CONCAT(CONVERT(NVARCHAR(250),a.Location),'-->',CONVERT(NVARCHAR(250),b.Location))
	FROM #RDPaths a CROSS JOIN #DPaths b
	WHERE a.Type='DefaultData'
	AND a.Type=b.Type
	AND a.Location<>b.Location

	IF @Bandera=1
	BEGIN
	BEGIN TRAN
	UPDATE #DPaths SET Location=@Location,Restart=1 WHERE Type='DefaultData'
	COMMIT
	END

--LogBandera=1 When it is needed to restart the SQLServer service because "Log default directory" has changed at some time.
	--DECLARE @LogBandera int = 0
	SELECT @Bandera=0
	SELECT @Location=''
	SELECT @Bandera=1,@Location=CONCAT(CONVERT(NVARCHAR(250),a.Location),'-->',CONVERT(NVARCHAR(250),b.Location))
	FROM #RDPaths a CROSS JOIN #DPaths b
	WHERE a.Type='DefaultLog'
	AND a.Type=b.Type
	AND a.Location<>b.Location

	IF @Bandera=1
	UPDATE #DPaths SET Location=@Location,Restart=1 WHERE Type='DefaultLog'
END
-- =============================================
-- Example to execute the stored procedure
-- =============================================
--use DBAdmin;

--CREATE TABLE #DPaths(Type nvarchar(50),Location sql_variant,Restart integer);CREATE TABLE #RDPaths(Type nvarchar(50),Location sql_variant);EXECUTE dbo.get_defaultpathdb;
--CREATE TABLE #DPath(Type nvarchar(50),Location nvarchar(250),Restart integer);INSERT INTO #DPath(Type,Location,Restart) SELECT Type,CONVERT(NVARCHAR(250),Location),Restart FROM #DPaths;INSERT INTO #DPath(Type,Location) SELECT Type,CONVERT(NVARCHAR(250),Location) FROM #RDPaths WHERE Type='BackupDirectory';
--SELECT Type,Location,Restart FROM #DPath;


--SELECT 1 
--	FROM #RDPaths a CROSS JOIN #DPaths b
--	WHERE a.Type='DefaultData'
--	AND a.Type=b.Type
--	AND a.Location<>b.Location
