def sort_list(lst):
    first_element = lst[0]
    sorted_lst = sorted(lst[1:])  # сортируем все элементы кроме первого
    sorted_lst.insert(0, first_element)  # вставляем первый элемент в начало отсортированного списка
    return sorted_lst

N = 10
lst = [3, 1, 2, 5, 4, 7, 6, 9, 8, 10]
sorted_lst = sort_list(lst)
print(sorted_lst)