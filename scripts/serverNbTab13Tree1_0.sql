USE master;
IF EXISTS (
SELECT *
FROM INFORMATION_SCHEMA.ROUTINES
WHERE SPECIFIC_SCHEMA = N'dbo'
AND SPECIFIC_NAME = N'sp_get_composite_job_info_moldmydb'
)
DROP PROCEDURE dbo.sp_get_composite_job_info_moldmydb;
IF EXISTS (
SELECT *
FROM INFORMATION_SCHEMA.ROUTINES
WHERE SPECIFIC_SCHEMA = N'dbo'
AND SPECIFIC_NAME = N'sp_help_job_moldmydb'
)
DROP PROCEDURE dbo.sp_help_job_moldmydb;