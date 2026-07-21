# Product of Two Matrices

r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    a = []
    b = []
    c = []

    print("Enter first matrix:")
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input()))
        a.append(row)

    print("Enter second matrix:")
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input()))
        b.append(row)

    for i in range(r1):
        row = []
        for j in range(c2):
            total = 0
            for k in range(c1):
                total += a[i][k] * b[k][j]
            row.append(total)
        c.append(row)

    print("Product Matrix:")
    for row in c:
        print(row)