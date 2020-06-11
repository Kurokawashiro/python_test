
def fizzbuzz(file_str = './input.txt'):
    f = open(file_str)
    res = []
    for x in f:
        res.append(x)
    f.close()

    seq = []
    for i in res:
        if ':' in i:
            a = i.split(':')
            b = a[1].split('\n')
            seq.append((int(a[0]),b[0]))
        else:
            m = int(i.split('\n')[0])

    seq.sort()

    res_str = ""
    for t in seq:
        if m%t[0]==0:
            res_str+=t[1]
    if res_str=="":
        res_str = m

    print(res_str)
    return res_str
fizzbuzz()
