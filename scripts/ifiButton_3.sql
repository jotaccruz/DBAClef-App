CREATE TABLE #ifiTest (message nvarchar(150),flag int);
CREATE TABLE #times (startdate datetime,enddate datetime);
INSERT INTO #times (startdate) VALUES (getdate());
EXECUTE master.dbo.ifi_testing;
UPDATE #times SET enddate=getdate();

IF (SELECT DATEDIFF(SECOND,startdate,enddate) FROM #times) >50
BEGIN
	INSERT INTO #ifiTest
	SELECT 'IFI is not working as expected. secpol.msc',0
END
ELSE
BEGIN
	INSERT INTO #ifiTest
	SELECT 'IFI is already working',1
END

drop database [ifitesting];
