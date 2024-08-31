import paramiko
import time

def ssh_connect(hostname, port, username, password):
    try:
        # Create an SSH client instance
        client = paramiko.SSHClient()

        # Automatically add the remote server's SSH key (use with caution)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote device
        client.connect(hostname, port=port, username=username, password=password)

        print(f"Connected to {hostname}")

        # Start an interactive shell session on the remote device
        remote_conn = client.invoke_shell()

        # Wait for the prompt to be ready
        time.sleep(1)
        remote_conn.recv(1000)

        # Send a command to the remote device
        remote_conn.send("show version\n")

        # Wait for the command to execute
        time.sleep(2)

        # Receive the output from the remote device
        output = remote_conn.recv(5000).decode('utf-8')

        # Print the output to the console
        print(output)

        # Close the connection
        client.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace these variables with your device's information
    hostname = "192.168.1.1"
    port = 22
    username = "admin"
    password = "your_password"

    # Call the SSH connect function
    ssh_connect(hostname, port, username, password)
