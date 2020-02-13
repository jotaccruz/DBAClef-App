SELECT 'Account Retry Delay' as Component,
paramvalue as retry_sec 
FROM msdb.dbo.sysmail_configuration 
WHERE paramname = 'AccountRetryDelay';