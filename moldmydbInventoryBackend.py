import moldmydbSource
from moldmydbSource import *

#VARIABLES ZONE
    #cur=conn.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS book (id integer PRIMARY KEY,
    #title text, author text, year integer, isbn integer)")
    #conn.commit()
    #conn.close()

mysqlserver='172.25.20.17'#ip.get()
mysqlusername='ISJCruz'#user.get()
mysqlpsw='T3lu52018!'#pas.get()

def view():
    sqlexec="SELECT \
    TRUNCATE((@row_number:=@row_number+1),1)as No,\
    srv_name,\
    srv_instance,\
    srv_ins_port,\
    srv_ip1,\
    srv_ip2,\
    srv_user,\
    srv_pwd,\
    srv_directory,\
    srv_os,\
    srv_frecuency,\
    srv_bk_location,\
    srv_type,\
    srv_location,\
    srv_domain,\
    CASE WHEN srv_active = 0 THEN 'OFF'\
    ELSE 'ON' END AS srv_active_letter,\
    srv_created_dt,\
    srv_updated_dt,\
    srv_active\
    FROM lgm_servers,\
    (SELECT @row_number:=0) AS t\
    ORDER BY srv_name;"
    rows=dbservers(sqlexec,mysqlserver,mysqlusername,mysqlpsw)
    #print (rows)
    return rows

def search(title="",author="",year="",isbn=""):
    conn=connect()
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR \
                isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete (id):
    conn=connect()
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update (id, title,author,year,isbn):
    conn=connect()
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?" \
                ,(title,author,year,isbn,id))
    conn.commit()
    conn.close()

#connect()
#insert("Letter","Jhon",1938,12345)
#print(view())
#print("---")
#print(search("Letter"))
