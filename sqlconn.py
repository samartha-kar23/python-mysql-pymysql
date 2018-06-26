import pymysql

conn = pymysql.connect(host='10.14.88.224', user='root', password='sensor_cloud', db='SENSORS')

a= conn.cursor()

sql = "select cast(Status as unsigned) as Status from SENSOR"

countrow = a.execute(sql)
conn.commit()
#print("Number of rows : ",countrow)
data = a.fetchmany()
print(type(data[0][0]))
