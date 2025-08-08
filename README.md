#  Python Multiplayer Chat App (CLI + Tkinter GUI)

A **multithreaded chat application** built in Python using sockets.  
Includes both a **command-line interface (CLI)** client and an optional **Tkinter-based GUI** client for a more user-friendly experience.

---

# Features
- Real-time chat between multiple clients.
- Nickname prompt on join.
- Join/leave notifications.
- CLI client for lightweight use.
- Tkinter GUI client with scrollable chatbox.
- Multithreaded server for handling many clients at once.
- Easy to configure host & port.

---



# Requirements
- **Python 3.8+**
- `tkinter` (included with most Python installs; Linux users may need `sudo apt install python3-tk`)

---



### 1) Clone the repository
```bash
git clone https://github.com/<jackcundiff22>/<chat-app-python>.git
cd <chat-app-python>

### 2) Start the server
```bash
python server.py
```
You should see:
```
Server is listening...
```

### 3) Run one or more clients
Open new terminals for each client and run:
```bash
python client.py
```
Enter a nickname when prompted and start chatting!

### (Optional) Run the GUI client
```bash
python gui_client.py
```
> Note: Tkinter GUIs do not run on Replit. Use the CLI client on Replit, or run the GUI locally.

# Default Configuration
The default host and port are set to localhost:
```python
HOST = "127.0.0.1"
PORT = 55555
```
To allow connections from other machines on your LAN, run the server with:
```python
HOST = "0.0.0.0"
```
Then have clients connect using the server machine’s local IP (e.g., `192.168.x.x`).

# Project Structure
```
.
├─ server.py        # TCP server that accepts clients and broadcasts messages
├─ client.py        # Command-line client (nickname prompt, send/receive threads)
├─ gui_client.py    # Tkinter GUI client (optional)
└─ README.md
```

# How It Works (Brief)
- **Server**:
  - `accept()` new client connections in a loop
  - Request and store a nickname
  - Start a thread per client to `recv()` messages and `broadcast()` them
- **Client**:
  - Start a `receive()` thread to continuously print incoming messages
  - Main thread (or a `write()` thread) sends user input to the server

# Troubleshooting
- **`ConnectionRefusedError`**: Start the server first, verify host/port, and ensure no firewall is blocking localhost.
- **GUI won’t open on Replit**: Replit doesn’t support desktop GUIs. Use `client.py` there.
- **No messages appear**: Make sure clients and server use the **same** host/port and you’re not mixing networks.

# Next Steps (Ideas)
- Private DMs (`/dm <user> <msg>`)
- Timestamps and colored usernames
- Chat history logging to file
- User authentication
- Flask/Socket.IO web version for browser clients

# License
MIT (optional—add a `LICENSE` file if you want)

---

Made with ❤️ in Python. Have fun hacking!
