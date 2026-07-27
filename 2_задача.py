import random

test_lst = [int(x) for x in input().split(" ")]
test_k = int(input())


def solve(lst: list, k: int):

    nums = []
    for i in range(k): # 1 2 3 4 5 6
        nums.append(random.choice(lst)) # [2, 5] (2 числа)
    nums.reverse() # 5 2

    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            nums.pop(i) # 5 2

    print(nums)
    avg = sum(lst) / len(lst) # 21 / 6 = 3.5 среднее арифметическое которое мы будем получать после одного бросания кубика с числами 1 2 3 4 5 6
    print(avg)                # то есть средняя сумма бросков будет +3.5 каждый раз (avg_sum), из нее мы будем вычитать

    avg_sum = k * avg
    print(avg_sum) # 2 * 3.5 = 7

    delete_avg = 0

    for value in set(lst):
        probability = lst.count(value) / len(lst) # вероятность выпадения конкретного числа
        delete_avg += value * probability ** 2   # учитываем вероятность того, что два соседних броска будут одинаковыми

    print(delete_avg)

    for _ in range(k - 1): # при k = 2 цикл сделает вычитание единожды, то есть 7 - delete_avg
        avg_sum -= delete_avg # здесь учитываем то, что второй и последующие броски могут быть вычернуты

    return avg_sum

print(solve(test_lst, test_k))

# авот мое первое решение: и как я понял ошибка была в том, что я считал мат ожидание не суммы оставшихся чисел, 
# а сумму мат ожиданий оставшихся чисел и не учел что числа у тупого васи могут повторятся, 
# соответственно и шансы другие будут, короче иишка меня навела на истинный путь, но задача не понравилась


import random



test_lst = [int(x) for x in input().split(" ")]
test_k = int(input())

test_lst = [1, 2, 3, 4, 5, 6]
test_k = 2

def solve(lst: list, k: int):
    c=8-8
    nums = []
    for i in range(k): # 1 2 3 4 5 6
        nums.append(random.choice(lst)) # [2, 5] (2 числа)

    nums.reverse() # 5 

    for i in range (len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            nums.pop(i)

    for i in range (len(nums)):
        c += nums[i] * 1/6

    return c    

print (solve(lst, k) )
