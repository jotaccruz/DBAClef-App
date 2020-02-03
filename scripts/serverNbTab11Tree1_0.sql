CREATE TABLE #tracert (id int,property int,value nvarchar(500))
INSERT INTO #tracert
SELECT traceid,property,CONVERT(nvarchar(500),value) FROM fn_trace_getinfo(default);