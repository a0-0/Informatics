def newLine(result, depth, isList=False):
    if not isList:
        result += "\n" + "  " * depth
    else:
        result += "\n" + "  " * (depth - 1) + "- "
    return result


def convert():
    f = open("Парсинг.json", encoding="utf8")
    text = f.read()
    f.close()

    writing = False
    element = True
    inList = False
    depth = -1

    result = ""

    for i in text:
        if writing:
            if i == '"':
                writing = not writing
                if not element:
                    result = newLine(result, depth)
                else:
                    result += ": "
                element = not element
                continue
            result += i
        else:
            if i == '"':
                writing = True
            elif i == "{":
                depth += 1
                element = True
                if inList:
                    result = newLine(result, depth, True)
            elif i == "}":
                depth -= 1
            elif i == "[":
                inList = True
            elif i == "]":
                inList = False

    f = open("resultWithCode.yml", mode="w", encoding="utf8")
    f.write(result)
    f.close()


if __name__ == '__main__':
    convert()
