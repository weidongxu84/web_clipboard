Introduction
============

A very simple shared text clipboard web application.

Install Guide
=============

**Install Apache, MySQL, mod-wsgi (Apache)**

Command line for GNU Debian:

> sudo apt-get install apache2 mysql-server libapache2-mod-wsgi

**Configure site and database**

Modify "web_clipboard/web_clipboard/settings.py", for "ADMINS" and "DATABASES" setting.

Modify "web_clipboard/web_clipboard.conf", for site location.

**Create database**

Command line:

> mysql -u root -p

> mysql> create database web_clipboard;

> mysql> exit

**Synchronize database**

Command line:

> ../env/bin/python manage.py syncdb

> ../env/bin/python manage.py migrate

**Configure Apache**

Link Apache conf file, then restart Apache.

Command line:

> sudo ln -s web_clipboard.conf /etc/apache2/conf.d/web_clipboard.conf
> sudo apache2ctl graceful
