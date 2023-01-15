A = int(input("Введите число А: "))
B = int(input("Введите число B: "))

def power(A,B):
    if B>0:
        return A*power(A,B-1)
    else:
        return 1

res = power(A,B)
print(res)