from pymeta import *


@debug
def add(num1,num2):
    return num1+num2


@debug(prefix="***")
def sub(num1,num2):
    return num2-num1

# print(sub(5,10))
# print(add(5,10))


@elementvalues
@debugclass
class ClassMeta:
    def a(self):
        pass

    def b(self,b):
        # pass
        print("b is = %r" % b)


cm = ClassMeta()


# print(cm.a())
print(cm.b(5))
