SELECT 
id,
name,
severity,
CASE WHEN enabled=0 
THEN 'No' 
ELSE 'Yes'
END AS Enabled 
FROM msdb.dbo.sysalerts