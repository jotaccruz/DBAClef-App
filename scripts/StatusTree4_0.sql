DECLARE @ProductVersion VARCHAR(100)
SELECT @ProductVersion = CAST(SERVERPROPERTY('productversion') AS varchar(100))
SELECT @ProductVersion AS VERSION;
--DECLARE @Major VARCHAR(100)
--DECLARE @Minor VARCHAR(100)
--SELECT @Minor = PARSENAME(@ProductVersion, 1)
--SELECT @Major = PARSENAME(@ProductVersion, 4)
--SELECT
--CASE WHEN @Major IS NULL THEN @ProductVersion ELSE LEFT(@ProductVersion,LEN(@ProductVersion)-CHARINDEX('.',REVERSE(@ProductVersion))) END AS VERSION;
