def Diffie_Hellman(a, Xa, Xb, q):
    Ya = pow(a, Xa, q)
    Yb = pow(a, Xb, q)
    print(f"Exchange Values are:\nYa:\t{Ya}\nYb:\t{Yb}")
    
    Ka = pow(Yb, Xa, q)
    Kb = pow(Ya, Xb, q)
    
    return Ka, Kb

def compare_private_key(Ka, Kb):
    if Ka == Kb:
        print(f"Private keys are the same: {Ka}")
    else:
        print(f"Private keys don't match\nKa:\t{Ka}\nKb:\t{Kb}")

# Main execution
q = int(input("Enter the public number 'q': "))
a = int(input("Enter the public number alpha (a): "))

Xa = int(input("Enter the private key Xa: "))
Xb = int(input("Enter the private key Xb: "))

print(f"Public numbers are:\nq:\t{q}\na:\t{a}")
print(f"Private keys are:\nXa:\t{Xa}\nXb:\t{Xb}")

Ka, Kb = Diffie_Hellman(a, Xa, Xb, q)
compare_private_key(Ka, Kb) 
