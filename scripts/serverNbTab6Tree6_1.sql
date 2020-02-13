IF EXISTS (SELECT SQLAgentMailEnabled FROM #SQLAgentMailEnabled) 
BEGIN 
	SELECT 'SQL Agent Mail Enabled' as Component,
	CASE WHEN Datos=1 
	THEN 'Enabled' 
	ELSE 'Disabled' 
	END AS SQLAgentMailEnabled 
	FROM #SQLAgentMailEnabled 
END 
ELSE 
BEGIN 
	SELECT 'SQL Agent Mail Enabled' as Component, 'Express Edition' AS SQLAgentMailEnabled 
END;