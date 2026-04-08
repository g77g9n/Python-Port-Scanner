import socket
import datetime

print("-" * 50)
print("Starting Personal Port Scanner...")
print("Time started: " + str(datetime.datetime.now()))
print("-" * 50)

target = "127.0.0.1" 

try:
    for port in range(1, 500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5) 
        
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"[*] Alert: Port {port} is OPEN")
            
        s.close() 

except KeyboardInterrupt:
    print("\nExiting Program.")
except socket.error:
    print("\nServer not responding.")

print("-" * 50)
print("Scan Complete!")