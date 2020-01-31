EXEC sp_configure 'show advanced options',1;
RECONFIGURE WITH OVERRIDE;
IF EXISTS (SELECT * FROM sys.configurations WHERE name LIKE 'remote admin connections')
BEGIN
EXEC sp_configure 'remote admin connections', 1;
END;
IF EXISTS (SELECT * FROM sys.configurations WHERE name LIKE 'backup checksum default')
BEGIN
EXEC sp_configure 'backup checksum default', 1;
END
EXEC sp_configure 'show advanced options',0;
RECONFIGURE WITH OVERRIDE;