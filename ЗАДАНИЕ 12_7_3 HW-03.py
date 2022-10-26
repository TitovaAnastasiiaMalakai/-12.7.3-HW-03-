per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада:"))
TKB = int(5.6 * money/100)
SKB = int(5.9 * money/100)
VTB = int(4.28 * money/100)
SBER = int(4.0 * (money/100))
deposit = {'ТКБ': TKB, 'СКБ': SKB, 'ВТБ': VTB, 'СБЕР': SBER}
print("Ваши накопления за год для сравнения:", deposit)
deposit = [TKB, SKB, VTB, SBER]
print("Максимальная сумма, которую вы можете заработать:", max(deposit))
