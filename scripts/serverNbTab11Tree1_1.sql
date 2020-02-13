SELECT id,
CASE (property)
WHEN 1 THEN 'Trace options'
WHEN 2 THEN 'File name'
WHEN 3 THEN 'Max size'
WHEN 4 THEN 'Stop time'
WHEN 5 THEN 'Current status'
END Property,value FROM #tracert