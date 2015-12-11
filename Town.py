__author__ = 'jeshon.assuncao'

class Town :
    def __init__(self, name):
      self.name = name

    #def final(self, history, connections):
    #   for connection in connections:
     #       if(connection["A"] == self.name and connection["B"] not in history):
     #           return False;
     #       elif(connection["B"] == self.name and connection["A"] not in history):
     #           return False;
     #   return True

    def final(self, history, townB):
        if(townB in history):
            return True
        else:
            return False

    def applicableOps(self, history, funcHeuristique, connections):
        ops = []

        for connection in connections:
            if(connection["A"] == self.name and connection["B"] not in history):
                    ops.append({"name" : connection["B"], "resultHeur" : funcHeuristique(self.name, connection["B"])})
            elif(connection["B"] == self.name and connection["A"] not in history):
                    ops.append({"name" : connection["A"], "resultHeur" : funcHeuristique(self.name, connection["A"])})
        return ops


    def legal(self, connections):
        for connection in connections:
            if(self.name in connection['A'] or self.name in connection['B']):
                return True

        return False

    def apply(self, op) :
        return Town(op)