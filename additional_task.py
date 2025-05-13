def merge_k_lists(lists):
    if not lists:
        return []
    if len(lists)==1:
        return lists[0]
    mid = len(lists) // 2
    left_half = lists[:mid]
    right_half = lists[mid:]
    return merge(merge_k_lists(left_half), merge_k_lists(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def main():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print("Невідсортований список:", lists)
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)


if __name__ == "__main__":
    main()