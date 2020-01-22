CREATE TABLE #SQLAgentMailProfile 
(SQLAgentMailProfile nvarchar(20),
dat sysname null);

INSERT INTO #SQLAgentMailProfile 
EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE',N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',N'DatabaseMailProfile';