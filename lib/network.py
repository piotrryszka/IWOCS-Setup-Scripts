# imports
import paramiko


# need to add more arguments, like to make host, username, password correct in every case
def ip_connect():
    # checking private configuration
    host = "pluton.kt.agh.edu.pl"
    port = 22
    username = "msztaba"
    # needs to be hashed
    password = "098azerty@MS"

    # project-config settings
    # username = walter
    # password = mel0n98
    # host = f'172.30.100.{ip_number}'


    # creating list of commands to be executed
    try:
        with open("tftp-conf-files/commands.txt", 'r') as my_file:
            content = my_file.read()
            content_list = content.split("\n")

        # creating connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)

        # executing commands
        for command in content_list:
            stdin, stdout, stderr = ssh.exec_command(command)
            lines = stdout.readlines()
            print(lines)

        # closing connection
        ssh.close()
    except:
        print("something went wrong")
