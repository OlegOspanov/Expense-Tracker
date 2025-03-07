
l = ['a',11,'b', 12, 13, 14]
def filter_list(l):
    a = [i for i in l if type(i) == int]
    print(a)

if __name__ == '__main__':
    filter_list(l)