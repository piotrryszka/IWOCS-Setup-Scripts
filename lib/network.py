# settling ip connection
import paramiko

def ip_connect(ip-number):

    # setting
    ip_address = f'172.30.100.{ip-number}'
    # ask if it is correct
    router_username = "walter"
    router_password = "mel0n98"

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # connecting by our data
    ssh.connect(ip_address,
            username=router_username,
            password=router_password,
            look_for_keys=False )

    # running some commands to check if it device is configured
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("show ip route")

    # getting output
    output = ssh_stdout.readlines()

    # closing connection
    ssh.close()
