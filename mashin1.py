#coded N839 《■》KINGHacker《■》

#modluse of script
import time
import random
#color's
GREEN = '\033[1;32m'
RED = '\033[1;31m'
RESET = '\033[0m'
YELLOW = '\033[0;93m'

#banner of script
print (f'''\n {GREEN}

███    ███  █████  ███████ ██   ██ ██ ███    ██ 
████  ████ ██   ██ ██      ██   ██ ██ ████   ██ 
██ ████ ██ ███████ ███████ ███████ ██ ██ ██  ██ 
██  ██  ██ ██   ██      ██ ██   ██ ██ ██  ██ ██ 
██      ██ ██   ██ ███████ ██   ██ ██ ██   ████ 
				KINGHacker
''')
#Help
print (f'''\n {YELLOW}

>--------》(+) for addition 


>-------》(-) for subtraction


>------》(/) for subtraction


>-----》(*) for multiplication


>----》(**) for exponent



''')

#porsesh
n1 = int(input(f'\n {RED}>----------》Your number'))
n2 = int(input(f'\n {GREEN}>--------》Your number'))
op = input(f'\n {RED}>-------》Your variable')
result = 0

if op == '+':
	  result = n1 + n2
elif op == '*':
  	result = n1 * n2
elif op == '/':
	  result = n1/n2
elif op == '-':
	  result = n1-n2
elif op == '**':
	  result = n1**n2
	
print(f"result = {result}")