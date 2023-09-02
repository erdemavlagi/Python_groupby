
range(len("string"))

def alterneting(string):
    new_string = ""

    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()
    print(new_string)


def buyult(string):
    net_string= ""

    for i in range(len(string)):
        net_string += string[i].upper()

    print(net_string)




 buyult("erdemavlaği")