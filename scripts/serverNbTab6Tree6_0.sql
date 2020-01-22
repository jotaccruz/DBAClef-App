CREATE TABLE #SQLAgentMailEnabled 
(
SQLAgentMailEnabled nvarchar(15),
Datos INT);
INSERT INTO #SQLAgentMailEnabled 
EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent', N'UseDatabaseMail';