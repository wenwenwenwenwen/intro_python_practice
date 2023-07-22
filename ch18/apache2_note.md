## Apache2
**Reference:**
- https://www.blopig.com/blog/2022/10/using-conda-environments-with-flask-and-apache/
- https://stackoverflow.com/questions/20627327/invalid-command-wsgiscriptalias-perhaps-misspelled-or-defined-by-a-module-not

1. install apache2
    ```
    $ sudo apt install apache2
    ```

2. create conda env for apache2 (python3.8)
    ```
    $ source miniconda3/bin/activate
    $ conda create --name apache2 python=3.8
    ```

3. install bottle
    ```
    $ pip3 install bottle, mod_wsgi
    ```

4. get `mod_wsgi-express` path
    ```
    $ which mod_wsgi-express
    /home/<user name>/miniconda3/envs/apache2/bin/mod_wsgi-express
    ```

5. get the information needed to configure Apache to use this mod_wsgi
    ```
    $ sudo /home/<user name>/miniconda3/envs/apache2/bin/mod_wsgi-express install-module
    LoadModule wsgi_module "/usr/lib/apache2/modules/mod_wsgi-py38.cpython-38-x86_64-linux-gnu.so"
    WSGIPythonHome "/home/<user name>/miniconda3/envs/apache2"
    ```

6. set /etc/apache2/mods-available/wsgi.conf(& wsgi.load) files
    **wsgi.load**
    ```
    LoadModule wsgi_module "/usr/lib/apache2/modules/mod_wsgi-py38.cpython-38-x86_64-linux-gnu.so"
    ```
    **wsgi.conf**
    ```
    <IfModule mod_wsgi.c>
        WSGIPythonHome "/home/<user name>/miniconda3/envs/apache2"
    </IfModule>
    ```

7. add the following script to /etc/apache2/site-available/000-default.conf
    ```
    ...DocumentRoot...
    
    WSGIScriptAlias / /home/<user name>/intro_python_practice/ch18/home.wsgi
    WSGIDaemonProcess testapp python-path="/home/<username>/intro_python_practice/ch18" python-home="/home/<username>/miniconda3/envs/apache2"
    <Directory /home/<user name>/intro_python_practice/ch18>
    WSGIProcessGroup testapp
    WSGIApplicationGroup %{GLOBAL}
    Require all granted
    </Directory>

    ...<VirtualHost>...
    ```

5. change owner
    ```
    $ sudo chown www-data:www-data -R /etc/apache2(& /var/www)
    ```

6. add user to group www-data
    ```
    sudo usermod -a -G www-data <user name>
    ```

7. enable wsgi mod in Apache -> start service -> stop service
    ```
    sudo a2enmod wsgi
    sudo service apache2 restart
    sudo service apache2 stop
    ```
