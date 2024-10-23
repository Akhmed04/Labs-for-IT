numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_ = 0

for i in numbers:
    if (i == None):
        continue
    sum_ += i
avr = (sum_/len(numbers))

new_numbers = [ avr if el is None else el for el in numbers]

print("Измененный список:", new_numbers)
