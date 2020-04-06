X, Y, Z = map(int, input().split())

tmp1 = X
X = Y
Y = tmp1

tmp2 = X
X = Z
Z = tmp2

print('{0} {1} {2}'.format(X, Y, Z))