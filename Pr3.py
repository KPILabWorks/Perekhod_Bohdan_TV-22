import random

#------------------- Генеруємо штучні транзакції -----------------
data = [random.gauss(500, 50) for _ in range(365)]
anomaly_indices = random.sample(range(365), 10)
for i in anomaly_indices:
    data[i] += random.choice([300, -300])  # Аномалі я

# --------------------- Обчислення відхилень --------------------------
mean = sum(data) / len(data)
std = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5

# =============== Виявлення аномалій ===========
threshold = 3
predicted_anomalies = []
for i, x in enumerate(data):
    z = abs((x - mean) / std)
    if z > threshold:
        predicted_anomalies.append(i)

print("Аномальні індекси (справжні):", sorted(anomaly_indices))
print("Аномальні індекси (виявлені):", predicted_anomalies)
