# Remote SSH for Kaggle

Utilities to **connect Kaggle Notebook with GitHub and VS Code via SSH** using key-based authentication.

This project is designed for **non-interactive environments** like Kaggle, where SSH confirmations must be handled automatically.

---

## Features

* Setup SSH server on Kaggle
* Configure GitHub SSH authentication
* Clone GitHub repositories via SSH
* Expose SSH using ngrok
* Connect with VS Code Remote-SSH

---

## Requirements

* GitHub SSH key (ED25519 recommended)
* Kaggle Notebook with Internet enabled
* Optional: ngrok auth token

> **Note:** All secrets (SSH keys, passwords, tokens) must be stored using **Kaggle Secrets**.
> No sensitive data is committed to this repository.

---

## Basic Usage (Kaggle)

```python
import sys
sys.path.append('/kaggle/working/remote-ssh')

from remote_setup.connect import (
    setup_github_config,
    clone_project_from_github,
    connect_vscode
)

# One-time: trust GitHub SSH host
!ssh-keyscan -p 443 ssh.github.com >> ~/.ssh/known_hosts

setup_github_config()

clone_project_from_github(
    giturl='git@github.com:ORG/REPO.git',
    folder='/kaggle/working/project',
    branch='main'
)

connect_vscode()
```

---

## Security Notes

* SSH keys are **never stored in this repo**
* Host verification is handled automatically for notebook environments
* Recommended for **development and research**, not production

