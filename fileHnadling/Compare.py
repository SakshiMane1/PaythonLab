with open("file1.txt", "r") as file1:
    lines1 = file1.readlines()

with open("file2.txt", "r") as file2:
    lines2 = file2.readlines()

if lines1 == lines2:

    print("Both files are identical.")

else:

    print("Files are different.")

    min_length = min(len(lines1), len(lines2))

    for i in range(min_length):

        if lines1[i] != lines2[i]:

            print("First difference at line:", i + 1)
            print("File 1:", lines1[i].strip())
            print("File 2:", lines2[i].strip())
            break
    else:

        print("Difference because one file has extra lines.")