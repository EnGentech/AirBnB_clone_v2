#!/usr/bin/env bash
# Proceed for deployment of web_static

sudo apt-get update
sudo apg-get upgrade -y

sudo apt-get install nginx -y
sudo service nginx start
sudo chmod -R 777 /var/www/
sudo chmod -R 777 /etc/nginx/sites-enabled/default

cp /var/www/html/index.html /var/www/html/back_up
echo "Hello World!" > /var/www/html/index.html

file_path="/data/web_static/releases/test"
if [ ! -d "$file_path" ]; then
    sudo mkdir -p "$file_path"
fi

sudo touch /data/web_static/releases/test/index.html
sudo chmod -R 777 /data/

printf "<!Doctype html>
<html>
<head>
    <title>MyTestFile</title>
</head>
<body>
    <p>Holberton School</p>
</body>
</html>" > /data/web_static/releases/test/index.html

link_path="/data/web_static/current"
tag_path="/data/web_static/releases/test/"

if [ -L "$link_path" ]; then
    sudo rm "$link_path"
fi

sudo ln -s "$tag_path" "$link_path"

sudo chown -R ubuntu /data/

printf "
server {\n
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    add_header X-Served-By $HOSTNAME;
    server_name engentech.tech;

    location /hbnb_static {
        alias /data/web_static/current/;
    }

    location /redirect_me {

        try_files $uri $uri/ =404;
    }
}" > /etc/nginx/sites-enabled/default

sudo service nginx restart
