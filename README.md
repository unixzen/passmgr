# passmgr
Simplest password manager

#### Dependencies

* sqlite
* python3

#### Prepare

1. First of all need install [sqlite](https://sqlite.org/docs.html) database.

* Debian

```
sudo apt install sqlite
```

* Centos

```
sudo yum install sqlite
```

2. Clone repo [passmgr](https://github.com/unixzen/passmgr.git).

```
git clone https://github.com/unixzen/passmgr.git
```

3. Create database where will be store data about passwords.

```
sqlite3 DatabaseName.db
```

or you can use action `create_db` of passmgr. Will be create database with fields: title, username, password, description.

```
python3 passmgr.py create_db DatabaseName.db
```

#### Usage

```
python3 passmgr.py <action> <param 1> <param 2> ... <param N>
```

You can see help, just type:

```
python3 passmgr.py help
```

Output:

```
Usage: passmgr.py <action> <params>
action: show_all, show, edit, add.
For example, add action: python3 passmgr.py add bank login password 'Enter to internet bank'
For example, edit action: python3 passmgr.py edit bank username login1
For example, show action: python3 passmgr.py show bank
show_all action output all items at passmgr
```

#### TODO

* Make webapp passmgr
* Encrypt for database

