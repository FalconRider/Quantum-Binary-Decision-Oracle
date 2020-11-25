# FOR AMUSEMENT ONLY - based on Dwaves antenna model

#The ORACLE Api - DECISION SUPPORT PROOF APP                  VERIFER
#                       P.Gitschner 2020

print("")
print("")

print("----------------------------------------------------------VERIFYER --")

print("  The QUANTUM ORACLE - A DECISION INDEPENDANCE SUPPORT PROOF ")
print("---------------------------------------------------------------------")
print("")
print("VERYFICATION  Requested    ")
print("")

title  = input("Decision in regards to :    ")
print("")

from hashlib import sha256



print(" ENTER THE 4 Componants of the Certification as on the Certificate ")
print("")
timestamp  = input("1   Timestamp with all decimal places   ")
print(" ")
Choice1  = input("2   Alternative One   ")
print("")
Choice2  = input("3   Alternative Two   ")
print("")

decision = input("4   Decision as returned by Quantum computer   ")
print(""      )
print(""      )
print(""      )
print(" ---for VERIFICATION,  you have entered  ")
print("  ")
print("AS to the Decision in regards to ", title)
print("  ")


print("Timestamp of the decision request as enterd ",timestamp)
print("  ")

print("WHERE AS Alternative One was  " ,Choice1)
print("")
print("AND Alternative Two was       ", Choice2) 
print("  ")


print("  ")
print("And the QUANTUM COMPUTER'S TRULY RANDOM INDEPENDANT DECISION was :  ",decision)
print(" ")
print ("------------------------------------------------------------------------- ")

hashbase = (str(Choice1)+str(Choice2) + str(decision)+str(timestamp ))
hash = (sha256(hashbase.encode('utf-8')).hexdigest())
#hash = sha256(hashbase)  testing

print("")
print("Cryptographic VERIFICATION should match Certification of Proof hash :")
print("")
print("   ", hash)
print(" ")
print ("------------------------------------------------------------------------- ")


