__auther_ = "daniel david"


def main():
    file1 = open(r'C:\Users\d2712\Desktop\ex.txt','r')
    file2 = open(r'C:\Users\d2712\Desktop\solution.txt', 'w')
    for line in file1:
        print(line)
        solution1 = input('solution?\n')

        file2.write(line + '=' + str(solution1) + '\n')
    file1.close()
    file2.close()
    file2 = open(r'C:\Users\d2712\Desktop\solution.txt', 'r')
    for line1 in file2:
        print(line1,)
    file2.close()

if __name__ == '__main__':
        main()