import json
from getpass import getpass
from .helpers import clean
from .variables import GREEN, RED, WHITE, END, L_GREEN, L_CYAN

# -------------------------    MAIN   ------------------------- #

def login():
  exist = False
  valid = None
  clean()

  try:
    with open(FILE) as file:
      user = input('Please! Enter your username: ')
      passwd = getpass(prompt='Please! enter your password: ')
      
      db = json.load(file)
      db_user = None
      db_passwd = None


      for x in range(0, len(db)):
        if user in db[x]['name']:
          exist = True
          db_user = db[x]['name']
          db_passwd = db[x]['password']
          break
        else:
          exist = False

      if exist:
        if db_passwd == passwd:
          print(f'{GREEN}Acceding ...{END}')
          clean(1)
          return True

        else:
          print(f'{RED}ERROR: {END}Password isnt valid')

      else:
        print(f'{RED}ERROR: {END}{WHITE}This user doesnt exist{END}')

  except:
    print('Doesnt exists users!')
    clean(.5)

def register():
  temp_file = None
  exist = False
  try:
    # Read JSON
    with open(FILE) as file:
      name = input('Enter your new username: ')
      passwd = getpass(prompt='Enter your new password: ')
      confirm = getpass(prompt='Enter your password again: ')

      db = json.load(file)

      for x in range(0, len(db)):
        if name in db[x]['name']:
          exist = True
          break

        else:
          exist = False

      if exist:
        clean()
        print(f'{RED}ERROR: {END}{WHITE}This user already exist{END}')
        return(0)

      else:
        path = input('Please enter your path ("/", "/home", "/home/username/.folder"): ')
        if passwd == confirm:
          newuser = {'name': name, 'password': passwd, 'path': path}
          db.append(newuser)
      
      temp_file = db
    
    # Write new object
    with open(FILE, 'w') as file:
      json.dump(temp_file, file, indent=2)

  except Exception as exc:
    print(exc)


  print(f'{L_GREEN}Register:{END} The user has been {L_CYAN}added{END}')

