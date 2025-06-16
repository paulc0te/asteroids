# asteroids

It's an [Asteroids](https://en.wikipedia.org/wiki/Asteroids_(video_game))  like game based on pygame

### Prerequisites
* Python 3.10+ installed   
* Access to a unix-like shell (e.g. zsh or bash)   
* If you are on WSL, you will probably need to install VcXsrv to run pygame. Follow the installation and configuration instructions on the linked site.


### Dev notes

```bash
cd /u01/workspace/github.com/paulc0te/asteroids
python3.12 -m venv venv
. venv/bin/activate
pip3.12 install -r requirements.txt
pip3.12 freeze
```

### Launch in Windows 11

[information about wsl](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps)

```bash
run powershell
wsl --install
sudo apt install x11-apps -y
sudo apt update
Install python3.12, pip3.12
wsl# cd /u01/asteroids
rm -rf venv
python3.12 -m venv venv
. venv/bin/activate
pip3.12 install -r requirements.txt
python3.12 main.py
```
