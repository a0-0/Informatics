def convert():
    f = open("Парсинг.json", encoding="utf8")
    text = f.read()
    f.close()

    writing = False
    element = True

    result = {}
    realResult = ""
    keys = []
    longest = 0
    elementName = ""
    value = ""

    for i in text:
        if writing:
            if i == '"':
                writing = not writing
                if not element:
                    result[elementName].append(value)
                    if len(result[elementName]) > longest:
                        longest = len(result[elementName])
                    elementName = ""
                else:
                    if elementName not in result:
                        result[elementName] = []
                        keys.append(elementName)
                    value = ""
                element = not element
                continue
            if not element:
                value += i
            else:
                elementName += i
        else:
            if i == '"':
                writing = True
            elif i == "{":
                element = True
                elementName = ""

    realResult = "\t".join(keys) + "\n"
    for i in range(longest):
        for key in keys:
            if i < len(result[key]):
                realResult += result[key][i]
            realResult += "\t"
        realResult += "\n"

    f = open("resultWithTsv.tsv", mode="w", encoding="utf8")
    f.write(realResult)
    f.close()


if __name__ == '__main__':
    convert()
