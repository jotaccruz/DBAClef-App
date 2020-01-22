SELECT 
jo.name NAME,
isnull(suser_sname(jo.owner_sid),'~~UNKNOWN~~') OWNER,
CASE WHEN jo.enabled=1 
THEN 'ENABLE' 
ELSE 'DISABLE' 
END AS STATUS,
description DESCR 
FROM 
msdb.dbo.sysjobs jo 
CROSS APPLY 
msdb.dbo.sysjobschedules josc 
CROSS APPLY 
msdb.dbo.sysschedules sc 
WHERE jo.job_id=josc.job_id 
AND josc.schedule_id=sc.schedule_id 
AND (jo.name LIKE 'Service Restart Notification' OR sc.freq_type=64);