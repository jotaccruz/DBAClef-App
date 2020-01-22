-- =============================================
-- Create basic stored procedure template
-- =============================================

-- Drop stored procedure if it already exists
USE master;

IF EXISTS (
  SELECT * 
    FROM INFORMATION_SCHEMA.ROUTINES 
   WHERE SPECIFIC_SCHEMA = N'dbo'
     AND SPECIFIC_NAME = N'get_maxmemreco' 
)
   DROP PROCEDURE dbo.get_maxmemreco
GO

CREATE PROCEDURE dbo.get_maxmemreco
	@p1 int = 0, 
	@p2 int = 0
AS
	-- SET proper server memory (below calculations are for one instance only)
	DECLARE @maxservermem bigint, @minservermem bigint, @systemmem bigint, @mwthreads_count int, @sqlmajorver int, @numa int, @numa_nodes_afinned tinyint, @arch NVARCHAR(10), @sqlcmd NVARCHAR(255)
	-- Change below to 1 to set a max server memory config that is aligned with current affinied NUMA nodes.
	DECLARE @numa_affined_config bit = 0

	SELECT @sqlmajorver = CONVERT(int, (@@microsoftversion / 0x1000000) & 0xff);
	SELECT @arch = CASE WHEN @@VERSION LIKE '%<X64>%' THEN 64 WHEN @@VERSION LIKE '%<IA64>%' THEN 128 ELSE 32 END FROM sys.dm_os_windows_info WITH (NOLOCK);
	SELECT @systemmem = total_physical_memory_kb/1024 FROM sys.dm_os_sys_memory;
	SELECT @numa = COUNT(DISTINCT parent_node_id) FROM sys.dm_os_schedulers WHERE scheduler_id < 255 AND parent_node_id < 64;
	SELECT @numa_nodes_afinned = COUNT (DISTINCT parent_node_id) FROM sys.dm_os_schedulers WHERE scheduler_id < 255 AND parent_node_id < 64 AND is_online = 1;
	SELECT @minservermem = CONVERT(int, [value]) FROM sys.configurations WITH (NOLOCK) WHERE [Name] = 'min server memory (MB)';
	SELECT @maxservermem = CONVERT(int, [value]) FROM sys.configurations WITH (NOLOCK) WHERE [Name] = 'max server memory (MB)';
	SELECT @mwthreads_count = max_workers_count FROM sys.dm_os_sys_info;

	IF (@maxservermem = 2147483647 OR @maxservermem > @systemmem) AND @numa_affined_config = 0
	BEGIN
		SELECT CONVERT(NVARCHAR(20), 
			CASE WHEN @systemmem <= 2048 THEN @systemmem-512-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END)
				WHEN @systemmem BETWEEN 2049 AND 4096 THEN @systemmem-819-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END)
				WHEN @systemmem BETWEEN 4097 AND 8192 THEN @systemmem-1228-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END)
				WHEN @systemmem BETWEEN 8193 AND 12288 THEN @systemmem-2048-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END)
				WHEN @systemmem BETWEEN 12289 AND 24576 THEN @systemmem-2560-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END)
				WHEN @systemmem BETWEEN 24577 AND 32768 THEN @systemmem-3072-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END)
				WHEN @systemmem > 32768 AND SERVERPROPERTY('EditionID') IN (284895786, 1293598313) THEN CAST(0.5 * (((@systemmem-4096-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END)) + 65536) - ABS((@systemmem-4096-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END)) - 65536)) AS int) -- Find min of max mem for machine or max mem for Web and Business Intelligence SKU
				WHEN @systemmem > 32768 AND SERVERPROPERTY('EditionID') = -1534726760 THEN CAST(0.5 * (((@systemmem-4096-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END)) + 131072) - ABS((@systemmem-4096-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END)) - 131072)) AS int) -- Find min of max mem for machine or max mem for Standard SKU
				WHEN @systemmem > 32768 AND SERVERPROPERTY('EngineEdition') IN (3,8) THEN @systemmem-4096-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END) -- Enterprise Edition or Managed Instance
			END) AS MaxMemoryRecommended;
	END
	ELSE IF (@maxservermem = 2147483647 OR @maxservermem > @systemmem) AND @numa_affined_config = 1
	BEGIN
		SELECT CONVERT(NVARCHAR(20), 
			CASE WHEN @systemmem <= 2048 THEN ((@systemmem-512-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END))/@numa) * @numa_nodes_afinned
				WHEN @systemmem BETWEEN 2049 AND 4096 THEN ((@systemmem-819-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END))/@numa) * @numa_nodes_afinned
				WHEN @systemmem BETWEEN 4097 AND 8192 THEN ((@systemmem-1228-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END))/@numa) * @numa_nodes_afinned
				WHEN @systemmem BETWEEN 8193 AND 12288 THEN ((@systemmem-2048-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END))/@numa) * @numa_nodes_afinned
				WHEN @systemmem BETWEEN 12289 AND 24576 THEN ((@systemmem-2560-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END))/@numa) * @numa_nodes_afinned
				WHEN @systemmem BETWEEN 24577 AND 32768 THEN ((@systemmem-3072-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END))/@numa) * @numa_nodes_afinned
				WHEN @systemmem > 32768 AND SERVERPROPERTY('EditionID') IN (284895786, 1293598313) THEN ((CAST(0.5 * (((@systemmem-4096-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END)) + 65536) - ABS((@systemmem-4096-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END)) - 65536)) AS int))/@numa) * @numa_nodes_afinned -- Find min of max mem for machine or max mem for Web and Business Intelligence SKU
				WHEN @systemmem > 32768 AND SERVERPROPERTY('EditionID') = -1534726760 THEN ((CAST(0.5 * (((@systemmem-4096-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END)) + 131072) - ABS((@systemmem-4096-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END)) - 131072)) AS int))/@numa) * @numa_nodes_afinned -- Find min of max mem for machine or max mem for Standard SKU
				WHEN @systemmem > 32768 AND SERVERPROPERTY('EngineEdition') IN (3,8) THEN ((@systemmem-4096-(@mwthreads_count*(CASE WHEN @arch = 64 THEN 2 WHEN @arch = 128 THEN 4 WHEN @arch = 32 THEN 0.5 END)- CASE WHEN @arch = 32 THEN 256 ELSE 0 END))/@numa) * @numa_nodes_afinned -- Enterprise Edition or Managed Instance
			END) AS MaxMemoryRecommended;
	END;
GO

-- =============================================
-- Example to execute the stored procedure
-- =============================================
--EXECUTE dbo.get_maxmemreco 1, 2
--GO
