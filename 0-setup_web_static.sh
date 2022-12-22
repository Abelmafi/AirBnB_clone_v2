#!/usr/bin/env bash
# inital configration
if [ $? -ne 0 ]; then
	sudo apt-get -y update
	sudo apt-get install -y install nginx
else
	echo "Already installed"
fi

# configure file system
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Hello world2!" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# set permissions
sudo chown -R ubuntu:ubuntu /data/

# configure nginx
sudo sed -i '44i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

sudo service nginx restart
