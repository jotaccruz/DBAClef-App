SELECT ROW_NUMBER() OVER(ORDER BY [Type] ASC) AS [No],*
FROM
(
SELECT 
Type, 
Location, 
ISNULL(Restart,0) as [First], 
CASE WHEN (ISNULL(Restart,0)=1)
THEN 'Required' 
ELSE 'No' 
END AS [Second]
FROM #DPath
UNION
SELECT
CONVERT(nvarchar(100),max(cast(round(len(Type)*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(Location)*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(0)*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len('Required')*1.5,0) as int)))
FROM #DPath) temp