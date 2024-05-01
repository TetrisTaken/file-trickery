def swapFileData():
    file1 = input("Enter the name of the first file: ")
    file2 = input("Enter the name of the second file: ")
    with open(file1, 'r') as a:
        data_a=a.read()
    with open(file1, 'w') as b:
        a.write(data_a)

swapFileData()
