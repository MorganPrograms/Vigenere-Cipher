#Christopher Morgan
#620107769
#Vigenère Cipher

import tkinter as tk
from tkinter import ttk

table = [chr(i) for i in range (0,1000)]

def generateKey(string, key): 
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)])
  key = ''.join(map(str, key))
  return(key) 
  
def encryption():
  string = Plain1Entry.get()
  key = Key1Entry.get()
  key = generateKey(string,key)
  ciphertext = [] 
  for i in range(len(string)):
    x = (table.index(string[i]) +table.index(key[i])) % 1000
    x+=1
    ciphertext.append(table[x])
  string = ''.join(map(str, ciphertext))
  T = tk.Text(tab1, height = 5, width = 15)
  T.insert(1.0,string)
  T.grid(row=2, column=1, padx=15, pady=15)

def decryption():
  string = Cipher2Entry.get()
  key = Key2Entry.get()
  key = generateKey(string,key)
  plaintext = [] 
  for i in range(len(string)): 
    x = (table.index(string[i]) - table.index(key[i]) +1000 ) % 1000
    x -= 1
    plaintext.append(table[x])
  string = ''.join(map(str, plaintext))
  T = tk.Text(tab2, height = 5, width = 15)
  T.insert(1.0,string)
  T.grid(row=2, column=1, padx=15, pady=15)

def encryption2():
  string = Plain1Entry.get()
  key = Key1Entry.get()
  key = generateKey(string,key)
  ciphertext= [] 
  for i in range(len(string)): 
    x = (ord(string[i]) +ord(key[i])) % 26
    x += 65
    ciphertext.append(chr(x)) 
  string = ''.join(map(str, ciphertext))
  T = tk.Text(tab1, height = 5, width = 15)
  T.insert(1.0,string)
  T.grid(row=2, column=1, padx=15, pady=15)

def decryption2():
  string = Cipher2Entry.get()
  key = Key2Entry.get()
  key = generateKey(string,key)
  plaintext = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) -ord(key[i]) +26 ) % 26
    x += 65
    plaintext.append(chr(x))
  string = ''.join(map(str, plaintext))
  T = tk.Text(tab2, height = 5, width = 15)
  T.insert(1.0,string)
  T.grid(row=2, column=1, padx=15, pady=15)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Vigenère Cipher Application")
    tabControl = ttk.Notebook(root)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab1, text ='Encryption')
    tabControl.add(tab2, text ='Decryption')
    Plain1 = tk.Label(tab1, text="Plain Text:")
    Key1 = tk.Label(tab1, text="Key:")
    Cipher1 = tk.Label(tab1, text="Cipher Text:")
    Cipher2 = tk.Label(tab2, text="Cipher Text:")
    Key2 = tk.Label(tab2, text="Key:")
    Plain2 = tk.Label(tab2, text="Plain Text:")
    Plain1Entry = tk.Entry(tab1)
    Key1Entry = tk.Entry(tab1)
    Cipher2Entry = tk.Entry(tab2)
    Key2Entry = tk.Entry(tab2)
    Encrypt = tk.Button(tab1, text="Encrypt with tabula recta", command=encryption2)
    Decrypt = tk.Button(tab2, text="Decrypt with  tabula recta", command=decryption2)
    Encrypt1 = tk.Button(tab1, text="Encrypt with custom table", command=encryption)
    Decrypt1 = tk.Button(tab2, text="Decrypt with custom table", command=decryption)
    Plain1.grid(row=0, column=0, padx=15, pady=15)
    Plain1Entry.grid(row=0, column=1, padx=15, pady=15)
    Key1.grid(row=1, column=0, padx=15, pady=15)
    Key1Entry.grid(row=1, column=1, padx=15, pady=15)
    Cipher1.grid(row=2, column=0, padx=15, pady=15)
    Encrypt.grid(row=3, column=2, padx=15, pady=15)
    Encrypt1.grid(row=3, column=3, padx=15, pady=15)
    Cipher2.grid(row=0, column=0, padx=15, pady=15)
    Cipher2Entry.grid(row=0, column=1, padx=15, pady=15)
    Key2.grid(row=1, column=0, padx=15, pady=15)
    Key2Entry.grid(row=1, column=1, padx=15, pady=15)
    Plain2.grid(row=2, column=0, padx=15, pady=15)
    Decrypt.grid(row=3, column=2, padx=15, pady=15)
    Decrypt1.grid(row=3, column=3, padx=15, pady=15)
    tabControl.pack(expand = 1, fill ="both")
    root.mainloop()
