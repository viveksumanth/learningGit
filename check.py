
class Operations:

    def __init__(self):
        self.c = 5
        self.d = 5

    def mul(self):

        self.c += 1
        self.d += 1
        return self.c*self.d

    def div(self):

        self.a += 1
        self.b += 1
        return self.a//self.b

if __name__ == "__main__":

    opr = Operations()
    aDiv = opr.div()
    aMul = opr.mul()
    print(aDiv)
    print(aMul)

    