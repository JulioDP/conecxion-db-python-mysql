
import pymysql


conn = pymysql.connect(host='localhost',user='root',passwd='admin', db='universidad')
cur = conn.cursor()
cur.execute("select * from alumnos WHERE nombre = 'julio' ")
alum = cur.fetchone()
print('id: ',alum[0])
print('Nombre: ',alum[1])
print('Apellido: ',alum[2])
cur.close()
conn.close()
