import random
import csv
import configparser


config = configparser.ConfigParser()
config.read("config.ini")
top = int(config["Graph"]["top"])
communicate = int(config["Graph"]['maximum_of _ertices'])
filename = config["Graph"]['filename']

res=[[]*1 for i in range(top)]
def create_file(filename, graff):
    file = open('{}.csv'.format(filename), 'w', newline='')
    write = csv.writer(file, delimiter = ',', quotechar = '"')
    i = 0
    for line in graff:
        write.writerow(line)
        i += 1
    file.close()


def graf_not_orient(top, communicate, filename):
    for i in range(top):
        d = [p * 1 for p in range(0, top)]
        d.remove(i)
        c = []
        k = random.randint(1, communicate)
        for j in range(len(res[i])):
            if res[i][j] in d:
                d.remove(res[i][j])
        if len(res[i]) < k:
            s = len(res[i])
            while s < k:
                if d == []:
                    break
                rand_edge = random.choice(d)
                if len(res[rand_edge]) == communicate:
                    d.remove(rand_edge)
                elif len(res[rand_edge]) < communicate:
                    res[i].append(rand_edge + 1)
                    res[rand_edge].append(i + 1)
                    d.remove(rand_edge)
                    s += 1
    create_file(filename, res)


graf_not_orient(top, communicate, filename)

