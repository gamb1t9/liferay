# Enable required Apache modules by uncommenting the corresponding lines
sed -i '/^#LoadModule proxy_module/s/^#//'  /usr/local/apache2/conf/httpd.conf
sed -i '/^#LoadModule proxy_balancer_module/s/^#//'  /usr/local/apache2/conf/httpd.conf
sed -i '/^#LoadModule proxy_ajp_module/s/^#//'  /usr/local/apache2/conf/httpd.conf
sed -i '/^#LoadModule headers_module/s/^#//'  /usr/local/apache2/conf/httpd.conf
sed -i '/^#LoadModule proxy_http_module/s/^#//'  /usr/local/apache2/conf/httpd.conf
sed -i '/^#LoadModule slotmem_shm_module/s/^#//' /usr/local/apache2/conf/httpd.conf
sed -i '/^#LoadModule lbmethod_byrequests_module/s/^#//' /usr/local/apache2/conf/httpd.conf

# Include the custom virtual host configuration
echo "Include conf/extra/liferay.conf" >> /usr/local/apache2/conf/httpd.conf

# Start Apache service
httpd-foreground
