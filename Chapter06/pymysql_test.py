import pymysql

conn = pymysql.connect(host='localhost',
                       user='philip', passwd='75356072Philip&%#%^)&@',
                       db='mysql', charset='utf8' )
cur = conn.cursor()
cur.execute('USE scraping')
cur.execute('SELECT * FROM pages WHERE id=3')
print(cur.fetchone())
cur.close()
conn.close()

