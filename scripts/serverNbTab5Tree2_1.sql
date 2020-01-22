SELECT 
ISNULL(FailSafeOperator,CONVERT(NVARCHAR(250),
'No Fail safe Operator')) AS FailSafeOperator, 
CASE WHEN ISNULL(FailSafeOperator,CONVERT(NVARCHAR(250),'No Fail safe Operator'))='No Fail safe Operator' 
THEN '1' 
ELSE '0' 
END as Semaphore 
FROM #AlertInfo;