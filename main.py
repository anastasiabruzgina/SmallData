def rot(num):
    a = int(str(num).replace('6', '9', 1))
    return a

if __name__ == '__main__':
    num = int(input())
    print(rot(num))

