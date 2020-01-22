SELECT 
database_id ID,
a.name NAME,
ISNULL(CONVERT(VARCHAR(11),b.LastBackup),'Take Care') LASTBACKUP,
isnull(suser_sname(owner_sid),'~~UNKNOWN~~') OWNER,
convert(nvarchar(11), create_date) CREATION,
compatibility_level COMPATIBILITY,
state_desc STATUS,
recovery_model_desc RECOVERY,
page_verify_option_desc VERIFICATION,
log_reuse_wait_desc LRWAIT 
FROM 
master.sys.databases a LEFT JOIN 
(
SELECT 
DB.[name], 
BS.[type], 
MAX(BS.backup_finish_date) AS LastBackup 
FROM sys.databases AS DB 
LEFT JOIN 
msdb.dbo.backupset AS BS 
ON DB.[name] = BS.database_name 
WHERE BS.[type]='D' 
GROUP BY DB.[name], BS.[type]
) b 
ON a.name=b.name 
WHERE a.name NOT IN ('Tempdb','DBAdmin') 
ORDER BY a.name ASC, create_date ASC;