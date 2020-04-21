SELECT 
[Job_id],--0
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
[Date_created],--16
[Date_modified],--17
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
[Next_run_date],--22
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
ORDER BY [Enable];