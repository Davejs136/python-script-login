#!/usr/bin/python3
# -*- coding: utf-8 -*-

from core.messages import main_message, login_message
from core.main import login, register
from core.dashboard import dashboard
from core.helpers import setDefault, clean

# =============================     MAIN    ================================ #

def main():
  isValid = False
  while True:
    try:
      main_message() if not isValid else login_message()
      option = int(input(f'{CYAN}>>> {END}'))

      if option == 1:
        if login():
          dashboard()  # access to functionalities

      elif option == 2:
        register() # Register

      elif option == 3:
        isValid = True # About

      elif option == 4:
        pass # Help

      elif option == 0:
        break
      
    except:
      print('Character invalid!')
      clean(.5)


# print(f'\n\n{CYAN}[{END}*{CYAN}]{END} Searching for PHP installation...')


if __name__ == "__main__":
  setDefault()
  main()