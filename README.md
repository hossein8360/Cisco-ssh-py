# Cisco-ssh-py
#With this Python Script you can establish a SSH connection with your Cisco Devices. at first please read README File

Explanation:


paramiko.SSHClient(): This creates an instance of the SSH client.
set_missing_host_key_policy(paramiko.AutoAddPolicy()): Automatically adds the remote host's SSH key to the known hosts (use cautiously in production environments).
invoke_shell(): Starts an interactive shell session on the remote device.
send(): Sends a command to the remote device.
recv(): Receives data from the remote device.
time.sleep(): Provides a delay to ensure commands are fully executed and data is received.

How to Use:

Replace hostname, username, and password with the appropriate values for your Cisco device.
Run the script. It will connect to the specified device, execute the show version command, and print the output.
Important Notes:
Ensure that SSH is enabled on the Cisco device and that the credentials are correct.
The recv() buffer size (5000 in this example) may need to be adjusted based on the command output size.
This script is a basic example. For production use, you may want to include better error handling, logging, and command execution customization.
