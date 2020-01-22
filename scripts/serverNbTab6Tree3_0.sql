SELECT 
CASE WHEN CAST(value_in_use AS INT)=0 
THEN 'Disabled' 
ELSE 'Enabled' 
END AS DBMailEnabled 
FROM sys.configurations 
WHERE [name] ='Database Mail XPs';