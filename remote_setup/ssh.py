from IPython import get_ipython

def start_ssh(id_rsa_pub="", password="", install_ssh=False, config_ssh=False):
    print(f'{"*" * 10} SETUP SSH SERVICE {"*"*10}')

    ip = get_ipython()

    if install_ssh:
        ip.system('apt-get update > /dev/null')
        ip.system('apt-get install -y openssh-server > /dev/null')

    if id_rsa_pub:
        ip.system('mkdir -p ~/.ssh')
        ip.system(f'echo "{id_rsa_pub}" >> ~/.ssh/authorized_keys')
        ip.system('chmod 700 ~/.ssh')
        ip.system('chmod 600 ~/.ssh/authorized_keys')

    if config_ssh:
        cfgs = [
            "Port 22",
            "ListenAddress 0.0.0.0",
            "PermitRootLogin yes",
            "PubkeyAuthentication yes",
            "PasswordAuthentication yes",
            "AllowTcpForwarding yes",
            "GatewayPorts yes"
        ]
        for line in cfgs:
            key = line.split()[0]
            ip.system(
                f"sed -i 's/^#*{key}.*/{line}/' /etc/ssh/sshd_config"
            )

    if password:
        ip.system(f'echo -e "{password}\\n{password}" | passwd root > /dev/null')

    ip.system('service ssh restart')

    ip.system('grep -qx "^TERM=xterm-256color$" ~/.bashrc || echo "TERM=xterm-256color" >> ~/.bashrc')

    print(f'{"-" * 10} Finished {"-"*10}')
