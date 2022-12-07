from cipher import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#encode(message,shift)
def encode(message , shift ):
    result = ""

    for n in message:
        if n not in alphabet:
            result += n
        else:
            index = alphabet.index(n)
            index = index + shift
            if index >= 26:
                index=index%26
            result += alphabet[index]
    print(result)
    return result


def decode(message , shift):
    result = ""
    for n in message:
        if n not in alphabet:
            result += n
        else:
            index = alphabet.index(n)
            index = index - shift
            if index <= 0:
                index=(-index)%26
            result += alphabet[index]
    print(result)
    return result
app = "yes"
while app == "yes" :
    print(logo)
    func = input("enter encode or decode")
    message = input("enter a message")
    shift = int(input("how many numbers to shift"))
    if func == "encode":
        encode(message, shift)
    if func == "decode":
        decode(message, shift)

    app = input("do you want to start again yes or no ")