# 選択ソート
# リストの中から最も小さい要素を選んで、前に移動する

numbers = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(len(numbers)):
    min = i # ←最小値の位置をセット
    for j in range(i + 1, len(numbers)):
        if numbers[min] > numbers[j]:
            min = j # ←最小値が更新されたらその位置をセット

    # 最小値の位置と現在の要素を交換
    numbers[i], numbers[min] = numbers[min], numbers[i]

print(numbers)