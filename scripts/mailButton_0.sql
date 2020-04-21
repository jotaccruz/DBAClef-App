--================================================================
-- DATABASE MAIL CONFIGURATION
--================================================================
--==========================================================
-- Create a Database Mail account
--==========================================================
DECLARE @profile_id INT
DECLARE @profile_description sysname
DECLARE @profile_name nvarchar(50)
DECLARE @account_name nvarchar(50)
DECLARE @email_address nvarchar(250)
DECLARE @display_name nvarchar(250)
DECLARE @mailserver_name nvarchar(50)
DECLARE @description nvarchar(250)
DECLARE @port int;

SELECT @profile_id = COALESCE(MAX(profile_id),1) FROM msdb.dbo.sysmail_profile
SELECT @email_address='no-reply@telusinternational.com'
SELECT @display_name = CONVERT(nvarchar(250),@@servername) + ' Database Notification'
SELECT @mailserver_name = '172.17.64.124'
SELECT @account_name = 'DBA'
SELECT @profile_name = 'dba_profile'
SELECT @description = 'Email account for sending alerts and errors'
SELECT @profile_description = 'Database Mail Profile for ' + @@servername
SELECT @port = 25;

IF NOT EXISTS(SELECT name AS MailAccount FROM msdb.dbo.sysmail_account WHERE name = @account_name)
BEGIN
EXECUTE msdb.dbo.sysmail_add_account_sp
    @account_name = @account_name,
    @description = @description,
    @email_address = @email_address,
    @replyto_address = @email_address,
    @display_name = @display_name,
    @mailserver_name = @mailserver_name,
	@port = @port;
END

--==========================================================
-- Create a Database Mail Profile
--==========================================================
IF NOT EXISTS(SELECT name AS MailProfile FROM msdb.dbo.sysmail_profile WHERE name = @profile_name)
BEGIN
EXECUTE msdb.dbo.sysmail_add_profile_sp
    @profile_name = @profile_name,
    @description = @profile_description;

-- Add the account to the profile
EXECUTE msdb.dbo.sysmail_add_profileaccount_sp
    @profile_name = @profile_name,
    @account_name = @account_name,
    @sequence_number = @profile_id;

-- Grant access to the profile to the DBMailUsers role
EXECUTE msdb.dbo.sysmail_add_principalprofile_sp
    @profile_name = @profile_name,
    @principal_id = 0,
    @is_default = 1 ;
END
--==========================================================
-- Enable Database Mail
--==========================================================
USE master;
exec sp_configure 'show advanced', 1;
RECONFIGURE WITH OVERRIDE;
exec sp_configure 'Agent XPs',1
RECONFIGURE WITH OVERRIDE;
exec sp_configure 'Database Mail XPs', 1;
RECONFIGURE WITH OVERRIDE;
exec sp_configure 'show advanced', 0;
RECONFIGURE WITH OVERRIDE;

exec msdb.dbo.sp_set_sqlagent_properties @email_save_in_sent_folder = 0;

--================================================================
-- SQL Agent Properties Configuration
--================================================================
EXEC msdb.dbo.sp_set_sqlagent_properties 
	@email_profile = @profile_name
	, @use_databasemail=1;

EXEC msdb.dbo.sp_set_sqlagent_properties @databasemail_profile=@profile_name;