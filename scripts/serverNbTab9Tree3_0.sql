IF EXISTS (SELECT * FROM sys.databases o WHERE o.name = 'DBAdmin') 
BEGIN 
SELECT 
name,
info 
FROM 
DBAdmin.dbo.sysobjects 
WHERE name LIKE 'sp_whoisactive' 
END 
ELSE 
SELECT 'Missing' name,
'' info;