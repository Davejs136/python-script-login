from os import system

message = """
WELCOME TO MY SCRIPT!!!

What options we have ?

1 --------------------> Login
2 --------------------> Register
3 --------------------> About
4 --------------------> Quit

Please enter a option:
"""

class Process:
  """ This class realize the necessary functions """
  def show_message(self):
    print(message)

  def run(self):
    self.show_message()
    while True:
      option = input('> ')

      if not option:
        system('clear')
        print('Enter option: ')

      elif option == '4':
        system('clear')
        print('Byee :)')
        break


process = Process()

process.run()