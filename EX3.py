i = input("Enter Step of Harmonic : ")
i = int(i)

def harmonic(i):
    if i == 0:
        return 0
    else:
        result = (1/(i+1)+harmonic(i-1))
        print(f"Limit = {i}  Value = {result}")
        return result
harmonic(i)