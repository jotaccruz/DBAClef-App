SELECT
tl.name NAME, 
ISNULL(type_desc,'Missing') TYPE,
CASE is_disabled 
WHEN 0 THEN 'ENABLED'
WHEN 1 THEN 'DISABLED'
END STATUS, 
convert(nvarchar(11), create_date) CREATION, 
default_database_name DB
FROM #StandardsLogins tl
LEFT JOIN master.sys.server_principals l
ON l.name=tl.NAME
ORDER BY STATUS ASC,TYPE ASC, CREATION ASC;