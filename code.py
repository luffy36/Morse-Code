import tkinter
import sys
from tkinter import messagebox
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

encrypt_message = ''
decrypt_message = ''
#function to encrypt
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter !=' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher

def decrypt(message):
    message +=' '

    decipher = ''
    citext = ''

    for letter in message:
        if ( letter != ' '):

            i = 0
            citext += letter
        else:
            i += 1

            if i == 2:
                decipher +=' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher

root = tkinter.Tk()

root.title("Morse Code Encrypter And Decrypter")
root.configure(background = 'blue')
root.geometry("400x200")

instructions =  tkinter.Label(root, text = "Choose if to Encrypt or Decrypt\n\n",bg = 'blue', font = ('Helvetica',15))
instructions.pack()

def B_Call_back():
    top = tkinter.Tk()
    top .title("Encrypter")
    top.configure(bg = 'green')
    def E_Call_back():
        etext = e.get()
        result = encrypt(etext)
        label1 = tkinter.Label(top,text="\n Encrypted Message is : \n",bg = 'green').pack()
        elabel = tkinter.Label(top, text = result,bg = 'green',font = ('Arial',15)).pack()
    line = tkinter.Label(top , text = "\n",bg = 'green')
    line.pack()
    top.geometry("400x200")
    e = tkinter.Entry(top, textvariable=encrypt_message,)
    e.pack(side='top')
    E = tkinter.Button(top , text = " OK ",bg = 'red', command = E_Call_back)
    E.pack()
    return

def C_Call_back():
    top = tkinter.Tk()
    top.title("Decrypter")
    top.configure(bg='green')

    def E_Call_back():
        etext = e.get()
        result = decrypt(etext)
        label1 = tkinter.Label(top, text="\n Decrypted Message is : \n",bg = 'green').pack()
        elabel = tkinter.Label(top, text=result, font=('Arial', 15),bg='green').pack()

    line = tkinter.Label(top, text="\n",bg = 'green')
    line.pack()
    top.geometry("400x200")
    e = tkinter.Entry(top, textvariable=decrypt_message)
    E = tkinter.Button(top, text=" OK ",bg = 'red', command=E_Call_back)
    e.pack()
    E.pack()
    return

B = tkinter.Button(root, text = "Morse Code Encrypter",font = ('Arial',15), bg = 'Black',fg = 'Green', command = B_Call_back)
C = tkinter.Button(root, text = "Morse Code Decrypter",font = ('Arial',15),bg = 'Black',fg = 'Green', command = C_Call_back)
B.pack()
C.pack()
root.mainloop()

