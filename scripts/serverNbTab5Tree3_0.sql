SELECT 
ROW_NUMBER() OVER(ORDER BY [severity] ASC) AS [No],
ISNULL(id,LEN('id')) id,
ISNULL(name,LEN('name')) name,
ISNULL(severity,LEN('severity')) severity,
ISNULL(Enabled,LEN('Enabled')) [Enabled] 
FROM
(SELECT 
id,
name,
severity,
CASE WHEN enabled=0 
THEN 'No' 
ELSE 'Yes'
END AS Enabled 
FROM msdb.dbo.sysalerts
UNION
SELECT 
CONVERT(nvarchar(100),max(cast(round(len(id)*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(name)*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(severity)*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len('Yes')*1.5,0) as int)))
FROM msdb.dbo.sysalerts)temp