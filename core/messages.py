from .variables import D_GRAY, END

# -------------------------    MESSAGES   ------------------------- #

def main_message():
  print('')
  print('                RUNNING SCRIPT            ')
  print('')
  print('** MENU **')
  print('=============================================')
  print('Select an option:')
  print('')
  print('1) Login')
  print('2) Register')
  print('3) About')
  print('4) Help')
  print('')
  print('0) Exit')
  print('─────────────────────────────────────────────')

def login_message():
  print('')
  print('                PRIVATE FILES           ')
  print('')
  print('───> SCRIPT MENU ')
  print(f'{D_GRAY}============================================={END}')
  print('Select an option:')
  print('')
  print('1) Create Folder')
  print('2) Create File')
  print('3) Delete Folder')
  print('4) Delete File')
  print('')
  print('0) Exit')
  print(f'{D_GRAY}============================================={END}')