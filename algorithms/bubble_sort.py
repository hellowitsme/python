# バブルソート
# リストの隣り合ったデータを比較して、大小の順序が違っているときは並べ替えていく

numbers = [7, 13, 5, 3, 24, 11, 55]

for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]: # 前の数値が大きい時
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j] # 並べ替え

print(numbers)