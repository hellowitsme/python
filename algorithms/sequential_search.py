# カードの山から１枚づつ確認し、違ったら次へ

def sequential(number, n):
    answer = "Nothing!"
    for i in number:
        if i == n:
            answer = "Answer Number was: " + str(i)
            break
    return answer


number = range(0, 101)
result = sequential(number, 72)
print(result)