#Week 2 - Working with Variables
#Author: Tanner Cole

analyst_name = input("Enter your name: ")
system_name = input("Enter system hostname: ")
criticality = input("Enter criticality level (Low, Medium, High): ")

print("\n--- Asset Information ---")
print("Analyst:", analyst_name)
print("System:", system_name)
print("Criticality Level:", criticality)

risk_score = input("Enter the risk score for the asset (0-100): ")
print("Risk score entered:", risk_score)

risk_score = int(risk_score)
print("Numeric risk score:", risk_score)
print("Data type now:", type(risk_score))

if risk_score >= 8:
    print("[*] High-Risk Asset – prioritize review.")
elif risk_score >= 5:
    print("[!] Medium-Risk Asset – monitor closely.")
else:
    print("[+] Low-Risk Asset – standard monitoring.")

