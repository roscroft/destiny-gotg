with open("dict.txt", "r+") as f:
    with open("newdict.txt", "w+") as g:
        for line in f.readlines():
            l = line.split(" ")
            medal = l[1]
            medal = '"'+medal[:-1]+'",'
            newl = []
            newl.append(l[0])
            newl.append(medal)
            st = '"")\n'
            newl.append(st)
            news = " ".join(newl)
            g.write(news)
