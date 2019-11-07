import random


def main():

    madrih = [["naom daniel"], ["shahar itay"], ["maya gili"], ["ben kish lasko"], ["roni shely"], ["romi hakak"], ["inbal shmoel"], ["hila tamir"]]
    hanih = raw_input("write name and at the end print 999\n")
    x = []
    while hanih != "999":
        x.append(hanih)
        hanih = raw_input("write name and at the end print 999\n")
    c = int(raw_input("how many hanihim in a group\n"))
    print x
    c += 1
    for k in x:
        p = random.randint(0, 7)
        if len(madrih[p]) == c:
            while True:
                p = random.randint(0, 8)
                if len(madrih[p]) < c:
                    madrih[p].append(k)

                    break
        else:
            madrih[p].append(k)
    for t in madrih:
        print t
        print "\n"





if __name__ == '__main__':
    main()