import wmi
from wmi import *

#import pprint

#Remote Host
#server = "SCAEDYAK02"
#username = 'ti\jcruz.admin'
#psw = 'Flaca060409@'
#namespace="WMI"
#dir1="\root\cimv2:Win32_Volume"
#dir2="winmgmts:{impersonationLevel=impersonate,(LockMemory, !IncreaseQuota)}"\
#+"!\\" + server + dir1

#Local Host
#conn = wmi.WMI("localhost")

#Remote Host
#conn = wmi.WMI(server,user=username,password=psw)

#for class_name in conn.classes:
#  if 'Win32_Service' in class_name:
#    print (class_name)

#print(wmi.WMI().Win32_Service.methods.keys())

#print(wmi.WMI().Win32_Service.properties.keys())

def diskinfo(selected_modes, server, wmiuser, wmipass):
    if (selected_modes == 1):
        conn = wmi.WMI(server)
    else:
        conn = wmi.WMI(server,user=wmiuser,password=wmipass)
    diskinfo = {}
    diskinfo={'No': '1'\
             ,'SystemName': '25'\
             ,'Label': '25'\
             ,'Capacity': '25'\
             ,'DriveLetter': '25'\
             ,'FileSystem': '25'\
             ,'BlockSize': '10'\
             ,'Name': '25'\
             ,'FreeSpace': '25'\
             ,'DriveType': '25'}
    disks = []
    disks.append(diskinfo)
    i=2
    for Volumes in conn.Win32_Volume():
        if not Volumes.Name.startswith("\\"):
            #print("SystemName:{0} Label:{1} Capacity:{2} DriveLetter:{3}"\
            #      "BlockSize:{4} Name:{5} FreeSpace:{6}"\
            #      .format(Volumes.SystemName,Volumes.Label,\
            #              int(int(Volumes.Capacity)/1024/1024/1024)\
            #              ,Volumes.DriveLetter,Volumes.BlockSize,Volumes.Name\
            #              ,Volumes.FreeSpace))
            diskinfo={'No': str(i)\
                      ,'SystemName': Volumes.SystemName\
                      ,'Label': Volumes.Label\
                      ,'Capacity': int(int(0 if Volumes.Capacity is None else Volumes.Capacity)/1024/1024/1024)\
                      ,'DriveLetter': Volumes.DriveLetter\
                      ,'FileSystem': Volumes.FileSystem\
                      ,'BlockSize': int(int(0 if Volumes.BlockSize is None else Volumes.BlockSize)/1024)\
                      ,'Name': Volumes.Name\
                      ,'FreeSpace': int(int(0 if Volumes.FreeSpace is None else Volumes.FreeSpace)/1024/1024/1024)\
                      ,'DriveType': Volumes.DriveType}
            disks.append(diskinfo)
            i=i+1
    return disks

def pageinfo(selected_modes, server, wmiuser, wmipass):
    if (selected_modes == 1):
        conn = wmi.WMI(server)
    else:
        conn = wmi.WMI(server,user=wmiuser,password=wmipass)
    pageinfo = {'No': "1"\
                ,'SystemName': "35"\
                ,'Automatic': "10"\
                ,'Caption': "35"\
                ,'Status': "10"\
                ,'CurrentUsage': "10"\
                ,'PeakUsage': "10"\
                ,'InitialSize': "10"\
                ,'MaximumSize': "10"}
    pages = []
    pages.append(pageinfo)
    i=2
    for Volumes3 in conn.win32_ComputerSystem():
        pageinfo = {'No': str(i)\
                    ,'SystemName': ""\
                    ,'Automatic': ""\
                    ,'Caption': ""\
                    ,'Status': ""\
                    ,'CurrentUsage': ""\
                    ,'PeakUsage': ""\
                    ,'InitialSize': ""\
                    ,'MaximumSize': ""}

        if hasattr(Volumes3,'AutomaticManagedPagefile'):
            pageinfo.update({'Automatic': Volumes3.AutomaticManagedPagefile})
        else:
            pageinfo.update({'Automatic': 'False'})

        if hasattr(Volumes3,'Caption'):
            pageinfo.update({'SystemName': Volumes3.Caption})
        else:
            pageinfo.update({'SystemName': 'N/A'})

        for Volumes in conn.win32_pagefileUsage():
            for Volumes2 in conn.Win32_PageFile():
                if (Volumes.Name.replace('\\','').lower()==Volumes2.Name.replace('\\','').lower()):
                    if hasattr(Volumes,'CurrentUsage'):
                        pageinfo.update({'CurrentUsage': Volumes.CurrentUsage})
                    else:
                        pageinfo.update({'CurrentUsage': 'N/A'})

                    if hasattr(Volumes,'PeakUsage'):
                        pageinfo.update({'PeakUsage': Volumes.PeakUsage})
                    else:
                        pageinfo.update({'PeakUsage': 'N/A'})

                    if hasattr(Volumes,'Caption'):
                        pageinfo.update({'Caption': Volumes2.Caption})
                    else:
                        pageinfo.update({'Caption': 'N/A'})

                    if hasattr(Volumes,'Status'):
                        pageinfo.update({'Status': Volumes2.Status})
                    else:
                        pageinfo.update({'Status': 'N/A'})

                    if hasattr(Volumes,'InitialSize'):
                        pageinfo.update({'InitialSize': Volumes2.InitialSize})
                    else:
                        pageinfo.update({'InitialSize': 'N/A'})

                    if hasattr(Volumes,'MaximumSize'):
                        pageinfo.update({'MaximumSize': Volumes2.MaximumSize})
                    else:
                        pageinfo.update({'MaximumSize': 'N/A'})
        i=i+1
        pages.append(pageinfo)
    return pages


def mssqlinfo(selected_modes, server, wmiuser, wmipass):
    if (selected_modes == 1):
        conn = wmi.WMI(server)
    else:
        conn = wmi.WMI(server,user=wmiuser,password=wmipass)
    mssqlinfo = {}
    mssqlinfo={'No': '1'\
              ,'SystemName': '25'\
              ,'DisplayName': '75'\
              ,'Description': '50'\
              ,'Started': '15'\
              ,'StartMode': '15'\
              ,'StartName': '25'\
              ,'State': '15'\
              ,'Status': '15'\
              ,'PathName': '25'}
    services = []
    services.append(mssqlinfo)
    i=2
    for Services in conn.Win32_Service():
        if Services.DisplayName.startswith("SQL"):
            #print("SystemName:{0} Label:{1} Capacity:{2} DriveLetter:{3}"\
            #      "BlockSize:{4} Name:{5} FreeSpace:{6}"\
            #      .format(Volumes.SystemName,Volumes.Label,\
            #              int(int(Volumes.Capacity)/1024/1024/1024)\
            #              ,Volumes.DriveLetter,Volumes.BlockSize,Volumes.Name\
            #              ,Volumes.FreeSpace))
            mssqlinfo={'No': str(i)\
                      ,'SystemName': Services.SystemName\
                      ,'DisplayName': Services.DisplayName\
                      ,'Description': Services.Description\
                      ,'Started': Services.Started\
                      ,'StartMode': Services.StartMode\
                      ,'StartName': Services.StartName\
                      ,'State': Services.State\
                      ,'Status': Services.Status\
                      ,'PathName': Services.PathName}
            services.append(mssqlinfo)
            i=i+1
    return services

#disks=diskinfo()
#pp = pprint.PrettyPrinter(indent=4)
#pp = pprint.PrettyPrinter(depth=6)
#pp.pprint (disks)

#pages=pageinfo()
#for row in pages:
#    print (row['Automatic'],row['SystemName'],row['Caption'],row['Status'],row['CurrentUsage'],row['PeakUsage'],row['InitialSize'],row['MaximumSize'])
