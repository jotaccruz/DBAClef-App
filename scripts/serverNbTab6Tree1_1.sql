SELECT 
ROW_NUMBER() OVER(ORDER BY [Val] ASC) AS [No],*
FROM
(
SELECT 
Component,
Val 
FROM #DBmail
union
SELECT
CONVERT(nvarchar(100),max(cast(round(len(Component)*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(Val)*1.5,0) as int)))
FROM #DBmail)temp