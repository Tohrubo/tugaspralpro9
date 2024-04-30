handle = open("artikel.txt", "r")

handle_list = handle.readlines()
kata = []
for i in range(len(handle_list)):
    list_word = handle_list[i].split()
    for item in list_word:
        word = ''.join(j for j in item if j.isalpha())
        lword = word.lower()
        if lword not in kata:
            kata.append(lword)
print(kata)

handle.close()