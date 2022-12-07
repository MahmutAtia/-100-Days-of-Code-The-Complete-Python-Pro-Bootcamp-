

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
func = input("enter encode or decode")
message = input("enter a message")
shift = int(input("how many numbers to shift"))
#encode(message,shift)
def encode(message , shift ):
    result = ""

    for n in message:

        for i in range(len(alphabet)):
            if n == alphabet[i]:
                x = i + shift
                if x >= 26 :
                    x = x-26
        result += alphabet[x]
    print(result)
    return result


def decode(message , shift):
    result = ""
    for n in message:

        for i in range(len(alphabet)):
            if n == alphabet[i]:
                x = i - shift
                if x >= 26:
                    x = x + 26
        result += alphabet[x]
    print(result)
    return result

if func == "encode" :
    encode(message, shift)
if func == "decode":
    decode(message,shift)