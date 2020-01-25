IF (SELECT CAST(SERVERPROPERTY('Edition') AS VARCHAR(30))) NOT LIKE 'Express Edition%' 
BEGIN
	IF (SELECT @@version) NOT LIKE 'Microsoft SQL Server 2005%'
	BEGIN
		SELECT 
		CASE WHEN status_desc = 'Running' 
		THEN 'Running.' 
		ELSE 'Stopped.' 
		END AS SQLAgentStarted 
		FROM sys.dm_server_services 
		WHERE servicename LIKE 'SQL Server Agent%' 
	END
	ELSE
	BEGIN
		EXEC xp_servicecontrol N'querystate',N'SQLSERVERAGENT'
	END
END
ELSE 
BEGIN 
	SELECT 'Express Edition' SQLAgentStarted 
END;

