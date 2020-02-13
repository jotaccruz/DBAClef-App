SELECT 
name NAME,
description AS DESCR, 
CONVERT(nvarchar(100),value) AS VALUE, 
CONVERT(nvarchar(100),value_in_use) AS VALUEINUSE 
FROM sys.configurations 
WHERE value <> value_in_use
UNION
SELECT 
CONVERT(nvarchar(100),max(len(name))), 
CONVERT(nvarchar(100),max(len(description))), 
CONVERT(nvarchar(100),max(len(CONVERT(nvarchar(100),value)))), 
CONVERT(nvarchar(100),max(len(CONVERT(nvarchar(100),value_in_use))))
FROM sys.configurations 
WHERE value <> value_in_use
ORDER BY NAME DESC