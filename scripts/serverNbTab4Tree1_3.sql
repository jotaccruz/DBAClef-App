SELECT 
Type, 
Location, 
Restart, 
CASE WHEN (ISNULL(Restart,0)=1)
THEN 'Required' 
ELSE 'No' 
END AS Restart 
FROM #DPath;