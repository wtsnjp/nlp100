def cipher(text):
    code = ""
    for w in text:
        c = ord(w)
        if 96 < c < 123:
            c = 219 - c
        code += chr(c)
    return code

print(cipher("Hello world!"))
