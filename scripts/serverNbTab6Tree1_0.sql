CREATE TABLE #DBmail
(Component nvarchar(100),
Val nvarchar(100)
)
INSERT INTO #DBmail
SELECT 'SQL Agent XPs' as Component,
CASE WHEN CAST(value_in_use AS INT)=0 
THEN 'Disabled' 
ELSE 'Enabled' 
END AS SQLAgentEnabled
FROM sys.configurations 
WHERE [name] ='Agent XPs';


IF (SELECT CAST(SERVERPROPERTY('Edition') AS VARCHAR(30))) NOT LIKE 'Express Edition%' 
BEGIN
	IF (SELECT @@version) NOT LIKE 'Microsoft SQL Server 2005%'
	BEGIN
		INSERT INTO #DBmail
		SELECT 'SQL Agent' as Component, 
		CASE WHEN status_desc = 'Running' 
		THEN 'Running' 
		ELSE 'Stopped' 
		END AS SQLAgentStarted 
		FROM sys.dm_server_services 
		WHERE servicename LIKE 'SQL Server Agent%' 
	END
	ELSE
	BEGIN
		CREATE TABLE #status (status nvarchar(100))
		DECLARE @query nvarchar(100)
		INSERT INTO #status
		EXEC xp_servicecontrol N'querystate',N'SQLSERVERAGENT'
		INSERT INTO #DBmail 
		SELECT 'SQL Agent',status FROM #status
	END
END
ELSE 
BEGIN
	INSERT INTO #DBmail
	SELECT 'SQL Agent' as Component, 'Express Edition' SQLAgentStarted 
END

INSERT INTO #DBmail
SELECT 'Database Mail XPs' as Component,
CASE WHEN CAST(value_in_use AS INT)=0 
THEN 'Disabled' 
ELSE 'Enabled' 
END AS DBMailEnabled 
FROM sys.configurations 
WHERE [name] ='Database Mail XPs';


IF EXISTS(SELECT 1 FROM msdb.dbo.sysmail_profile)
BEGIN
	INSERT INTO #DBmail
	SELECT 'Mail Profile' as Component, name AS MailProfile FROM msdb.dbo.sysmail_profile;
END
ELSE
BEGIN
	INSERT INTO #DBmail
	SELECT 'Mail Profile' as Component, 'Missing' AS MailProfile
END


IF EXISTS(SELECT 1 FROM msdb.dbo.sysmail_account)
BEGIN
	INSERT INTO #DBmail
	SELECT 'Mail Account' as Component, name AS MailAccount FROM msdb.dbo.sysmail_account
END
ELSE
BEGIN
	INSERT INTO #DBmail
	SELECT 'Mail Account' as Component, 'Missing' AS MailProfile
END


CREATE TABLE #SQLAgentMailEnabled 
(
SQLAgentMailEnabled nvarchar(15),
Datos INT);
INSERT INTO #SQLAgentMailEnabled 
EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent', N'UseDatabaseMail';

IF EXISTS (SELECT SQLAgentMailEnabled FROM #SQLAgentMailEnabled) 
BEGIN 
	INSERT INTO #DBmail
	SELECT 'SQL Agent Mail Enabled' as Component,
	CASE WHEN Datos=1 
	THEN 'Enabled' 
	ELSE 'Disabled' 
	END AS SQLAgentMailEnabled 
	FROM #SQLAgentMailEnabled 
END 
ELSE 
BEGIN
	INSERT INTO #DBmail
	SELECT 'SQL Agent Mail Enabled' as Component, 'Express Edition' AS SQLAgentMailEnabled 
END;


CREATE TABLE #SQLAgentMailProfile 
(SQLAgentMailProfile nvarchar(20),
dat sysname null);

INSERT INTO #SQLAgentMailProfile 
EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE',N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',N'DatabaseMailProfile';

IF EXISTS (SELECT SQLAgentMailProfile FROM #SQLAgentMailProfile) 
BEGIN
	INSERT INTO #DBmail
	SELECT 'SQL Agent Mail Profile' Component , ISNULL(dat,'Missing') [profile] 
	FROM #SQLAgentMailProfile 
END 
ELSE 
BEGIN
	INSERT INTO #DBmail
	SELECT 'SQL Agent Mail Profile' Component, 'Express Edition' [profile]
END;


INSERT INTO #DBmail
SELECT 'Account Retry Delay' as Component,
paramvalue as retry_sec 
FROM msdb.dbo.sysmail_configuration 
WHERE paramname = 'AccountRetryDelay';