SELECT
ROW_NUMBER() OVER(ORDER BY name ASC, CREATION ASC) AS [No],*
FROM
(SELECT
database_id ID,
a.name NAME,
ltrim(rtrim(db_size)) SIZE,
ISNULL(CONVERT(VARCHAR(11),b.LastBackup),'Take Care') LASTBACKUP,
isnull(suser_sname(owner_sid),'~~UNKNOWN~~') OWNER,
convert(nvarchar(11), create_date) CREATION,
a.compatibility_level COMPATIBILITY,
state_desc STATUS,
recovery_model_desc RECOVERY,
page_verify_option_desc VERIFICATION,
log_reuse_wait_desc LRWAIT
FROM
master.sys.databases a
INNER JOIN #databases t ON a.database_id=t.dbid
LEFT JOIN
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
UNION
SELECT
CONVERT(nvarchar(100),max(cast(round(len(database_id)*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(a.name)*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(ltrim(rtrim(db_size)))*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(ISNULL(CONVERT(VARCHAR(11),b.LastBackup),'Take Care'))*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(isnull(suser_sname(owner_sid),'~~UNKNOWN~~'))*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(convert(nvarchar(11), create_date))*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(a.compatibility_level)*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(state_desc)*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(recovery_model_desc)*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(page_verify_option_desc)*1.5,0) as int))),
CONVERT(nvarchar(100),max(cast(round(len(log_reuse_wait_desc)*1.5,0) as int)))
FROM
master.sys.databases a
INNER JOIN #databases t ON a.database_id=t.dbid
LEFT JOIN
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

)temp
