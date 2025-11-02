lists = {'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m','A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S','G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z','N':'A','O':'B','P':'C','Q':'D','R':'E','S':'F','T':'G','U':'H','V':'I','W':'J','X':'K','Y':'L','Z':'M'}
def ASCI_string(string):
    result = ""
    for char in string:
        if char in lists:
            result += lists[char]
        else:
            result += char
    return result

def main():
    input_string=input("enter")
    output_string=ASCI_string(input_string)
    print("the converted string is:",output_string)
if __name__ == "__main__":
    main()
