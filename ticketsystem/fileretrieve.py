def fileRetrieve():
    f = open('usernamePassword.txt', 'r')
    listing = f.readlines()
    for i in listing:
        print i
    print listing


if __name__ == '__main__':
    fileRetrieve()
