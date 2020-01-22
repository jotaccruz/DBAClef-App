IF EXISTS (SELECT SQLAgentMailProfile FROM #SQLAgentMailProfile) 
BEGIN 
	SELECT ISNULL(dat,'Missing') [profile] 
	FROM #SQLAgentMailProfile 
END 
ELSE 
BEGIN 
	SELECT 'Express Edition' 
	SQLAgentMailProfileEnabled 
END;