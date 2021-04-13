# Numpy
# データを読み込んだり、必要なデータだけを取り出すのに使う
import numpy

score = numpy.loadtxt('score.csv', delimiter=",") # csvファイルの読み込み
print(score)

