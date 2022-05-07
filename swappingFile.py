def swapFileData():
    file1 = open("sample1.txt")
    file2 = open("sample2.txt")

    data_a = str(file1.readlines())
    data_b = str(file2.readlines())


    file1 = open("sample1.txt", "w")
    file1.write(data_b)
    file1.close()
    
    file2 = open("sample2.txt", "w")
    file2.write(data_a)
    file2.close()

    print(data_a)
    print(data_b)

swapFileData()