with open('NumberNew.txt', 'w', encoding='utf-8') as f_rus:
    with open('Number.txt', 'r', encoding='utf-8') as f:
        rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
        f_rus.write(str([line.replace(line.split()[0], rus.get(line.split()[0])) for line in f]))