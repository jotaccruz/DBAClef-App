IF EXISTS (SELECT * FROM sys.dm_os_performance_counters)
SELECT
TOP 1 CAST(SERVERPROPERTY('ProductVersion') AS NVARCHAR(100)) as ProductVersion,
CAST(SERVERPROPERTY('ProductLevel') AS NVARCHAR(100)) as PatchLevel,
CAST(SERVERPROPERTY('Edition') AS VARCHAR(100)) as Edition,
CASE WHEN (CAST(SERVERPROPERTY('IsClustered') AS VARCHAR(100))=0) THEN 'NOT' ELSE 'YES' END as IsClustered,
CASE WHEN (CAST(COALESCE(SERVERPROPERTY('IsHadrEnabled'),0) AS VARCHAR(100))=1) THEN 'YES' ELSE 'NOT' END as AlwaysOnEnabled,
'' AS Warning
FROM sys.dm_os_performance_counters;
ELSE
SELECT
TOP 1 CAST(SERVERPROPERTY('ProductVersion') AS NVARCHAR(100)) as ProductVersion,
CAST(SERVERPROPERTY('ProductLevel') AS NVARCHAR(100)) as PatchLevel,
CAST(SERVERPROPERTY('Edition') AS VARCHAR(100)) as Edition,
CASE WHEN (CAST(SERVERPROPERTY('IsClustered') AS VARCHAR(100))=0) THEN 'NOT' ELSE 'YES' END as IsClustered,
CASE WHEN (CAST(COALESCE(SERVERPROPERTY('IsHadrEnabled'),0) AS VARCHAR(100))=1) THEN 'YES' ELSE 'NOT' END as AlwaysOnEnabled,
'WARNING - No records found in sys.dm_os_performance_counters' AS Warning;