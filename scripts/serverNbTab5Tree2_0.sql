CREATE TABLE #AlertInfo 
(
FailSafeOperator NVARCHAR(255),
NotificationMethod INT,
ForwardingServer NVARCHAR(255),
ForwardingSeverity INT,
PagerToTemplate NVARCHAR(255),
PagerCCTemplate NVARCHAR(255),
PagerSubjectTemplate NVARCHAR(255),
PagerSendSubjectOnly NVARCHAR(255),
ForwardAlways INT);

INSERT  INTO #AlertInfo EXEC [master].[dbo].[sp_MSgetalertinfo] 
@includeaddresses = 0;