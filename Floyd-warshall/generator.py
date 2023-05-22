import random
import csv
import configparser


config = configparser.ConfigParser()
config.read("cfg.ini")

class generator:
    def __init__(self):
        self.N = int(config["settings"]["top"])
        self.sv = int(config["settings"]["max"])
        self.file = config["settings"]["filename"]
        self.ves = int(config["settings"]["weight"])

    @staticmethod
    def printf2(file,massiv):
        dictlist = []
        outfile = open('{}.csv'.format(file), 'w', newline='')
        writer = csv.writer(outfile, delimiter=';', quotechar='"')
        for i in range(len(massiv)):
            for key, value in massiv[i].items():
                dictlist.append(key)
                dictlist.append(value)
            j = 0
            writer.writerow(dictlist)
            j += 1
            dictlist.clear()
        outfile.close()
    print('Записываю сгенерированный граф')


    def g2(self):
        A = []
        B = list(range(self.N))
        massiv = []
        for i in range(self.N):
            massiv.append({})
        c = random.choice(B)
        B.remove(c)
        A.append(c)
        while (B != []):
            c = random.choice(B)
            d = random.choice(A)
            massiv[c][d] = random.randint(1, self.ves)
            B.remove(c)
            A.append(c)
        for i in range(self.N):
            if len(massiv[i]) != 0:
                rand = random.randint(1, (self.sv - 1))
            else:
                rand = random.randint(1, self.sv)
            for j in range(rand):
                massiv[i][random.randint(1, self.N - 1)] = random.randint(1, self.ves)
        generator.printf2(self.file, massiv)



generator().g2()