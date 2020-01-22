CREATE PROCEDURE dbo.get_vlf
	@p1 int = 0,
	@p2 int = 0
AS
    BEGIN
    declare @query varchar(100)
    declare @dbname sysname
    declare @vlfs int
    declare @databases table (dbname sysname)
    insert into @databases
    select name from sys.databases where state = 0
    declare @MajorVersion tinyint
    set @MajorVersion = LEFT(CAST(SERVERPROPERTY('ProductVersion') AS nvarchar(max)),CHARINDEX('.',CAST(SERVERPROPERTY('ProductVersion') AS nvarchar(max)))-1)
    if @MajorVersion < 11
    begin
		declare @dbccloginfo table
		(
		fileid smallint,
		file_size bigint,
		start_offset bigint,
		fseqno int,
		[status] tinyint,
		parity tinyint,
		create_lsn numeric(25,0)
		)
		while exists(select top 1 dbname from @databases)
			begin
			set @dbname = (select top 1 dbname from @databases)
			set @query = 'dbcc loginfo (' + '''' + @dbname + ''')'
			insert into @dbccloginfo
			exec (@query)
			set @vlfs = @@rowcount
			insert #vlfcounts
			values(@dbname, @vlfs)
			delete from @databases where dbname = @dbname
			end
    end
    else
    begin
		declare @dbccloginfo2012 table
		(
		RecoveryUnitId int,
		fileid smallint,
		file_size bigint,
		start_offset bigint,
		fseqno int,
		[status] tinyint,
		parity tinyint,
		create_lsn numeric(25,0)
		)
		while exists(select top 1 dbname from @databases)
			begin
			set @dbname = (select top 1 dbname from @databases)
			set @query = 'dbcc loginfo (' + '''' + @dbname + ''')'
			insert into @dbccloginfo2012
			exec (@query)
			set @vlfs = @@rowcount
			insert #vlfcounts
			values(@dbname, @vlfs)
			delete from @databases where dbname = @dbname
			end
    end
    select dbname, vlfcount
    from #vlfcounts
    order by dbname
END;