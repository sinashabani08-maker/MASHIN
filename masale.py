#coded N332 《■》KINGHacker《■》

#color's
GREEN = '\033[1;32m'
RED = '\033[1;31m'
RESET = '\033[0m'

#Help
print (f'''\n{RED}
      		=== Textbook Problem Solver 📘 ===
	    	Enter the person's name: John
		Enter the item (e.g., apple, pencil...):
		apple
		Enter the initial number of apples (F): 5
		Enter the number of apples that 
		changed(E): 2
		Operation (add ➕ / subtract ➖ /
		 multiply✖️ / divide ➗): subtract
		Enter time or context (optional): 10 AM

		📘 Problem Solution:
		John now has 3 apple(s).
		(This happened at 10 AM)
''')
print (f'''\n {GREEN}



''')
print('''

██████╗ ██████╗  ██████╗ ██╗     ███████╗███╗   ███╗
██╔══██╗██╔══██╗██╔═══██╗██║     ██╔════╝████╗ ████║
██████╔╝██████╔╝██║   ██║██║     █████╗  ██╔████╔██║
██╔═══╝ ██╔══██╗██║   ██║██║     ██╔══╝  ██║╚██╔╝██║
██║     ██║  ██║╚██████╔╝███████╗███████╗██║ ╚═╝ ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝     ╚═╝
     		《■》KINGHacker《■》
''')

# Get basic inputs from the user
name = input("Enter the person's name: ")
item = input("Enter the item (e.g., apple, pencil...): ")

F = float(input(f"Enter the initial number of {item}s (F): "))
E = float(input(f"Enter the number of {item}s that changed (E): "))

# Type of operation
operation = input("Operation (add ➕ / subtract ➖ / multiply ✖️ / divide ➗): ").strip()

# Optional time or context
H = input("Enter time or context (optional): ")

# Perform calculation based on chosen operation
if operation.lower() in ["add", "+", "➕"]:
    result = F + E
elif operation.lower() in ["subtract", "-", "➖"]:
    result = F - E
elif operation.lower() in ["multiply", "*", "✖️"]:
    result = F * E
elif operation.lower() in ["divide", "/", "➗"]:
    result = F / E if E != 0 else "Impossible (division by zero)"
else:
    result = "Invalid operation!"

# Display the result
print("\n📘 Problem Solution:")
if isinstance(result, (int, float)):
    print(f"{name} now has {result} {item}(s).")
else:
    print(result)

if H:
    print(f"(This happened at {H})")