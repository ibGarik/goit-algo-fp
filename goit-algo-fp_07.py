import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_simulations):
    counts = {sum_val: 0 for sum_val in range(2, 13)}

    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total_sum = die1 + die2
        counts[total_sum] += 1

    return counts

def main():
    num_simulations = 1_000_000
    

    print(f"Симуляція {num_simulations} кидків кубиків...")
    results = simulate_dice_rolls(num_simulations)


    theoretical_probs = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }


    print("\n{:^5} | {:^15} | {:^15} | {:^10}".format("Сума", "Монте-Карло %", "Теоретична %", "Різниця"))
    print("-" * 55)

    monte_carlo_probs = {}

    for s in range(2, 13):
        count = results[s]
        mc_prob = (count / num_simulations) * 100 
        monte_carlo_probs[s] = mc_prob
        
        theo_prob = theoretical_probs[s]
        diff = abs(mc_prob - theo_prob)
        
        print(f"{s:^5} | {mc_prob:^15.2f} | {theo_prob:^15.2f} | {diff:^10.2f}")


    sums = list(range(2, 13))
    mc_values = [monte_carlo_probs[s] for s in sums]
    theo_values = [theoretical_probs[s] for s in sums]

    plt.figure(figsize=(10, 6))
    

    plt.bar([x - 0.2 for x in sums], mc_values, width=0.4, label='Монте-Карло', color='skyblue', align='center')
    plt.bar([x + 0.2 for x in sums], theo_values, width=0.4, label='Теоретична', color='orange', align='center')

    plt.xlabel('Сума на кубиках')
    plt.ylabel('Ймовірність (%)')
    plt.title(f'Метод Монте-Карло ({num_simulations} кидків) vs Теорія')
    plt.xticks(sums)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

if __name__ == "__main__":
    main()