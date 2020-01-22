-- SQL Server Agent enabled
SELECT CASE WHEN CAST(value_in_use AS INT)=0 THEN 'Disabled;' ELSE 'Enabled' END AS SQLAgentEnabled FROM sys.configurations WHERE [name] ='Agent XPs';

-- SQL Server Agent status
IF (SELECT CAST(SERVERPROPERTY('Edition') AS VARCHAR(30))) NOT LIKE 'Express Edition%' BEGIN SELECT CASE WHEN status_desc = 'Running' THEN 'Running' ELSE 'Stopped' END AS SQLAgentStarted FROM sys.dm_server_services WHERE servicename LIKE 'SQL Server Agent%' END;

-- SQL Database Mail is enabled
SELECT CASE WHEN CAST(value_in_use AS INT)=0 THEN 'Disabled;' ELSE 'Enabled' END AS DBMailEnabled  FROM sys.configurations WHERE [name] ='Database Mail XPs';

-- @SQLAgentMailEnabled
SELECT CASE WHEN COUNT(*) > 0 THEN 'Enabled' ELSE 'Disabled' END AS SQLAgentMailEnabled FROM msdb.dbo.sysmail_profile;

-- @MailAccountEnabled
SELECT CASE WHEN COUNT(*) > 0 THEN 'Enabled' ELSE 'Disabled' END AS MailAccountEnabled FROM msdb.dbo.sysmail_account;

-- SQL Server Agent is enabled to use Database Mail
DECLARE @SQLAgentMailEnabled INT = 0; EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE', N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent', N'UseDatabaseMail', @SQLAgentMailEnabled OUTPUT; SELECT CASE WHEN @SQLAgentMailEnabled=1 THEN 'Enabled' ELSE 'Disabled' END AS SQLAgentMailEnabled

-- SQL Server Agent is enabled to use Database Mail and Mail Profile is assigned
DECLARE @SQLAgentMailProfileEnabled SYSNAME; EXECUTE master.dbo.xp_instance_regread N'HKEY_LOCAL_MACHINE',N'SOFTWARE\Microsoft\MSSQLServer\SQLServerAgent',N'DatabaseMailProfile', @SQLAgentMailProfileEnabled OUTPUT; SELECT CASE WHEN @SQLAgentMailProfileEnabled=1 THEN 'Enabled' ELSE 'Disabled' END AS SQLAgentMailProfileEnabled

---- Testing email
--DECLARE @profile SYSNAME, @retry_sec INT, @retry VARCHAR(10)

---- Find Mail profile name
--SELECT TOP 1 @profile = [name] 
--FROM msdb.dbo.sysmail_profile 
--ORDER BY  profile_id ;

--select @profile profile 

-- get email retry interval configuration value
SELECT paramvalue as retry_sec FROM msdb.dbo.sysmail_configuration WHERE paramname = 'AccountRetryDelay';


---- Check if there are failed emails for the last 24 hours
--SELECT @failed_emails_last24hours = COUNT(*) 
--FROM msdb.dbo.sysmail_event_log
--WHERE event_type='error' AND log_date > DATEADD(dd, -1, GETDATE());
--SELECT @failed_emails_last24hours failed_emails_last24hours

------ Send Test email
----BEGIN TRY
----   EXEC msdb.dbo.sp_send_dbmail
----      @profile_name = @profile, 
----             @recipients = $(DBA_Email),
----             @subject = 'Daily Test DB Mail',
----             @body = @@SERVERNAME
----END TRY

----BEGIN CATCH
----   SELECT @failed_email_error = ERROR_NUMBER() 
----END CATCH;

------ wait for retry interval (from DB mail configuration) plus 5 more seconds
----WAITFOR DELAY @retry
------ WAITFOR DELAY '00:00:05' -- or set it to fixe 5 seconds if you don't want to wait

------ Check if the test email failed
----SELECT @failed_email_test = CASE WHEN COUNT(*) > 0 THEN 1 ELSE 0 END
----FROM msdb.dbo.sysmail_event_log
----WHERE event_type='error' AND
----   log_date > DATEADD(ss, @retry_sec + 5, GETDATE());

---- Final report
--SELECT @@SERVERNAME AS Server_Name, 
--   CAST(GETDATE() AS SMALLDATETIME) AS Run_Date,
--   Control = @SQLAgentEnabled * @SQLAgentStarted * @DBMailEnabled * @MailProfileEnabled * @MailAccountEnabled * @SQLAgentMailEnabled * 
--         (CASE WHEN @SQLAgentMailProfileEnabled IS NOT NULL THEN 1 ELSE 0 END) * 
--         (CASE WHEN ISNULL(@failed_email_error, 0) = 0 THEN 1 ELSE 0 END) *
--         (CASE WHEN @failed_emails_last24hours = 0 THEN 1 ELSE 0 END),
--   Notes =  CASE WHEN CAST(SERVERPROPERTY('Edition') AS VARCHAR(30)) LIKE 'Express Edition%' 
--         THEN 'Express Edition, DB Mail not supported' ELSE 
--         CASE WHEN @SQLAgentEnabled = 0 THEN 'SQL Agent disabled; ' 
--            ELSE '' END +
--         CASE WHEN @DBMailEnabled = 0 THEN 'DB Mail disabled; ' 
--            ELSE '' END +
--         CASE WHEN @MailProfileEnabled = 0 THEN 'Mail Profile disabled; ' 
--            ELSE '' END + 
--         CASE WHEN @MailAccountEnabled = 0 THEN 'Mail Account disabled; ' 
--            ELSE '' END + 
--         CASE WHEN @SQLAgentMailEnabled = 0 THEN 'SQL Agent Mail disabled; ' 
--            ELSE '' END + 
--         CASE WHEN @SQLAgentMailProfileEnabled IS NOT NULL THEN '' 
--            ELSE 'SQL Agent Mail Profile disabled; ' END + 
--         CASE WHEN @failed_emails_last24hours > 0 
--            THEN 'failed email(s) during last 24 hours; ' ELSE '' END +
--         CASE WHEN @failed_email_error > 0 THEN 'failed email test; ' ELSE '' END END;