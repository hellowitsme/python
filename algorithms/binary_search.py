# 二分探索
# 探索範囲を半分に分ける
# 線形探索に比べて処理時間が短くなる
# 事前にソートが必要

def binary(value):
    # 数値を格納
    numbers = []
    for i in range(1, 22):
        numbers.append(i)
    
    left = 0    # 左端
    right = len(numbers) - 1 # 右端
    while left <= right:
        mid = (left + right) // 2    # 中央値
        if numbers[mid] == value:
            return mid
        elif value > numbers[mid]:
            # valueが中央値以上だったら、左端の位置を変更
            left = mid + 1
        else:
            # valueが中央値以下だったら、右端の位置を変更
            right = mid - 1
    return "Nothing"       # 見つからなかった場合
print(binary(13))