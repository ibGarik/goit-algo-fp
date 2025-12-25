def greedy_algorithm(items, budget):
    item_list = []
    for name, data in items.items():
        cost = data['cost']
        calories = data['calories']
        ratio = calories / cost
        item_list.append((name, cost, calories, ratio))


    item_list.sort(key=lambda x: x[3], reverse=True)

    total_calories = 0
    chosen_items = []
    current_budget = budget

    for name, cost, calories, ratio in item_list:
        if cost <= current_budget:
            chosen_items.append(name)
            total_calories += calories
            current_budget -= cost

    return chosen_items, total_calories


def dynamic_programming(items, budget):
    item_list = [(name, data['cost'], data['calories']) for name, data in items.items()]
    n = len(item_list)


    K = [[0 for w in range(budget + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        name, cost, calories = item_list[i - 1]
        for w in range(budget + 1):
            if cost <= w:
                K[i][w] = max(K[i - 1][w], calories + K[i - 1][w - cost])
            else:
                K[i][w] = K[i - 1][w]


    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if K[i][w] != K[i - 1][w]:
            name, cost, calories = item_list[i - 1]
            chosen_items.append(name)
            w -= cost 

    return chosen_items, K[n][budget]


# Тестування

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# жадібний алгоритм
greedy_items, greedy_cals = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм (бюджет {budget}):")
print(f"Вибрані страви: {greedy_items}")
print(f"Сумарна калорійність: {greedy_cals}")

print("-" * 30)

# Динамічне програмування
dp_items, dp_cals = dynamic_programming(items, budget)
print(f"Динамічне програмування (бюджет {budget}):")
print(f"Вибрані страви: {dp_items}")
print(f"Сумарна калорійність: {dp_cals}")