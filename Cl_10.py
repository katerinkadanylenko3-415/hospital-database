# decoration - фунції обгортки, що рошир функціональність без зміни коду

def simpleDecorator(func):
    print("Hello, i`m decorator !")
    def simpleWrapper():
        print("func start working")
        func()
        print("end working")

    return simpleWrapper



# @simpleDecorator
def sayHey():
    print("Welcome")

@simpleDecorator
def sayBye():
    print("Bye")



sayHey()

sayHeyPro = simpleDecorator(sayHey)

sayHeyPro()
sayBye()


def simpleDecorator3(func):
    print("Hello, i`m decorator 3!")
    def simpleWrapper(num1, num2):
        print("func start working")
        func(num1, num2)
        print("end working")

    return simpleWrapper


def simpleDecorator4(func):
    print("Hello, i`m decorator 4!")
    def simpleWrapper(num1, num2):
        print("func start working")
        result = func(num1, num2)
        print("end working")
        return result


    return simpleWrapper

@simpleDecorator4
def addNums(num1, num2):
    return num1 + num2

print(addNums(2, 2))

def calcmultiply(a, b):
    return a * b

# calcmultiplyPro = decoratingWithArg(calcmultiply)




def decoratorWrapper(argFordec):
    print(f"I have {argFordec}")

    def simpleDecorator5(func):
        print(f"Hello, i`m decorator 5 with args {argFordec}")

        def simpleWrapper(num1, num2):
            print("func start working")
            result = func(num1, num2)
            print("end working")
            return result

        return simpleWrapper

    return simpleDecorator5











