#coded N289 《■》KINGHacker《■》

#modluse of script
import subprocess
#banner of script
subprocess.run(["python", "banner2.py"])
#color's
green = '\033[1;32m'
red = '\033[1;31m'
reset = '\033[0m'
yellow = '\033[0;93m'

#menu
subprocess.run(["python", "banner3.py"])

print ('''



''')
MK = int(input(f'\n{yellow}>---Your Dastor------》'))

if MK ==1:
#mashin sade
      subprocess.run(["python", "mashin1.py"])
 
elif MK ==2:
#masale
	  subprocess.run(["python", "masale.py"])
	
elif MK ==3:
#Abut
	  subprocess.run(["python", "Abot.py"])
	  
else:
	print(f'''\n{green}
	     (\_/)             
             (o_o)            
            <)   )╯           
              ___
             /   \            

  ##################################
  #                                #
  #          NOT DASTOR            #
  #                                #
  ##################################
  ''')
  

