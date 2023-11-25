def find_max_possible_race_members(num_fights, rivals):
    race_members = set()
    for u, v in rivals:
        race_members.add(u)
        race_members.add(v)
    return len(race_members)

def Sol():
    input_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task08_input01.txt"
    output_file_path = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB04\\Task08_output01.txt"

    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        T = int(infile.readline().strip())

        for case_number in range(1, T + 1):
            num_fights = int(infile.readline().strip())
            rivals = [tuple(map(int, infile.readline().strip().split())) for _ in range(num_fights)]

            max_race_members = find_max_possible_race_members(num_fights, rivals)

            outfile.write(f"Case {case_number}: {max_race_members-1}\n")

Sol()
