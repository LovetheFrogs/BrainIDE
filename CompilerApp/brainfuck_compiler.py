# Brainfuck compiler.
def readCodeFile(path):
    file = open(path, "r")
    code = ""
    for line in file:
        newLine = line.rstrip()
        code += newLine

    file.close()

    return code


def codeReader(lang, code, pointer, input_data):
    i = 0
    out = ""
    pos_to_read = 0
    my_input = None
    input_data += 'ñ'
    while i < len(code):
        current = code[i]
        if current == '[':
            aux = i + 1
            aux2 = i + 1
            current = code[aux]
            while current != ']' or lang[pointer] != 0:
                if current == ']':
                    aux = aux2
                elif current == ',':
                    my_input = input_data[pos_to_read]
                    if pos_to_read + 1 < len(input_data):
                        pos_to_read += 1
                        if input_data[pos_to_read] == '\n' and pos_to_read + 1 < len(input_data):
                            pos_to_read += 1
                    pointer, lang, out = interpreter(lang, pointer, current, out, my_input)
                    aux += 1
                else:
                    pointer, lang, out = interpreter(lang, pointer, current, out, my_input)
                    aux += 1
                current = code[aux]
            i = aux
        elif current == ',':
            my_input = input_data[pos_to_read]
            if pos_to_read + 1 < len(input_data):
                pos_to_read += 1
                if input_data[pos_to_read] == '\n' and pos_to_read + 1 < len(input_data):
                    pos_to_read += 1
            pointer, lang, out = interpreter(lang, pointer, current, out, my_input)
        else:
            pointer, lang, out = interpreter(lang, pointer, current, out, my_input)

        i += 1

    return out


def interpreter(lang, pointer, current, out, input_data):
    if current == '<':
        pointer -= 1
    if current == '>':
        pointer += 1
    if current == '+':
        if lang[pointer] == 255:
            lang[pointer] = 0
        else:
            lang[pointer] += 1
    if current == '-':
        if lang[pointer] == 0:
            lang[pointer] = 255
        else:
            lang[pointer] -= 1
    if current == '.':
        out += (chr(lang[pointer]))
    if current == ',':
        if input_data != 'ñ':
            lang[pointer] = ord(input_data)

    return pointer, lang, out


def inicialize():
    lang = [0] * 30000
    pointer = 0
    # fileExtension = ".bf"

    return lang, pointer  # , fileExtension
