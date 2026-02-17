def greeting():
    """
    Prints out a bunch of greetings in various languages
    :return: The greeting string
    """
    print("Hello")
    print("Hola")
    print("Bonjour")
    print("Hallo")
    print("Privet")
    print("Ni hao")
    print("Ciao")

def greeting2(name):
    """
    Prints out a bunch of greetings in various languages
    :param name: the name of the erson to greet
    :return:
    """
    message = ""
    message += "Hello"
    print("Hello")
    print("Hola")
    print("Bonjour")
    print("Hallo")
    print("Privet")
    print("Ni hao")
    print("Ciao")

    def greeting3(name):
        """
        Prints out a bunch of greetings in various languages
        :param name: the name of the erson to greet
        :return:
        """
        message = ""
        message += "Hello"
        return message

for i in range(10):
    greeting()
print("I can take a break")
for i in range(5):
    greeting2("Lukas")


print(greeting3("bob").replace("bob", "billybob").upper())