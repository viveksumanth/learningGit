
class Operations:

    def __init__(self):
        self.c = 5
        self.d = 5

    def mul(self):
        #branch1-Changes are here
        self.c += 1
        self.d += 1
        return self.c*self.d

    def div(self):
        #branch2-Changes are here
        self.x += 1
        self.y += 1
        return self.x//self.y

if __name__ == "__main__":

    opr = Operations()
    aDiv = opr.div()
    aMul = opr.mul()
    print(aDiv)
    print(aMul)

    