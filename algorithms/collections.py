def count(chara):
    count = {}
    for i in chara:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)

count("Google")