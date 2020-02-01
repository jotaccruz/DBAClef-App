CREATE PROCEDURE dbo.ifi_testing
	@p1 int = 0, 
	@p2 int = 0
AS
BEGIN
	ALTER DATABASE [ifitesting] MODIFY FILE ( NAME = N'ifitesting', SIZE = 5242880KB );
END
---- =============================================
---- Example to execute the stored procedure
---- =============================================
--EXECUTE dbo.ifi_testing 1, 2;
