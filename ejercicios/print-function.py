# if __name__ == '__main__':
#     print(*range(1, int(input())+1), sep='')

if __name__ == '__main__':
    n = int(input())
    result = ""
    for numero in range(1, n+1):
        result += str(numero)

    print(result)
