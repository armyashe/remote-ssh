import os
from IPython import get_ipython

def setup_github_config(private_key_path):
    ip = get_ipython()

    key_name = os.path.basename(private_key_path)
    ssh_dir = os.path.expanduser("~/.ssh")
    key_path = f"{ssh_dir}/{key_name}"

    ip.system("mkdir -p ~/.ssh")
    ip.system(f"cp '{private_key_path}' '{key_path}'")
    ip.system(f"chmod 600 '{key_path}'")

    ssh_config_path = os.path.join(ssh_dir, "config")

    config_block = f"""
Host github.com
    HostName ssh.github.com
    User git
    Port 443
    IdentityFile {key_path}
    IdentitiesOnly yes
"""

    # Append if not exists
    if os.path.exists(ssh_config_path):
        with open(ssh_config_path, "r") as f:
            if "Host github.com" in f.read():
                print("GitHub SSH config already exists")
                return

    with open(ssh_config_path, "a") as f:
        f.write(config_block)

    print("GitHub SSH config added")
    ip.system("ssh -T git@github.com || true")
