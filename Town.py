__author__ = 'jeshon.assuncao & tom.rey'

class Town :
    def __init__(self, name, resultHeur=0):
        self.name = name
        self.resultHeur = resultHeur

    def __repr__(self):
        return ('name : ' + self.name + ' - h+g : ' + str(self.resultHeur))

    def final(self, history, townB):
        if(townB in history):
            return True
        else:
            return False

    def applicableOps(self, history, funcHeuristique, connections):
        ops = []

        for connection in connections:
            if(connection["A"] == self.name and connection["B"] not in history):
                    ops.append(Town(connection['B'], funcHeuristique(self.name, connection['B'])+ int(connection['Dist'])))
            elif(connection["B"] == self.name and connection["A"] not in history):
                    ops.append(Town(connection['A'], funcHeuristique(self.name, connection['A'])+ int(connection['Dist'])))
        return ops

    def legal(self, connections):
        for connection in connections:
            if(self.name in connection['A'] or self.name in connection['B']):
                return True

        return False

    def apply(self, op) :
        return Town(op)