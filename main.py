M = []
rows, columns = 0, 0

# Matrix looks like
# M = [[1 2 3],
#      [4 5 6]]

def createMatrix():
    global rows, columns

    print("Enter the number of rows: ")
    rows = int(input())

    print("Enter the number of columns")
    columns = int(input())

    for row in range(rows):
        M.append([])
        for column in range(columns):
            print(f"Add a number for spot row {row + 1} : column {column + 1}")
            M[row].append(int(input()))

def testMatrix():
    global rows, columns
    rows, columns = 3, 3
    i=1
    for row in range(rows):
        M.append([])
        for column in range(columns):
            M[row].append(i)
            i += 1

def printMatrix():
    for row in range(rows):
        print("[ ", end='')
        for column in range(columns):
            print(f"{M[row][column]} ", end='')
        print("]")

def REF():
    column = 0
    row = 0
    while column < columns:
        printMatrix()
        print()

        pivot = M[row][column]
        for c in range(column, columns): # eg. 1/a1 R1 -> R1
            M[row][c] = M[row][c] / pivot

        for r in range(row + 1, rows):
            constant = -M[r][column] / M[row][column]
            for c in range(column, columns):
                M[r][c] = M[r][c] + constant * M[row][c]

        column+=1
        row+=1

def REFtoRREF():
    column = 1
    row = 1
    while column < columns:
        printMatrix()
        print()

        if (rows == 1 or columns == 1):
            break

        for r, row_data in enumerate(M[:row]):
            constant = M[r][column]
            for c in range(column, columns):
                M[r][c] = M[r][c] - constant * M[row][c]
        column+=1
        row+=1







def main():
    while True:
        user_input = input("Enter a command (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        try:
            # Evaluate the user input as Python code
            eval(user_input, globals(), locals())
        except Exception as e:
            print(f"Error: {e}")

main()