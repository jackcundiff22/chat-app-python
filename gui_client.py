import socket 
import threading 
import tkinter as tk 
from tkinter import scrolledtext

HOST = '127.0.0.1'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nickname = None 

def start_gui():
  def send_message():
    message = f"{nickname}: {msg_entry.get()}"
    client.send(message.encode('utf-8'))
    msg_entry.delete(0, tk.END)

  def recieve_messages():
    while True:
      try:
        message = client.recv(1024).decode('utf-8')
        if message == 'NICK':
          client.send(nickname.encode('utf-8'))
        else:
          chat_box.config(state='normal')
          chat_box.insert(tk.END, message + '\n')
          chat_box.yview(tk.END)
          chat_box.config(state='disabled')

      except:
         break

  window = tk.Tk()
  window.title("Chat Client")

  chat_box = scrolledtext.ScrolledText(window, state='disabled', wrap='word')
  chat_box.pack(padx=20, pady=5, fill='both', expand=True)

  msg_entry = tk.Entry(window)
  msg_entry.pack(padx=20, pady=(0,5), fill='x')

  send_button = tk.Button(window, text="Send", command=send_message)
  send_button.pack(pady=(0,10))

  thread = threading.Thread(target=recieve_messages)
  thread.daemon = True
  thread.start()

  window.mainloop()



nickname = input("Enter your nickname: ")
try:
  client.connect((HOST, PORT))

except: 
  print("Unable to connect to server.")
  exit()

start_gui()



        


