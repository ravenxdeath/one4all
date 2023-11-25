def minCoins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def processInputAndOutput(input_path, output_path):
    with open(input_path, 'r') as f001:
        lines = f001.readlines()
    
    results = []
    n, amount = map(int, lines[0].strip().split())
    coins = list(map(int, lines[1].strip().split()))
    results.append(minCoins(coins, amount))
    
    with open(output_path, 'w') as f002:
        for result in results:
            f002.write(str(result) + '\n')

input_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB08\\task03_input01.txt"
output_file_path01 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB08\\task03_output01.txt"

input_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB08\\task03_input02.txt"
output_file_path02 = "C:\\CODE\\TahmidRaven\\UNI\\CSE221venv\\LAB08\\task03_output02.txt"

processInputAndOutput(input_file_path01, output_file_path01)
processInputAndOutput(input_file_path02, output_file_path02)

