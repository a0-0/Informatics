import yaml
import json


def convert():
    f = open("Парсинг.json", mode="r", encoding="utf8")
    text = json.loads(f.read())
    f.close()

    text1 = yaml.dump(text)

    f1 = open("resultWithLibrary.yml", mode="w", encoding="utf8")
    f1.write(text1)
    f1.close()


if __name__ == '__main__':
    convert()
