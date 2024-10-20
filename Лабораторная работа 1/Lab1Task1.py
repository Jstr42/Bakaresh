numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]



s = sum([num for num in numbers if num is not None])


l = len(numbers)

a = s / l

numbers = [a if num is None else num for num in numbers]





# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)