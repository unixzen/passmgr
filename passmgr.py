#!/usr/bin/env python3

import sqlite3
import sys

def create_db(database_name):
  con = sqlite3.connect(database_name)
  cur = con.cursor()
  cur.execute('CREATE TABLE pass (id INTEGER PRIMARY KEY, title VARCHAR(100), username VARCHAR(100), password VARCHAR(30), description TEXT)')
  con.commit()
  con.close()
  print(f"Created database {database_name}")

def add_item(title, username, password, description):
  con = sqlite3.connect('pass.db')
  cur = con.cursor()
  cur.execute('INSERT INTO pass (id, title, username, password, description) VALUES(NULL, ?, ?, ?, ?)', (title, username, password, description))
  con.commit()
  con.close()
  print(f"You insert {title}, {username}, {password}, {description}")

def edit_item(title, item, new_item):
  con = sqlite3.connect('pass.db')
  cur = con.cursor()
  t = (new_item, title)
  title_show = (title,)
# OUTPUT BEFORE CHANGES
  cur.execute('SELECT title, username, password, description FROM pass WHERE title = ?', title_show)
  print("BEFORE")
  for row in cur:
    print('-'*50)
    print('title:', row[0])
    print('username:', row[1])
    print('password:', row[2])
    print('description:', row[3])
    print('-'*50)
  if item == "username":
    cur.execute('UPDATE pass SET username = ? WHERE title = ?', t)
    print("Edited username field")
  elif item == "password":
    cur.execute('UPDATE pass SET password = ? WHERE title = ?', t)
    print("Edited password field")
  else:
    cur.execute('UPDATE pass SET description = ? WHERE title = ?', t)
    print("Edited description field")
  con.commit()
  cur.execute('SELECT title, username, password, description FROM pass WHERE title = ?', title_show)
# OUTPUT AFTER CHANGES
  print("AFTER")
  for row in cur:
    print('-'*50)
    print('title:', row[0])
    print('username:', row[1])
    print('password:', row[2])
    print('description:', row[3])
    print('-'*50)
  con.close()

def show_item(title):
  con = sqlite3.connect('pass.db')
  cur = con.cursor()
  t = (title,)
  cur.execute('SELECT username, password, description FROM pass WHERE title = ?', t)
  print("This row where title is", str(title))
  for row in cur:
    print('-'*50)
    print('username:', row[0])
    print('password:', row[1])
    print('description:', row[2])
    print('-'*50)
  con.close()

def show_all():
  con = sqlite3.connect('pass.db')
  cur = con.cursor()
  cur.execute('SELECT title, username, password, description FROM pass')
  for row in cur:
    print('-'*50)
    print('title:', row[0])
    print('username:', row[1])
    print('password:', row[2])
    print('description:', row[3])
    print('-'*50)
  con.close()

def help():
  print("Usage: passmgr.py <action> <params>")
  print("action: show_all, show, edit, add.")
  print("For example add action: python3 passmgr.py add bank login password 'Enter to internet bank'")
  print("For example edit action: python3 passmgr.py edit bank username login1")
  print("For example show action: python3 passmgr.py show bank")
  print("show_all action output all items at passmgr")

def main():
  if sys.argv[1] == "create":
    create_db(str(sys.argv[2]))
  if sys.argv[1] == "add":
    add_item(str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]), str(sys.argv[5]))
  if sys.argv[1] == "show":
    show_item(str(sys.argv[2]))
  if sys.argv[1] == "show_all":
    show_all()
  if sys.argv[1] == "edit":
    edit_item(str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]))
  if sys.argv[1] == "help":
    help()


if __name__ == '__main__':
    main()
