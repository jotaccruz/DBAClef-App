--use msdb;
--CREATE TABLE #job_status
--(
--[Job_id] uniqueidentifier,--0
--[Originating_server] nvarchar(250),--1
--[Name] sysname,--2
--[Enable] tinyint,--3
--[Description] nvarchar(1024),--4
--[Start_step_id] int,--5
--[Category] nvarchar(250),--6
--[Owner] nvarchar(250),--7
--[Notify_level_eventlog] int,--8
--[Notify_level_email] int,--9
--[Notify_level_netsend] int,--10
--[Notify_level_page] int,--11
--[Notify_email_operator] nvarchar(250),--12
--[Notify_netsend_operator] nvarchar(250),--13
--[Notify_page_operator] nvarchar(250),--14
--[Delete_level] int,--15
--[Date_created] datetime,--16
--[Date_modified] datetime,--17
--[Version_number] int,--18
--[Last_run_date] int,--19
--[Last_run_time] int,--20
--[Last_run_outcome] int,--21
--[Next_run_date] int,--22
--[Next_run_time] int,--23
--[Next_run_schedule_id] int,--24
--[Current_execution_status] int,--25
--[Current_execution_step] nvarchar(250),--26
--[Current_retry_attempt] int,--27
--[Has_step] int,--28
--[Has_schedule] int,--29
--[Has_target] int,--30
--[Type] int);--31
--EXEC master.dbo.sp_help_job_moldmydb;


SELECT ROW_NUMBER() OVER(ORDER BY (SELECT 100) ASC) AS [No],*
FROM
(
SELECT 
CONVERT(nvarchar(250),[Job_id]) AS Job_id,--0
[Originating_server],--1
[Name],--2
CASE WHEN [Enable]=1 THEN 'ON' ELSE 'OFF' END AS [Enable],--3
[Description],--4
[Start_step_id],--5
[Category],--6
[Owner],--7
[Notify_level_eventlog],--8
[Notify_level_email],--9
[Notify_level_netsend],--10
[Notify_level_page],--11
[Notify_email_operator],--12
[Notify_netsend_operator],--13
[Notify_page_operator],--14
[Delete_level],--15
convert(nvarchar(11), [Date_created]) [Date_created],--16
convert(nvarchar(11), [Date_modified]) [Date_modified],--17
[Version_number],--18
[Last_run_date],--19
[Last_run_time],--20
CASE [Last_run_outcome]
WHEN 0 THEN 'Fail'
WHEN 1 THEN 'Succeed'
WHEN 2 THEN 'Retry'
WHEN 3 THEN 'Cancel'
WHEN 4 THEN 'Progress'
ELSE 'Unknown'
END AS [Last_run_outcome],--21
convert(nvarchar(11), [Next_run_date]) [Next_run_date],--22
[Next_run_time],--23
[Next_run_schedule_id],--24
[Current_execution_status],--25
[Current_execution_step],--26
[Current_retry_attempt],--27
CASE [Has_step]
WHEN 0 THEN 'N'
ELSE CONVERT(nvarchar(5),[Has_step])
END AS [Has_step],--28
CASE [Has_schedule]
WHEN 0 THEN 'N'
ELSE CONVERT(nvarchar(5),[Has_schedule])
END AS [Has_schedule],--29
[Has_target],--30
[Type]--31
FROM #job_status

UNION

SELECT
CONVERT(nvarchar(100),max(cast(round(len([Job_id])*1.5,0) as int))),--0
CONVERT(nvarchar(100),max(cast(round(len([Originating_server])*1.5,0) as int))),--1
CONVERT(nvarchar(100),max(cast(round(len([Name])*1.5,0) as int))),--2
CONVERT(nvarchar(100),max(cast(round(len('OFF')*1.5,0) as int))),--3
CONVERT(nvarchar(100),max(cast(round(len([Description])*1.5,0) as int))),--4
CONVERT(nvarchar(100),max(cast(round(len([Start_step_id])*1.5,0) as int))),--5
CONVERT(nvarchar(100),max(cast(round(len([Category])*1.5,0) as int))),--6
CONVERT(nvarchar(100),max(cast(round(len([Owner])*1.5,0) as int))),--7
CONVERT(nvarchar(100),max(cast(round(len([Notify_level_eventlog])*1.5,0) as int))),--8
CONVERT(nvarchar(100),max(cast(round(len([Notify_level_email])*1.5,0) as int))),--9
CONVERT(nvarchar(100),max(cast(round(len([Notify_level_netsend])*1.5,0) as int))),--10
CONVERT(nvarchar(100),max(cast(round(len([Notify_level_page])*1.5,0) as int))),--11
CONVERT(nvarchar(100),max(cast(round(len([Notify_email_operator])*1.5,0) as int))),--12
CONVERT(nvarchar(100),max(cast(round(len([Notify_netsend_operator])*1.5,0) as int))),--13
CONVERT(nvarchar(100),max(cast(round(len([Notify_page_operator])*1.5,0) as int))),--14
CONVERT(nvarchar(100),max(cast(round(len([Delete_level])*1.5,0) as int))),--15
CONVERT(nvarchar(100),max(cast(round(len([Date_created])*1.5,0) as int))),--16
CONVERT(nvarchar(100),max(cast(round(len([Date_modified])*1.5,0) as int))),--17
CONVERT(nvarchar(100),max(cast(round(len([Version_number])*1.5,0) as int))),--18
CONVERT(nvarchar(100),max(cast(round(len([Last_run_date])*1.5,0) as int))),--19
CONVERT(nvarchar(100),max(cast(round(len([Last_run_time])*1.5,0) as int))),--20
CONVERT(nvarchar(100),max(cast(round(len('Progress')*1.5,0) as int))),--[Last_run_outcome],--21
CONVERT(nvarchar(100),max(cast(round(len([Next_run_date])*1.5,0) as int))),--22
CONVERT(nvarchar(100),max(cast(round(len([Next_run_time])*1.5,0) as int))),--23
CONVERT(nvarchar(100),max(cast(round(len([Next_run_schedule_id])*1.5,0) as int))),--24
CONVERT(nvarchar(100),max(cast(round(len([Current_execution_status])*1.5,0) as int))),--25
CONVERT(nvarchar(100),max(cast(round(len([Current_execution_step])*1.5,0) as int))),--26
CONVERT(nvarchar(100),max(cast(round(len([Current_retry_attempt])*1.5,0) as int))),--27
CONVERT(nvarchar(100),max(cast(round(len('YES')*1.5,0) as int))),--[Has_step],--28
CONVERT(nvarchar(100),max(cast(round(len('YES')*1.5,0) as int))),--[Has_schedule],--29
CONVERT(nvarchar(100),max(cast(round(len([Has_target])*1.5,0) as int))),--30
CONVERT(nvarchar(100),max(cast(round(len([Type])*1.5,0) as int)))--31
FROM #job_status
) temp
ORDER BY [NAME]