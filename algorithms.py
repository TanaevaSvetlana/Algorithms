# Алгоритм Евклида (найти НОД натуральных чисел)
def Euclidean_algorithm(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print(max(a, b))
# Euclidean_algorithm(5, 10)


# Решето Эратосфена (вывести все простые числа до натурального числа n>2)
def sieve_of_Eratosthenes(n):
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for i in range(number * 2, n + 1, number):
                numbers[i-2] = 0
    print(*list(filter(lambda x: x != 0, numbers)))
# sieve_of_Eratosthenes(6)


# Сортировка пузырьком (O(n**2))
def bubble_sort(list_of_nums):
    fl = True
    while fl:
        fl = False
        for i in range(len(list_of_nums) - 1):
            if list_of_nums[i] > list_of_nums[i + 1]:
                list_of_nums[i], list_of_nums[i + 1] = list_of_nums[i + 1], list_of_nums[i]
                fl = True
# list_ = [5, 3, 1, 4, 2]
# bubble_sort(list_)
# print(list_)


# Сортировка кучей (O(n*logn))
def helper_function(list_of_nums, heap_size, root_index):   # вспомогательная функция
    largest = root_index   # корневой индекс - индекс наибольшего элемента
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and list_of_nums[left_child] > list_of_nums[largest]:
        largest = left_child

    if right_child < heap_size and list_of_nums[right_child] > list_of_nums[largest]:
        largest = right_child

    if largest != root_index:
        list_of_nums[root_index], list_of_nums[largest] = list_of_nums[largest], list_of_nums[root_index]
        helper_function(list_of_nums, heap_size, largest)


def heap_sort(list_of_nums):
    n = len(list_of_nums)

    for i in range(n, -1, -1):     # второй аргумент означает остановку алгоритма перед первым элементом списка
        helper_function(list_of_nums, n, i)

    for i in range(n - 1, 0, -1):
        list_of_nums[i], list_of_nums[0] = list_of_nums[0], list_of_nums[i]
        helper_function(list_of_nums, i, 0)
# random_list_of_nums = [5, 3, 1, 4, 2]
# heap_sort(random_list_of_nums)
# print(random_list_of_nums)
