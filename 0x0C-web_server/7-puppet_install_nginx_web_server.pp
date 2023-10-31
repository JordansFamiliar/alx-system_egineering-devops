#!/usr/bin/env bash
# Configure Nginx for a custom 404 page and start the server.

# Update the package list to ensure we have the latest information.
sudo apt-get update

# Install Nginx web server.
sudo apt-get -y install nginx

# Allow incoming HTTP traffic through the firewall.
ufw allow 'Nginx HTTP'

# Set appropriate permissions for the web directory.
chmod -R 755 /var/www

# Create a basic "Hello World" HTML file as the default web page.
echo 'Hello World' > /var/www/html/index.html

# Define the Nginx server configuration for custom 404 pages.
new_config=\
"server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    location / {
        try_files \$uri \$uri/ =404;
    }
    error_page 404 /404.html;
    location /404.html {
        internal;
    }
    
    if (\$request_filename ~ redirect_me){
        rewrite ^ https://www.youtube.com/watch?v=SDnpEqK7EBQ permanent;
    }
}
"

# Create a custom 404 page for Nginx.
echo "Ceci n'est pas une page" > /var/www/html/404.html

# Apply the server configuration by writing it to the Nginx default site.
echo "$new_config" > /etc/nginx/sites-available/default

# Check if Nginx is running and start or restart it accordingly.
if [ "$(pgrep nginx)" -le 0 ]; then
    service nginx start
else
    service nginx restart
fi
