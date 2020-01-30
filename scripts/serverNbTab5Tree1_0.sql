SELECT 
name,
email_address,
CASE WHEN enabled=0 
THEN 'No' 
ELSE 'Yes' 
END AS Enabled,
CASE WHEN pager_days=0 
THEN 'All' 
ELSE 'Some days'
END AS Notifications 
FROM msdb.dbo.sysoperators 
WHERE enabled = 1
and name = 'DBA TICA'