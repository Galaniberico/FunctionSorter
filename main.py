class function:

    def __init__(self, t):
        self.text = t
        self.name = self.getName(t)

    def getName(self, t):
        id = t.index('(')
        foundname = False
        ss = ''
        for i in range(id-1,-1, -1):
            if t[i] == '*' or t[i] == '&' or t[i] == ' ':
                if not foundname:
                    continue
                ss = t[i:id]
                break
            else:
                foundname = True
        return ss

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return self.name

def main():
    file = open("./aordenar.txt")
    functions = []
    aux = ''
    for l in file:
        if l == '\n' or l == '    \n':
            continue
        aux += l
        if (aux == '' and (l.endswith(';\n') or l.endswith(';'))) or (aux != '' and (l.endswith('}\n') or l.endswith('}')) and aux.count('{') == aux.count('}')):
            func = function(aux)
            functions.append(func)
            aux = ''
    functions.sort()
    file.close()
    file = open("./ordenao.txt", "w")
    for f in functions:
        file.write(f.text + '\n')
    file.close()









if __name__ == '__main__':
    main()
