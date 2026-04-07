#Week2 - Asset Reporting
#Author: Tanner Cole

analyst_name = input("Enter your name: ")
department = input("Enter your department: ")
hostname = input("Enter the system hostname: ")
criticality = input("Enter criticality level (Low, Medium, High): ")

risk_score = input("Enter the risk score for the asset (0-100): ")
risk_score = int(risk_score)

print("="*40)
print(" Cyber Defense - Asset Report ")
print("="*40)

print("Analyst Name:", analyst_name)
print("Department:", department)
print("System Hostname:", hostname)
print("Criticality Level:", criticality)
print("Risk Score:", risk_score)

if risk_score >= 8:
    print("[*] High-Risk Asset – prioritize review.")
elif risk_score >= 5:
    print("[!] Medium-Risk Asset – monitor closely.")
else:
    print("[+] Low-Risk Asset – standard monitoring.")

from datetime import datetime
print("Report Generated:", datetime.now())