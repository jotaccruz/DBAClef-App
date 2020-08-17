SELECT ROW_NUMBER() OVER(ORDER BY [ServerName\InstanceName] ASC) AS [No],*
FROM
(SELECT
CONVERT(nvarchar(250),@@servername) AS 'ServerName\InstanceName',
CONVERT(nvarchar(250),SERVERPROPERTY('servername')) AS 'ServerName',
CONVERT(nvarchar(250),SERVERPROPERTY('machinename')) AS 'Windows_Name',
CONVERT(nvarchar(250),SERVERPROPERTY('ComputerNamePhysicalNetBIOS')) AS 'NetBIOS_Name',
CONVERT(nvarchar(250),ISNULL(SERVERPROPERTY('instanceName'),'DEFAULT')) AS 'InstanceName',
CONVERT(nvarchar(250),SERVERPROPERTY('IsClustered')) AS 'IsClustered'
UNION
SELECT
CONVERT(nvarchar(250),len(CONVERT(nvarchar(250),@@servername))) AS 'ServerName\InstanceName',
CONVERT(nvarchar(250),len(CONVERT(nvarchar(250),SERVERPROPERTY('servername')))) AS 'ServerName',
CONVERT(nvarchar(250),len(CONVERT(nvarchar(250),SERVERPROPERTY('machinename')))) AS 'Windows_Name',
CONVERT(nvarchar(250),len(CONVERT(nvarchar(250),SERVERPROPERTY('ComputerNamePhysicalNetBIOS')))) AS 'NetBIOS_Name',
CONVERT(nvarchar(250),len(CONVERT(nvarchar(250),ISNULL(SERVERPROPERTY('instanceName'),'DEFAULT')))) AS 'InstanceName',
CONVERT(nvarchar(250),len(CONVERT(nvarchar(250),SERVERPROPERTY('IsClustered')))) AS 'IsClustered') temp
