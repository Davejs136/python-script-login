import json
from os import system
from .variables import DEFAULT, FILE


# -------------------------    FUNCTIONS   ------------------------- #

def setDefault():
  try:
    with open(FILE, 'r+') as file:
      if not file.read():
        json.dump(DEFAULT, file, indent=2)

  except FileNotFoundError as notFound:
    # Create el file
    system(f'touch {FILE}')
    setDefault()


def clean(time=0):
  system(f'sleep {time} && clear')