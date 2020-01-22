SELECT 
name NAME, 
type_desc TYPE, 
CASE WHEN is_disabled = 0 
THEN 'ENABLED' 
ELSE 'DISABLED' 
END STATUS, 
convert(nvarchar(11), create_date) CREATION, 
default_database_name DB 
FROM master.sys.server_principals 
WHERE IS_SRVROLEMEMBER ('sysadmin',name) = 1 
ORDER BY is_disabled ASC,type_desc ASC, create_date ASC;