def power(A,B):
    if B>0:
        return A*power(A,B-1)
    else:
        if B<0:
            print("Мы так не договаривались, введите положительную степень")
            return 0
        else:
            return 1

try:
    A = int(input("Введите число А: "))
    B = int(input("Введите число B: "))
    res = power(A,B)
    print(res)
except:
    print("Что-то пошло не так")