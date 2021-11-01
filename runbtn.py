import glob
imports = glob.glob("*.py")
imports.remove('runbtn.py')
modules = []
i = 0
for x in imports:
  i += 1
  print(f"{i-1}. {x}")
userInput = int(input("Chose program (index number): "))
try:
  print("========== Beginning Runtime ==========", end = '\n\n')
  modules.append(__import__(imports[userInput]))
  print(f"Successfully imported {imports[userInput]}")
except ImportError:
  print(f"\n\n ========== End of Runtime =========== \n Post Scriptum: Computer go wonk, {imports[userInput]} may have problems during runtime.")