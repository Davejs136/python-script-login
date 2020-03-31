from .helpers import clean
from .variables import RED, END

# -------------------------    FUNCTIONS   ------------------------- #

def dashboard():
  while True:
    try:
      login_message() # message
      option = int(input('Select option: '))

      if option == 0:
        clean()
        print('Logout success')
        return
    except:
      print(f'{RED}Character invalid!{END}')
      clean(.5)