import time

print("""
 _____                      _____ _                      
| ____|__ _  __ _          |_   _(_)_ __ ___   ___ _ __  
|  _| / _` |/ _` |  _____    | | | | '_ ` _ \ / _ \ '__| 
| |__| (_| | (_| | |_____|   | | | | | | | | |  __/ |    
|_____\__, |\__, |           |_| |_|_| |_| |_|\___|_|    
      |___/ |___/                                        
""")

print("Ei-Timer Version 1.6")
print("Wie willst du dein Ei? \n Durchgebraten (1), Weich (2) oder Ultra-Soft (3) ?")

eingabe = input("Deine Wahl:")
if eingabe == "1":
    print("Dein Ei wird durchgebraten!")
    for i in range(600, -1, -1):
        print(f"Verbleibende Zeit: {i} Sekunden", end="\r")
        time.sleep(1)
    print("\nFertig, guten Appetit!")
elif eingabe == "2":
    print("Dein Ei wird weich!")
    for i in range(360, -1, -1):
        print(f"Verbleibende Zeit: {i} Sekunden", end="\r")
        time.sleep(1)
    print("\nFertig, guten Appetit!")
elif eingabe == "3":
    print("Dein Ei wird ultraweich!")
    for i in range(180, -1, -1):
        print(f"Verbleibende Zeit: {i} Sekunden", end="\r")
        time.sleep(1)
    print("\nFertig, guten Appetit!")
else:
    print("Ungültige Eingabe. Bitte wähle 1, 2 oder 3.")
         
         
         