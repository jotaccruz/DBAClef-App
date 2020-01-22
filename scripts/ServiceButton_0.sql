use msdb;
IF EXISTS (
	SELECT *
	FROM INFORMATION_SCHEMA.ROUTINES
	WHERE SPECIFIC_SCHEMA = N'dbo'
	AND SPECIFIC_NAME = N'get_servicenotification'
)
DROP PROCEDURE dbo.get_servicenotification;