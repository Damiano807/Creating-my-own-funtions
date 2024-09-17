
n=int(input ("Digite um número :"))
n2=n
n
binario=list()
#binario.append(1)
if n>0 and n!=1:
    q=n/2

    while True:

        resto=n%2
        binario.append(resto)
        n = n // 2
        if n== 1:
            binario.append(1)
            break
        #print(binario)
    binario2=list()
    p=len(binario)-1
    for i in range(p,-1,-1):
        binario2.append(binario[i])
    print(f" O número {n} em binário é :",end="")
    for i in binario2:
        print(i,end="")
if n2==1:
    print(f"O número {n2} em binário é 01 ",end="")
elif n2==0:
    print(f"O número 0 em binário é 0")
print()


