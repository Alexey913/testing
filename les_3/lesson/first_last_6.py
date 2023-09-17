# Разработайте тесты для метода firstLast6, где на вход подается массив чисел, а метод
# возвращает true, если первое или последнее число в массиве равно 6, иначе false.

def first_last_6(numbers: list[int]) -> bool:
    if numbers[0] == 6 or numbers[-1] == 6:
        return True
    return False

if __name__ == "__main__":
    nums = [5, 5, 10, 8, 6]
    print(first_last_6(nums))