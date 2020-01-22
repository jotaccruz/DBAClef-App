DECLARE @StringToExecute NVARCHAR(4000);
CREATE TABLE #test (cpu_count int,physical_memory_GB int,sql_memory_GB numeric(10,2));
IF EXISTS ( SELECT  *
FROM sys.all_objects o
INNER JOIN sys.all_columns c ON o.object_id = c.object_id
WHERE   o.name = 'dm_os_sys_info'
AND c.name = 'physical_memory_kb' )
BEGIN
SET @StringToExecute = '
SELECT
cpu_count,
CAST(ROUND((physical_memory_kb / 1024.0 / 1024), 1) AS INT) as physical_memory_GB,
CAST((CONVERT(int,value_in_use)/1024.0) as numeric(10,2)) as SQLMEM
FROM sys.dm_os_sys_info
CROSS APPLY sys.configurations
WHERE [name] =''max server memory (MB)''';
END
ELSE IF EXISTS ( SELECT  *
FROM    sys.all_objects o
INNER JOIN sys.all_columns c ON o.object_id = c.object_id
WHERE o.name = 'dm_os_sys_info'
AND c.name = 'physical_memory_in_bytes' )
BEGIN
SET @StringToExecute = '
SELECT
cpu_count,
CAST(ROUND((physical_memory_in_bytes / 1024.0 / 1024.0 / 1024.0 ), 1) AS INT) as physical_memory_GB,
CAST((CONVERT(int,value_in_use)/1024.0) as numeric(10,2)) as SQLMEM
FROM sys.dm_os_sys_info
CROSS APPLY sys.configurations
WHERE [name] =''max server memory (MB)''';
END
INSERT INTO #test
EXECUTE(@StringToExecute);