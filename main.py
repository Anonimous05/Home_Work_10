class Compleks:

    def __init__(self, justNum, mnim):
        self.justNum = justNum
        self.mnim = mnim

    def __add__(self, addCompleks):
        just = self.justNum + addCompleks.justNum
        mnim = self.mnim + addCompleks.mnim

        print(f"{just} + {mnim}i")
        return Compleks(just, mnim)

    def __sub__(self, subCompleks):
        just = self.justNum - subCompleks.justNum
        mnim = self.mnim - subCompleks.mnim

        if just < 0 and mnim > 0:
            print(f"({just}) - {mnim}i")
        elif mnim < 0 and just > 0:
            print(f"{just} - ({mnim})i")
        elif just < 0 and mnim < 0:
            print(f"({just}) - ({mnim})i")
        else:
            print(f"{just} - {mnim}i")

        return Compleks(just, mnim)

    def __mul__(self, mulCompleks):
        just1 = self.justNum * mulCompleks.justNum
        mnim1 = self.mnim * mulCompleks.mnim
        tot1 = just1 - mnim1

        just2 = self.justNum * mulCompleks.mnim
        mnim2 = self.mnim * mulCompleks.justNum
        tot2 = just2 + mnim2
        print(f"{tot1} + {tot2}i")
        return Compleks(tot1, tot2)


num1 = Compleks(4, 5)
num2 = Compleks(2, 4)
total = num1 - num2

