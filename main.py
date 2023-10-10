def func_cow(arr, count_cow):
    arr.sort()
    final_number = 0
    number = 1
    current_stable_with_cow = arr[0]
    count_cow -= 1
    copy_count_cow = count_cow
    cow_arr = []

    while number != arr[-1]:
        if copy_count_cow == 0:
            final_number = number

        copy_count_cow = count_cow
        number += 1
        # print("number", number)
        i = 0

        for i, value in enumerate(arr[:-1]):
            if number <= arr[i + 1] - current_stable_with_cow:
                current_stable_with_cow = arr[i + 1]
                # print("current_stable_with_cow", current_stable_with_cow)
                cow_arr.append(current_stable_with_cow)
                # if len(cow_arr) == final_number+1:
                #     print("cow_arr", cow_arr)
                copy_count_cow -= 1
                if copy_count_cow == 0:
                    cow_arr.clear()
                    cow_arr.append(arr[0])
                    current_stable_with_cow = arr[0]
                    break

    print(final_number)
    return final_number


func_cow([1, 2, 3, 4, 5, 10, 30, 40, 60, 90], 4   )
func_cow([1, 2, 8, 4, 9], 3)
func_cow([2, 5, 7, 11, 15, 20], 3)
