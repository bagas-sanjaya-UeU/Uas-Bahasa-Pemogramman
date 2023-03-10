import tkinter as tk
import mysql.connector

db = mysql.connector.connect(user='root', password='', host='localhost', database='produk_db')
cursor = db.cursor()

root = tk.Tk()
root.title("Aplikasi data produk dengan Tkinter dan MySQL")
root.geometry("600x400")

label_name = tk.Label(root, text="Nama_produk")
entry_name = tk.Entry(root)

label_kategori_produk = tk.Label(root, text="kategori_produk")
entry_kategori_produk = tk.Entry(root)

label_harga = tk.Label(root, text="harga")
entry_harga = tk.Entry(root)

def create_data():
    name = entry_name.get()
    kategori_produk = entry_kategori_produk.get()
    harga = int(entry_harga.get())

    cursor.execute("INSERT INTO produk (nama_barang, kategori_barang, harga_barang) VALUES (%s, %s, %s)", (name, kategori_produk, harga))
    db.commit()

def read_data():
    cursor.execute("SELECT * FROM produk")
    result = cursor.fetchall()
    for x in result:
        print(x)
    

def update_data():
    name = entry_name.get()
    kategori_produk = entry_kategori_produk.get()
    harga = int(entry_harga.get())

    cursor.execute("UPDATE produk SET harga_produk = %s WHERE nama_produk = %s", (harga, name))
    db.commit()

def delete_data():
    name = entry_name.get()
    cursor.execute("DELETE FROM produk WHERE nama_produk = %s", (name,))
    db.commit()

button_create = tk.Button(root, text="Tambah", command=create_data)
button_read = tk.Button(root, text="Baca", command=read_data)
button_update = tk.Button(root, text="Ubah", command=update_data)
button_delete = tk.Button(root, text="Hapus", command=delete_data)

label_name.pack()
entry_name.pack()

label_kategori_produk.pack()
entry_kategori_produk.pack()

label_harga.pack()
entry_harga.pack()

button_create.pack()
button_read.pack()
button_update.pack()
button_delete.pack()

root.mainloop()

cursor.close()
db.close()
