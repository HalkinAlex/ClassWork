def second_min(elements):
    sorted_elements = sorted(set(elements))  # Видаляємо дублікати і сортуємо список
    if len(sorted_elements) < 2:
        raise ValueError("List must contain at least two unique elements")
    return sorted_elements[1]

# elements = [5, 1, 9, 0, 7]
elements = [5,1,9,0,7]

assert second_min(elements) == 1