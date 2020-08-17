IF EXISTS (
	SELECT name 
	FROM master..sysobjects
	WHERE 
	name like 'dm_server_services'
	)
	SELECT servicename [SERVICE],'SQL Server Services' [DESC], startup_type_desc [START],service_account [ACCOUNT],status_desc [STATE]
	FROM sys.dm_server_services
ELSE
	SELECT 'Missing' [SERVICE],'SQL Server Services' [DESC], '' [START],'' [ACCOUNT],'' [STATE]