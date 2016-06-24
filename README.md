## SeeChic ecommerce test ##

The repository contains the django project files required by [SeeChic](http://seechic.com)

**The project contains:**
- simple ecommerce site contains the main features:
    - Login and SignUp
    - Products
    - Sales Orders
    - Shopping Cart
- ecommerce integration with [odoo 8.0](http://odoo.com)
    - Products Integration
    - Customers Integration
    - Sales orders Integration

### Django Version
1.8.7

### Odoo Version
8.0

### Installation

Clone the repo to your local machine
```
git clone [repo_url] seechic
```

Install postgresql
```
$ sudo apt-get install postgresql
```

You need VirtualEnvWrapper installed globally:

```
$ pip install virtualenvwrapper
...
$ export WORKON_HOME=~/.virtualenvs
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv seechic
```

Install development requirments
```
$ cd seechic/requirements
$ pip install -r development.txt
```

Edit VirtualEnv postactivate and predeactivate scripts to set *DJANGO_SETTINGS_MODULE*

```
$ vim ~/.virtualenvs/seechic/bin/postactivate
```
write in the file:
```
export DJANGO_SETTINGS_MODULE="config.settings.development"
```
```
$ vim ~/.virtualenvs/seechic/bin/predeactivate
```
write in the file:
```
unset DJANGO_SETTINGS_MODULE
```

Create new file called "secret.py" in settings directory
```
$ vim config/settings/secret.py
```

Write in the file:
```
SECRET_KEY = "YOUR_SECRET_KEY"
DB_NAME = "YOUR_DB_NAME"
DB_USER = "YOUR_DB_USER"
DB_PASSWORD = "YOUR_DB_PASSWORD"
DB_HOST = "YOUR_DB_HOST"
```

Run the server
```
python manage.py runserver
```
