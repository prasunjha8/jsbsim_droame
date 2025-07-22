import socket
import struct

UDP_IP = "127.0.0.1"
UDP_PORT = 5501
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"📡 Listening on {UDP_IP}:{UDP_PORT}")

EXPECTED_LENGTH = 408

while True:
    data, addr = sock.recvfrom(1024)
    print(f"📦 Received {len(data)} bytes")

    if len(data) < EXPECTED_LENGTH:
        print("❗ Incomplete packet")
        continue

    # You can print the first few float values to verify
    values = struct.unpack('d'*1 + 'f'*100, data[:408])  # Try this roughly
    print("📈 Example data:")
    print(f"  Time: {values[0]}")
    print(f"  Latitude (approx): {values[1]}")
    print(f"  Longitude (approx): {values[2]}")
    print(f"  Altitude (approx): {values[3]}")


'''
 /Applications/FlightGear.app/Contents/MacOS/fgfs \
  --aircraft=c172p \
  --fdm=external \
  --native-fdm=socket,out,30,127.0.0.1,5501,udp \
  --native-fdm=socket,in,30,127.0.0.1,5502,udp \
  --generic=socket,out,30,127.0.0.1,5501,udp,fg_net_fdm \
  --timeofday=noon --altitude=500 --vc=60

'''