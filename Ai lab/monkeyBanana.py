import random
class C:
    def __init__(self,B):
        self.B=B
    def __repr__(self):
        return "Monkey with %d bananas"%self.B
M=[C(random.randint(0,50)) for i in range(5)]
print ("Random Monkeys:")
print (M)
def NOB(monkey):
    return monkey.B
print ("Number of bananas (First Monkey):", NOB(M[0]))
MM=max(M,key=NOB)
print ("Max Monkey:",MM)