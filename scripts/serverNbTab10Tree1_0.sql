SELECT 
ROW_NUMBER() OVER(ORDER BY STATUS ASC,TYPE ASC, CREATION ASC) AS [No],*
FROM
(SELECT 
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
UNION
SELECT
CONVERT(nvarchar(100),max(cast(round(len(name)*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(type_desc)*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len('DISABLED')*1.5,0) as int))), 
CONVERT(nvarchar(100),max(cast(round(len(convert(nvarchar(11), create_date))*1.5,0) as int))), 
CONVERT(nvarchar(100),max(cast(round(len(default_database_name)*1.5,0) as int)))
FROM master.sys.server_principals 
WHERE IS_SRVROLEMEMBER ('sysadmin',name) = 1)temp