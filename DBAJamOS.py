import wmi
import pprint

#Remote Host
server = "SCAEDYAK02"
username = 'ti\jcruz.admin'
psw = '060409@Flaca'
namespace="WMI"
dir1="\root\cimv2:Win32_Volume"
dir2="winmgmts:{impersonationLevel=impersonate,(LockMemory, !IncreaseQuota)}"\
+"!\\" + server + dir1

#Local Host
#conn = wmi.WMI("localhost")

#for class_name in conn.classes:
#  if 'Volume' in class_name:
#    print (class_name)
    
#print(wmi.WMI().Win32_Volume.methods.keys())

#print(wmi.WMI().win32_ComputerSystem.properties.keys())
    
def diskinfo(server="SCAEDYAK02"):
    conn = wmi.WMI(server,user=username,password=psw)
    diskinfo = {}
    disks = []
    for Volumes in conn.Win32_Volume():
        if not Volumes.Name.startswith("\\"):
            #print("SystemName:{0} Label:{1} Capacity:{2} DriveLetter:{3}"\
            #      "BlockSize:{4} Name:{5} FreeSpace:{6}"\
            #      .format(Volumes.SystemName,Volumes.Label,\
            #              int(int(Volumes.Capacity)/1024/1024/1024)\
            #              ,Volumes.DriveLetter,Volumes.BlockSize,Volumes.Name\
            #              ,Volumes.FreeSpace))
            diskinfo={'SystemName': Volumes.SystemName\
                      ,'Label': Volumes.Label\
                      ,'Capacity': int(int(Volumes.Capacity)/1024/1024/1024)\
                      ,'DriveLetter': Volumes.DriveLetter\
                      ,'FileSystem': Volumes.FileSystem\
                      ,'BlockSize': int(int(Volumes.BlockSize)/1024)\
                      ,'Name': Volumes.Name\
                      ,'FreeSpace': int(int(Volumes.FreeSpace)/1024/1024/1024)\
                      ,'DriveType': Volumes.DriveType}
            disks.append(diskinfo)
    return disks

def pageinfo(server="SCAEDYAK02"):
    conn = wmi.WMI(server,user=username,password=psw)
    pageinfo = {'SystemName': ""\
                ,'Automatic': ""\
                ,'Caption': ""\
                ,'Status': ""\
                ,'CurrentUsage': ""\
                ,'PeakUsage': ""\
                ,'InitialSize': ""\
                ,'MaximunSize': ""}
    pages = []
    for Volumes3 in conn.win32_ComputerSystem():
        pageinfo.update({'Automatic': Volumes3.AutomaticManagedPagefile\
                         ,'SystemName': Volumes3.Caption})
    for Volumes in conn.win32_pagefileUsage():
        for Volumes2 in conn.Win32_PageFile():
            if (Volumes.Name==Volumes2.Name):
                pageinfo.update({'CurrentUsage': Volumes.CurrentUsage\
                                 ,'PeakUsage': Volumes.PeakUsage\
                                 ,'Caption': Volumes2.Caption\
                                 ,'Status': Volumes2.Status\
                                 ,'InitialSize': Volumes2.InitialSize\
                                 ,'MaximunSize': Volumes2.MaximunSize})
        pages.append(pageinfo)
    return pages

#disks=diskinfo()
#pp = pprint.PrettyPrinter(indent=4)
#pp = pprint.PrettyPrinter(depth=6)
#pp.pprint (disks)
    
#pages=pageinfo()
#for row in pages:
#    print (row['Automatic'],row['SystemName'],row['Caption'],row['Status'],row['CurrentUsage'],row['PeakUsage'],row['InitialSize'],row['MaximunSize'])