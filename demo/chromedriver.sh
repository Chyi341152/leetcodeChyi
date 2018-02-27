#!/usr/bin/env bash

# Install Chrome, ChromeDriver and Selenium on Ubuntu

# Versions
CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`


# Remove existing downloads and binaries so we can start from scratch
sudo apt-get remove google-chrome-stable
rm ~/Downloads/chromedriver_linux64.zip
sudo rm /usr/local/chromedriver

# Install dependencies
sudo apt-get update
sudo apt-get install -y unzip

# Install Chrome.
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable

# Install ChromeDriver.
wget -N http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -P ~/Downloads/
unzip ~/Downloads/chromedriver_linux64.zip -d ~/Downloads/
rm ~/Downloads/chromedriver_linux64.zip
sudo mv -f ~/Downloads/chromedriver /usr/local/bin/chromedriver
sudo chown $USER:$USER /usr/local/bin/chromedriver
sudo chmod 0755 /usr/local/bin/chromedriver

# Install selenium
pip3 install selenium
