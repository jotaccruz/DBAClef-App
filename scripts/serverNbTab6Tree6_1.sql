IF EXISTS (SELECT SQLAgentMailEnabled FROM #SQLAgentMailEnabled) 
BEGIN 
	SELECT 
	CASE WHEN Datos=1 
	THEN 'Enabled' 
	ELSE 'Disabled' 
	END AS SQLAgentMailEnabled 
	FROM #SQLAgentMailEnabled 
END 
ELSE 
BEGIN 
	SELECT 'Express Edition' AS SQLAgentMailEnabled 
END;