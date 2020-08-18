#!/usr/bin/env bash
#sets up a web servers for the deployment of web_static

file="\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir /data/web_static/releases/test/
sudo mkdir /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i "35i $file" /etc/nginx/sites-available/default
sudo service nginx restart
