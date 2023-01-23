import mysql.connector

# membuat koneksi ke database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="produk_db"
)

# membuat cursor
cursor = db.cursor()

#query SQL
sql = "SELECT * FROM produk"

# eksekusi query
cursor.execute(sql)

# mengambil semua data
data = cursor.fetchall()

# menampilkan data
for x in data:
    print(x)

# menutup koneksi
db.close()

