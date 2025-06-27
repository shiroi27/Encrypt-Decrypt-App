from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():
    
    screen = Tk()
    screen.geometry("940x500+400+100")
    screen.title("ENCRYPT AND DECRYPT")
    screen.config(bg="#8AC6FB")

    # Header
    header_frame = Frame(screen, width=940, height=60, bg="#FFA861")
    header_frame.place(x=0, y=0)
    header_label = Label(header_frame, text="🔐 ENCRYPT AND DECRYPT", font=("Times New Roman", 32, "bold"), bg="#FFA861", fg="#000000")
    header_label.place(relx=0.52, rely=0.5, anchor=CENTER)

    decorative_line = Frame(screen, bg="#ED4A4A", height=6, width=940)
    decorative_line.place(x=0, y=60)

    # Text Input
    Label(screen, text="Enter Text :", fg="#000000", font=("Times New Roman", 20 , "bold"),bg="#8AC6FB").place(x=20, y=80)
    text1 = Text(screen, font=("Georgia", 24 , "bold"), bg="#FFFFFF", fg="#000000", relief=GROOVE, wrap=WORD, bd=2)
    text1.place(x=20, y=110, width=400, height=150)

    # Secret Key
    Label(screen, text="Enter Secret Key :", fg="#000000", font=("Times New Roman", 20,"bold"),bg="#8AC6FB").place(x=20, y=280)
    code = StringVar()
    Entry(textvariable=code, width=22, bd=2, font=("Times New Roman", 18 , "bold")).place(x=20, y=310)

    # Output Labels and Boxes 
    Label(screen, text="Decrypted Message :", fg="#000000",font=("Times New Roman", 20 ,"bold"),bg="#8AC6FB").place(x=470, y=80)
    decrypted_output = Text(screen, font=("Georgia", 24 , "bold"), bg="#FFFFFF", fg="#000000", relief=GROOVE, wrap=WORD, bd=2)
    decrypted_output.place(x=470, y=110, width=440, height=150)

    Label(screen, text="Encrypted Message :",fg="#000000",font=("Times New Roman", 20,"bold"),bg="#8AC6FB").place(x=470, y=270)
    encrypted_output = Text(screen, font=("Georgia", 24,"bold"), bg="#FFFFFF", fg="#000000", relief=GROOVE, wrap=WORD, bd=2)
    encrypted_output.place(x=470, y=300, width=440, height=150)

    def encrypt_message():
        message = text1.get("1.0", END).strip()
        key = code.get()
        if message:
            if key == "12345":
                encoded_bytes = base64.b64encode(message.encode("utf-8"))
                encrypted_output.delete("1.0", END)
                encrypted_output.insert(END, encoded_bytes.decode("utf-8"))
            else:
                messagebox.showerror("Error", "Wrong secret key.")

    def decrypt_message():
        encrypted_text = encrypted_output.get("1.0", END).strip()
        if not encrypted_text:
            encrypted_text = text1.get("1.0", END).strip()
        key = code.get()
        if encrypted_text and key:
            if key == "12345":
                try:
                    decoded_bytes = base64.b64decode(encrypted_text)
                    decrypted_output.delete("1.0", END)
                    decrypted_output.insert(END, decoded_bytes.decode("utf-8"))
                except:
                    messagebox.showerror("Error", "Invalid encrypted message or format.")
            else:
                messagebox.showerror("Error", "Wrong secret key.")
                return

    def reset_fields():
        text1.delete("1.0", END)
        code.set("")
        decrypted_output.delete("1.0", END)
        encrypted_output.delete("1.0", END)

    # Buttons
    Button(text="ENCRYPT", height=2, width=18, bg="#FFB6C1", fg="#000000", bd=1, command=encrypt_message).place(x=20, y=360)
    Button(text="DECRYPT", height=2, width=18, bg="#90EE90", fg="#000000", bd=1, command=decrypt_message).place(x=243, y=360)
    Button(text="RESET", height=2, width=43, bg="#8AC6FB", fg="#000000", bd=1, command=reset_fields).place(x=20, y=420)

    screen.mainloop()

main_screen()