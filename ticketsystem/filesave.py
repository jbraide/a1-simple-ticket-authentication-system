from random_string_gen import usernameGenerator, passwordGenerator


def fileSave():

    f = open('usernamePassword.txt', 'w+')
    for i in range(100):
        f.write('%s, %s \n' % (usernameGenerator(),  passwordGenerator()))
    f.close()


if __name__ == '__main__':
    fileSave()
