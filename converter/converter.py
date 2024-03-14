from converter_values import *

print(options["help"])
res = input("Response: ")


while res.lower() != "q":
    res = res.strip().split(" ")

    try:
        if len(res) == 1:
            print(options[res[0]])

        elif len(res) == 4:
            for i in res[3].split(','):
                value = round(eval( "{} * {}['{}'] / {}['{}']".format(res[2],res[0],i,res[0],res[1]) ), 6)
                print("{} \t : {}".format(i,value))

        else:
            print("Invalid command")

    except:
        print("Invalid command")

    res = input("\nResponse: ")
