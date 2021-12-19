import re


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
            x = re.findall('"', i)
            if len(x) > 0:
                writing = True
            elif i == "{":
                depth += 1
                element = True
                if inList:
                    result = newLine(result, depth, True)
            x1 = re.findall("}", i)
            if len(x1) > 0:
                depth -= 1
            elif i == "[":
                inList = True
            x3 = re.findall("]", i)
            if len(x3) > 0:
                inList = False

    f = open("resultWithRegulars.yml", mode="w", encoding="utf8")
    f.write(result)
    f.close()


xr = re.findall(__name__, '__main__')
if len(xr) > 0:
    convert()
