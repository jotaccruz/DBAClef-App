SELECT 
ROW_NUMBER() OVER(ORDER BY [DESCR] ASC) AS [No],*
FROM
(SELECT 
name NAME,
description AS DESCR, 
CONVERT(nvarchar(100),value) AS VALUE, 
CONVERT(nvarchar(100),value_in_use) AS VALUEINUSE 
FROM sys.configurations 
WHERE value <> value_in_use
UNION
SELECT 
CONVERT(nvarchar(100),max(cast(round(len(name)*1.5,0) as int))), 
CONVERT(nvarchar(100),max(cast(round(len(description)*1.5,0) as int))), 
CONVERT(nvarchar(100),max(cast(round(len(CONVERT(nvarchar(100),value))*1.5,0) as int))), 
CONVERT(nvarchar(100),max(cast(round(len(CONVERT(nvarchar(100),value_in_use))*1.5,0) as int)))
FROM sys.configurations 
WHERE value <> value_in_use
)temp