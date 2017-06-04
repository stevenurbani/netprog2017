import websocket

# Buat object websocket
ws = websocket.WebSocket()
# Buat koneksi ke server
ws.connect("ws://localhost:8877")

ws.send("Tes")

data = ws.recv()

print data