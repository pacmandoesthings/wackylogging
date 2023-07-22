# github.com/pacmandoesthings
# pacman's wacky logging lib

from colorama import *
init()

def Info(text):
  print(f"{Back.CYAN}{Fore.WHITE} INFO {Back.RESET}{Fore.RESET} {text}")
  
def Success(text):
  print(f"{Back.GREEN}{Fore.WHITE} SUCCESS {Back.RESET}{Fore.RESET} {text}")
  
def Error(text):
  print(f"{Back.RED}{Fore.WHITE} ERROR {Back.RESET}{Fore.RESET} {text}")
  
def Warn(text):
  # let the intrusive thoughts in, make it say "warm"
  print(f"{Back.YELLOW}{Fore.WHITE} WARN {Back.RESET}{Fore.RESET} {text}")