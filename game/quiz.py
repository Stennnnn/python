import sys

print(r"""\     
─────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████─██████──────────██████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████████──██░░██─
─██░░██████████─██████░░██████─██░░██████████─██░░░░░░░░░░██──██░░██─
─██░░██████████─────██░░██─────██░░██████████─██░░██──██░░██──██░░██─
─██░░░░░░░░░░██─────██░░██─────██░░░░░░░░░░██─██░░██──██░░██──██░░██─
─██████████░░██─────██░░██─────██░░██████████─██░░██──██░░██──██░░██─
─────────██░░██─────██░░██─────██░░██─────────██░░██──██░░██████░░██─
─██████████░░██─────██░░██─────██░░██████████─██░░██──██░░░░░░░░░░██─
─██░░░░░░░░░░██─────██░░██─────██░░░░░░░░░░██─██░░██──██████████░░██─
─██████████████─────██████─────██████████████─██████──────────██████─
─────────────────────────────────────────────────────────────────────
                """)

print("Welkom bij mijn computer quiz!")
play = input("Wil je een spel spelen? 'yes' of 'no' ")


if play != "yes":
    print("Jammer ;C")
    input("Druk op ENTER om af te sluiten ")
    quit()
    

print("Laten we beginnen! :D")

print("===============================")

cor = "a"
inc = "b"
inc1 = "c"
print("a. central processing unit")
print("b. central power unit")
print("c. central program unit")
answer = input("vraag 1. Wat is een CPU? ")
if answer == "a":
    print("Correct!")
else:
    print("Incorrect! Het antwoord was 'A'")
    
print("===============================")

inc = "a"
inc2 = "b"
cor = "c"
print("a. SCSI")
print("b. PCI")
print("c. PCIE")
answer = input("vraag 2. Hoe heet de verbinding waarmee het moederbord verbinding heeft met expansion kaarten? ")
if answer == "c":
    print("Correct!")
else:
    print("Incorrect! Het antwoord was 'C'")

print("===============================")
 
inc = "a"
inc2 = "b"
cor = "c"
print("a. SCSI")
print("b. PCI")
print("c. PCIE")
answer = input("vraag 3.  ")
if answer == "c":
    print("Correct!")
else:
    print("Incorrect! Het antwoord was 'C'")

print("===============================")
