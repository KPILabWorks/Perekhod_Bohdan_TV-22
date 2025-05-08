import numpy as np
import matplotlib.pyplot as plt


# --- Прикладна модель попиту (падає з ростом ціни) ---
def demand(tariff):
    return 100 - 2 * tariff  # штучна лінійна еластичність


# --- Вартість виробництва в кожну годину (фіксована або нелінійна) ---
def cost(d):
    return 0.5 * d ** 1.5


# --- Цільова функція (мінус прибуток = для мінімізації) ---
def objective(tariffs):
    demands = demand(tariffs)
    return -np.sum(tariffs * demands - cost(demands))


# --- Генетичний алгоритм ---
def genetic_algorithm(fitness_fn, n_hours=24, pop_size=100, generations=100):
    pop = np.random.uniform(1, 10, (pop_size, n_hours))
    best_values = []

    for gen in range(generations):
        fitness = np.array([fitness_fn(ind) for ind in pop])
        best_values.append(-np.min(fitness))

        idx = np.argsort(fitness)
        pop = pop[idx[:pop_size // 2]]  # Відбір кращої половини

        offspring = []
        for _ in range(pop_size // 2):
            p1, p2 = pop[np.random.randint(0, len(pop), 2)]
            cross = np.random.randint(1, n_hours)
            child = np.concatenate([p1[:cross], p2[cross:]])
            # --- МУТАЦІЯ ---
            if np.random.rand() < 0.2:
                child[np.random.randint(0, n_hours)] += np.random.normal(0, 0.5)
            offspring.append(child)

        pop = np.vstack([pop, offspring])
    return best_values


# --- Градієнтний спуск ---
def gradient_descent(obj_fn, n_hours=24, lr=0.01, iterations=100):
    tariffs = np.random.uniform(1, 10, n_hours)
    history = []
    for _ in range(iterations):
        # --- Обчислюємо градієнт чисельно ---
        grad = np.zeros(n_hours)
        epsilon = 1e-5
        for i in range(n_hours):
            t1 = tariffs.copy()
            t1[i] += epsilon
            grad[i] = (obj_fn(t1) - obj_fn(tariffs)) / epsilon
        tariffs -= lr * grad
        history.append(-obj_fn(tariffs))
    return history


# --- Порівняння ---
ga_perf = genetic_algorithm(objective)
gd_perf = gradient_descent(objective)

plt.plot(ga_perf, label='Генетичний алгоритм')
plt.plot(gd_perf, label='Градієнтний спуск')
plt.xlabel('Ітерація')
plt.ylabel('Прибуток')
plt.title('Порівняння ефективності оптимізації тарифів')
plt.legend()
plt.grid()
plt.show()
