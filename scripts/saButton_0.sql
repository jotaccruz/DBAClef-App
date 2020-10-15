DECLARE @command nvarchar(250)

SELECT @command = 'IF ''?'' NOT IN(''master'', ''model'', ''msdb'', ''tempdb'') BEGIN USE [?] 
   exec sp_changedbowner ''sa''; END'

EXEC sp_MSforeachdb @command;