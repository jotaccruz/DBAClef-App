SELECT srv_name as SERVER,
srv_instance as INSTANCE,
srv_ip1 as IP,
srv_ins_port as PORT,
'' as USER,
'' as PWD,
srv_os as OS
FROM lgm_servers 
ORDER BY srv_name;