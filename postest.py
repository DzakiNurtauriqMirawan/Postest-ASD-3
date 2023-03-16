import os
os.system("cls")
from prettytable import PrettyTable


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
                
class LinkedList_pertama:
    def __init__(self):
        self.head = None
    
    def tambah_pertama(self, data):
        if self.head is None :
            self.head = Node(data)
        else : 
            nodebaru = Node(data)
            nodebaru.next = self.head
            self.head = nodebaru
        
    def index_list(self, index):
        current_node = self.head
        current_index = 0
        while current_node is not None:
            if current_index == index:
                return current_node
            current_node = current_node.next
            current_index += 1

    def hapus_pertama(self, position):
        if self.head is None:
            return
        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1
        if index < position:
            print("\nIndex is out of range.")
        elif index == 0:
            self.head = self.head.next
        else:
            previous.next = current.next

    def display_pertama(self):
        if self.head is None:
            print("Linked list kosong")
        else :
            table = PrettyTable()
            table.field_names = ["No","Judul Lagu"]
            current_node = self.head
            x1 = 1
            while current_node is not None:
                table.add_row([x1,current_node.data])
                x1 += 1
                current_node = current_node.next
            print(table)

class LinkedList_Kedua:
    def __init__(self):
        self.head = None
    
    def tambah_kedua(self, data):
        if self.head is None :
            self.head = Node(data)
        else : 
            nodebaru = Node(data)
            nodebaru.next = self.head
            self.head = nodebaru

    def display_kedua(self):
        if self.head is None:
            print("Linked list kosong")
        else :
            table = PrettyTable()
            table.field_names = ["No","Judul Lagu"]
            current_node = self.head
            x1 = 1
            while current_node is not None:
                table.add_row([x1,current_node.data])
                x1 += 1
                current_node = current_node.next
            print(table)

class LinkedList_ketiga:
    def __init__(self):
        self.head = None
    
    def tambah_ketiga(self, data):
        if self.head is None :
            self.head = Node(data)
        else : 
            nodebaru = Node(data)
            nodebaru.next = self.head
            self.head = nodebaru

    def display_ketiga(self):
        if self.head is None:
            print("Linked list kosong")
        else :
            table = PrettyTable()
            table.field_names = ["No","Judul Lagu"]
            current_node = self.head
            x1 = 1
            while current_node is not None:
                table.add_row([x1,current_node.data])
                x1 += 1
                current_node = current_node.next
            print(table)

list_tetap = LinkedList_pertama()
list_nambah = LinkedList_Kedua()
list_hapus = LinkedList_ketiga()

def tambah():
    inputA = input("ketik judul lagu : ")
    print(inputA)
    list_tetap.tambah_pertama(inputA)
    list_nambah.tambah_kedua(inputA)

def hapus():
    inputB = int(input("Pilih nomor yang ingin dihapus : "))
    x = list_tetap.index_list(inputB-1)
    list_hapus.tambah_ketiga(x.data)
    list_tetap.hapus_pertama(inputB-1)

while True:
        print("""
        ====================================
                    Selamat Datang
        ====================================
                1. Pilih Tambah Lagu
                2. Pilih Hapus Lagu
                3. Pilih Menampilkan Lagu
                4. Riwayat Lagu
                5. Keluar
        ====================================
        """)
        pilihan = str(input(("Masukkan Pilihan 1/2/3/4/5 : ")))
        if pilihan == "1":
            tambah()
        elif pilihan == "2":
            hapus()
        elif pilihan == "3":
            list_tetap.display_pertama()
        elif pilihan == "4":
            while True:
                print("""
                ====================================
                            Selamat Datang
                ====================================
                        1. Riwayat menambah lagu
                        2. Riwayat menghapus lagu
                        3. Keluar
                ====================================
                """)
                pilih = input("Pilih 1/2/3 : ")
                if pilih == "1":
                    print("Data Lagu : ")
                    list_nambah.display_kedua()
                elif pilih == "2":
                    print("Data Lagu : ")
                    list_hapus.display_ketiga()
                elif pilih == "3":
                    print("TERIMAKASIH ")
                    exit()
                else:
                    print("Pilihan Tidak Ada")
        elif pilihan == "5":
            print("TERIMAKASIH ")
            exit()
        else:
            print("Pilihan Tidak Ada")