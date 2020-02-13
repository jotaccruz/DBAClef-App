CREATE TABLE #times (startdate datetime,enddate datetime, dif int, message nvarchar(150),flag int);
INSERT INTO #times (startdate) VALUES (getdate());
EXECUTE master.dbo.ifi_testing;
UPDATE #times SET enddate=getdate();
UPDATE #times SET dif=DATEDIFF(SECOND,startdate,enddate) FROM #times

IF ((SELECT top 1 dif FROM #times) >30)
BEGIN
	UPDATE #times
	SET message='IFI is not working as expected. secpol.msc',flag=0
END
ELSE
BEGIN
	UPDATE #times
	SET message='IFI is already working',flag=1
END