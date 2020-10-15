SELECT
ROW_NUMBER() OVER(ORDER BY Dbname ASC) AS [No],*
FROM
(
    SELECT * FROM #dbcc_log

	UNION

	SELECT
	CONVERT(nvarchar(100),max(cast(round(len(Dbname)*1.5,0) as int))),
	CONVERT(nvarchar(100),max(cast(round(len(LogSizeMB)*1.5,0) as int))),
	CONVERT(nvarchar(100),max(cast(round(len(LogSpaceUsed)*1.5,0) as int))),
	CONVERT(nvarchar(100),max(cast(round(len(Stat)*1.5,0) as int)))
	FROM
	#dbcc_log

)temp
