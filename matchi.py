print('Введите количество строк N:')
N=int(input())
matrix=list()
count=int()
#заполнение
for i in range(N):
    vrm=list()
    for j in range(2):
        vrm.append(int(input()))
    matrix.append(vrm)
#просмотр
for i in range(N):
    for j in range(2):
        print(matrix[i][j],end=' ')
    print()
print(matrix)
print()
for i in range(N):
    kom=list()
    kom=matrix[i]#0
    print(kom)
    x=matrix[i][1]#2
    for i in range(N):
        if matrix[i]!=kom:#1 [2,4]
            print(matrix[i],end=' ')
            if x==matrix[i][0]:#2
                count+=1
    print()
print(count)