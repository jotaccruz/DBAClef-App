IF EXISTS (SELECT SQLAgentMailProfile FROM #SQLAgentMailProfile) 
BEGIN 
	SELECT 'SQL Agent Mail Profile' Component , ISNULL(dat,'Missing') [profile] 
	FROM #SQLAgentMailProfile 
END 
ELSE 
BEGIN 
	SELECT 'SQL Agent Mail Profile' Component, 'Express Edition' [profile]
END;