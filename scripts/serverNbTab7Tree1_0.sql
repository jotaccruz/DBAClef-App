SELECT 
name NAME, 
description AS DESCR, 
CONVERT(nvarchar(100),value) AS VALUE, 
CONVERT(nvarchar(100),value_in_use) AS VALUEINUSE 
FROM sys.configurations 
WHERE value <> value_in_use;