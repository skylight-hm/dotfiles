#!/usr/bin/python3
import os
import argparse
import subprocess as sb

from loguru import logger

PATH_USER_BIN = "/usr/bin"
PATH_USER = "/usr"

def run(command):
    ls_command = command.split(" ")
    p = sb.run(ls_command)
    if p.returncode != 0:
        logger.error(f"\"{command}\" execute failed!")
        raise SystemExit()
    return 0

def install_tmux(github_proxy):
    # check tmux exists 
    if os.path.exists(f"{PATH_USER_BIN}/tmux"):
        logger.info(f"neomvim exsits at {PATH_USER_BIN}/tmux.")
    # download latest tmux and install
    else:
        command = "apt install -y tmux"
        p = sb.run(command)
        if p.returncode != 0:
            logger.error("tmux install failed!")

def install_btm(github_proxy):
    # check btm exists 
    if os.path.exists(f"{PATH_USER_BIN}/btm"):
        logger.info(f"neomvim exsits at {PATH_USER_BIN}/btm.")
    # download 0.9.3 btm and install
    else:
        command = f"curl -LO {github_proxy}https://github.com/ClementTsang/bottom/releases/download/0.9.3/bottom_0.9.3_amd64.deb && sudo dpkg -i bottom_0.9.3_amd64.deb && rm -f bottom_0.9.3_amd64.deb"
        p = sb.run(command)
        if p.returncode != 0:
            logger.error("btm install failed!")

def install_nnn(github_proxy):
    # check nnn exists 
    if os.path.exists(f"{PATH_USER_BIN}/nnn"):
        logger.info(f"neomvim exsits at {PATH_USER_BIN}/nnn.")
    # download latest nnn and install
    else:
        command = "apt install -y nnn"
        p = sb.run(command)
        if p.returncode != 0:
            logger.error("nnn install failed!")

def install_neovim(github_proxy, force=False):
    # check neovim exists 
    if os.path.exists(f"{PATH_USER_BIN}/nvim") and force == False:
        logger.info(f"neomvim exsits at {PATH_USER_BIN}/nvim.")
    # download latest neovim and install
    else:
        command = f"wget {github_proxy}https://github.com/neovim/neovim/releases/download/stable/nvim-linux64.tar.gz" 
        run(command)
        command = f"tar xvf nvim-linux64.tar.gz --strip-components 1 -C {PATH_USER}" 
        run(command)
        command = "rm -rf nvim-linux64.tar.gz"
        run(command)
    
def main():
    parser = argparse.ArgumentParser(description="install app")
    parser.add_argument("--no-ghproxy", "-ng", action='store_false',
                        help="without ghproxy clone")
    parser.add_argument("--force", "-f", action='store_true',
                        help="force execute")
    args = parser.parse_args()
    github_proxy = "https://ghproxy.com/" if args.no_ghproxy else ""
    force = args.force
    
    install_nnn(github_proxy, force)
    install_tmux(github_proxy, force)
    install_btm(github_proxy, force)
    install_neovim(github_proxy, force)
    
if __name__ == "__main__":
    main()