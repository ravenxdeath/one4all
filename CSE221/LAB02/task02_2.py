#Time complexity O(n). It utilizes a simple merge function to merge two lists. 

input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB02\\task02_2_input.txt"
output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB02\\task02_2_output.txt"

def merged(ls01, ls02):
    result = []
    pt01 = 0
    pt02 = 0

    while pt01 < len(ls01) and pt02 < len(ls02):  
        if ls01[pt01] <= ls02[pt02]:
            result.append(ls01[pt01])
            pt01 += 1
        else:
            result.append(ls02[pt02])
            pt02 += 1

    while pt01 < len(ls01):              #merges the remaining elements  
        result.append(ls01[pt01])
        pt01 += 1

    while pt02 < len(ls02):              #merges the remaining elements  
        result.append(ls02[pt02])
        pt02 += 1

    return result

# The time complexity of the merged function is: O(n+n+n) = O(3n) =  O(n).

with open(input_file_path, "r") as f01, open(output_file_path, "w") as f02:
  
    N = int(f01.readline())
    Alice_ls = list(map(int, f01.readline().split()))
    
    M = int(f01.readline())
    BOB_ls = list(map(int, f01.readline().split()))
    
    merged_list = merged(Alice_ls, BOB_ls)

    f02.write(' '.join(map(str, merged_list)))
