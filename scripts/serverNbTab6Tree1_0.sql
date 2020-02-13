SELECT 'Agent XPs' as Component,
CASE WHEN CAST(value_in_use AS INT)=0 
THEN 'Disabled' 
ELSE 'Enabled' 
END AS SQLAgentEnabled
FROM sys.configurations 
WHERE [name] ='Agent XPs';