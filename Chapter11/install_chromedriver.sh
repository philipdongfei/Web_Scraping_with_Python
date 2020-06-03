#!/usr/bin/env bash
# install google chrome and chromedriver

sudo apt-get update
sudo apt-get install -y curl unzip xvfb libxi6 libgconf-2-4
sudo apt-get install default-jdk
#sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
sudo apt-key add linux_signing_key.pub
sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
#sudo apt-get -y install google-chrome-stable
sudo dpkg -i google-chrome-stable_83.0.4103.61-1_amd64.1.deb
#wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver83_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver

