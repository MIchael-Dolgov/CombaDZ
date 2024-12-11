def build_inversion_table_from_left(vector):
    n = len(vector)
    inversion_table = [0] * n
    for i in range(1, n):
        inversion_table[i] = sum(1 for j in range(i) if vector[j] > vector[i])
    return inversion_table

def restore_from_inversion_table_from_left(inversion_table):
    n = len(inversion_table)
    result = []
    for i in range(n):
        position = i - inversion_table[i]
        result.insert(position, i + 1)
    return result


#Восстановление перестановки из вектора инверсий происходит с точностью до порядка элементов
#Если вектор инверсий задан корректно, то восстановление перестановки происходит однозначно.
if __name__ == "__main__":
    original_vector = [5, 4, 1, 3, 2, 6, 7]
    print("Исходный вектор:", original_vector)

    inversion_table = build_inversion_table_from_left(original_vector)
    print("Таблица инверсий:", inversion_table)

    restored_vector = restore_from_inversion_table_from_left(inversion_table)
    print("Восстановленный вектор:", restored_vector)