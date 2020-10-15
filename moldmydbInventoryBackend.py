
#VARIABLES ZONE
    #cur=conn.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS book (id integer PRIMARY KEY,
    #title text, author text, year integer, isbn integer)")
    #conn.commit()
    #conn.close()





def search():
    conn=connect()
    cur=conn.cursor()
    cur.execute(sqlexec)
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
