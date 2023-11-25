# For O(nlogn) Time complexity we use merge sort algo 
# --> because merge sort has a time complexity of O(nlogn),

input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB02\\task02_1_input.txt"
output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB02\\task02_1_output.txt"

def merge_sorted_ls(list1, list2):
    result = []
    pt01 = 0
    pt02 = 0

    while pt01 < len(list1) and pt02 < len(list2):
        if list1[pt01] <= list2[pt02]:
            result.append(list1[pt01])
            pt01 += 1
        else:
            result.append(list2[pt02])
            pt02 += 1

    while pt01 < len(list1):
        result.append(list1[pt01])
        pt01 += 1

    while pt02 < len(list2):
        result.append(list2[pt02])
        pt02 += 1

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge_sorted_ls(left, right)


with open(input_file_path, "r") as f01, open(output_file_path, "w") as f02:
    N = int(f01.readline())
    Alice_ls = list(map(int, f01.readline().split()))
    M = int(f01.readline())
    BOB_ls = list(map(int, f01.readline().split()))

    merged_list = merge_sort(Alice_ls + BOB_ls)

    f02.write(' '.join(map(str, merged_list)))

#