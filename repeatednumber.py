from collections import Counter
list_of_integers = [2, 1, 0, 2, 5, 0, 4, 2, 4, 2, 5, 1, 3, 2]
cnt = Counter(list_of_integers)
print(cnt.most_common(3))
