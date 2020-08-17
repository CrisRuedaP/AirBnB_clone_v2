#!/usr/bin/env bash
#sets up a web servers for the deployment of web_static
file="location /hbnb_static/ {\nalias /data/web_static/current;\n}"
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "35i $file" /etc/nginx/sites-enabled/default
sudo service nginx restart
