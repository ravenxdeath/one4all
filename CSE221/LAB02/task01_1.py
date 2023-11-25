input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB02\\task01_1_input.txt"
output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB02\\task01_1_output.txt"

with open(input_file_path, "r") as f01, open(output_file_path, "w") as f02:


    lenArr, sumo = map(int, f01.readline().strip().split())

    arr = list(map(int, f01.readline().strip().split()))

    flag = False
    for j in range(lenArr):
        for k in range(j + 1, lenArr):
            if arr[j] + arr[k] == sumo:
                index01 = str(j + 1)
                index02 = str(k + 1)
                f02.write(index01 + " ")
                f02.write(index02 + " ")
                flag = True
                break

        if flag:
            break

    if not flag:
        f02.write("Impossible")

    f02.close()
    f01.close()

# This algorithm gives O(n^2) time complexity because of the nested loops. As shown the outloop runs n times where the inner loop runs n-1, n-2, n-3 ..... , 1 times eventually, gives the methematcall formula of (n * n-1 ) / 2 which gives O(n^2) time complexity.  