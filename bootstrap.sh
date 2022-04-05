#!/bin/bash

export DEBIAN_FRONTEND=noninteractive
export INSTALL_ZSH=true
export USERNAME=`whoami`
export PIPENV_VENV_IN_PROJECT="enabled"

## update and install required packages
sudo apt update
sudo apt -y install --no-install-recommends apt-utils dialog 2>&1
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt install -y \
  curl \
  git \
  gnupg2 \
  jq \
  sudo \
  openssh-client \
  less \
  iproute2 \
  procps \
  wget \
  unzip \
  apt-transport-https \
  lsb-release \
  python3.9

  # Install & Configure Zsh
if [ "$INSTALL_ZSH" = "true" ]
then
    sudo apt-get install -y \
    fonts-powerline \
    zsh

    cp -f ~/dotfiles/.zshrc ~/.zshrc
    chsh -s /usr/bin/zsh $USERNAME
    wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
    echo "source $PWD/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc
fi

# Python
curl https://bootstrap.pypa.io/get-pip.py -o $HOME/get-pip.py
python3.9 $HOME/get-pip.py
sudo update-alternatives --install $HOME/.python/current/bin/python python /usr/bin/python3.9 3
sudo update-alternatives --install $HOME/.python/current/bin/python python /usr/bin/python3.8 2
sudo update-alternatives --install $HOME/.python/current/bin/python python /usr/bin/python2.7 1

# Cleanup
sudo apt-get autoremove -y
sudo apt-get autoremove -y
sudo rm -rf /var/lib/apt/lists/*