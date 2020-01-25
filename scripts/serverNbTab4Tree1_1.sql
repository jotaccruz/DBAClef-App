CREATE PROCEDURE dbo.get_defaultpathdb
	@p1 int = 0, 
	@p2 int = 0
AS
BEGIN
	INSERT INTO #RDPaths
	EXEC master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'Software\Microsoft\MSSQLServer\MSSQLServer',N'DefaultData';
	INSERT INTO #DPaths(Type,Location)
	VALUES('DefaultData',LEFT(CONVERT(NVARCHAR(250),SERVERPROPERTY('InstanceDefaultdataPath')),LEN(CONVERT(NVARCHAR(250),SERVERPROPERTY('InstanceDefaultdataPath')))-1));
	INSERT INTO #RDPaths
	EXEC master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'Software\Microsoft\MSSQLServer\MSSQLServer',N'DefaultLog';
	INSERT INTO #DPaths(Type,Location)
	VALUES('DefaultLog',LEFT(CONVERT(NVARCHAR(250),SERVERPROPERTY('InstanceDefaultLogPath')),LEN(CONVERT(NVARCHAR(250),SERVERPROPERTY('InstanceDefaultLogPath')))-1));
	INSERT INTO #RDPaths
	EXEC master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'Software\Microsoft\MSSQLServer\MSSQLServer',N'BackupDirectory';
	INSERT INTO #DPaths(Type,Location)
	VALUES('Error',SERVERPROPERTY('ErrorLogFileName'));
	DECLARE @Bandera int
	DECLARE @Location nvarchar(250)
	SELECT @Bandera = 0
	SELECT @Location = ''
	SELECT @Bandera=1,@Location=(CONVERT(NVARCHAR(250),a.Location)+'-->'+CONVERT(NVARCHAR(250),b.Location))
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
	SELECT @Bandera=0
	SELECT @Location=''
	SELECT @Bandera=1,@Location=(CONVERT(NVARCHAR(250),a.Location)+'-->'+CONVERT(NVARCHAR(250),b.Location))
	FROM #RDPaths a CROSS JOIN #DPaths b
	WHERE a.Type='DefaultLog'
	AND a.Type=b.Type
	AND a.Location<>b.Location
	IF @Bandera=1
	UPDATE #DPaths SET Location=@Location,Restart=1 WHERE Type='DefaultLog'
END;