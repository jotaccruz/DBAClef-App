--DROP TABLE #StandardsLogins
CREATE TABLE #StandardsLogins
(NAME nvarchar(400));

INSERT INTO #StandardsLogins (NAME)
VALUES ('TI\GR_DBAAdmin')
INSERT INTO #StandardsLogins (NAME)
VALUES ('TI\solarwinds.sam')
INSERT INTO #StandardsLogins (NAME)
VALUES ('TI\dba.backup');