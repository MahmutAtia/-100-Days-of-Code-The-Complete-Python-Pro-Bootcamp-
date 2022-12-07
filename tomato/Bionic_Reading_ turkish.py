import fontstyle
import math
text = "Benim a aa ismim mahmoud atia"
voles = ['A', 'E', 'I', 'I', 'O', 'Ö', 'U', 'Ü', 'a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']

words = text.split()

def bionic(word):
    index = math.floor(len(word)/2)
    bold = fontstyle.apply(word[:index], "BOLD")
    normal = word[index:]
    str = bold + normal + " "

    return  str





with open("bionic.docs" , "a") as f:
       f.write('{\\bmamo\\b0}')
