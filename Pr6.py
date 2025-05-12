import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv("Pr6_Amplitudes.csv")

# Перетворення "неправильних" даних в пусті (неправильні зі сторони застосунку)
df["Sound pressure level (dB)"] = pd.to_numeric(df["Sound pressure level (dB)"], errors='coerce')

# Візуалізація первинна
plt.figure(figsize=(12, 4))
plt.plot(df["Time (s)"], df["Sound pressure level (dB)"], color='darkred')
plt.title("Raw Sound Pressure Level")
plt.xlabel("Time (s)")
plt.ylabel("dB")
plt.grid(True)
plt.tight_layout()
plt.savefig("Pr6_raw_plot.png")
plt.close()

# Згладжування звуку методом зведення гучностей в 5 послідовних точках до одного значення
df["Smoothed dB"] = df["Sound pressure level (dB)"].rolling(window=5, min_periods=1).mean()

# Візуалізація після згладжування
plt.figure(figsize=(12, 4))
plt.plot(df["Time (s)"], df["Smoothed dB"], label="Smoothed", color='green')
plt.title("Smoothed Sound Pressure Level")
plt.xlabel("Time (s)")
plt.ylabel("dB")
plt.grid(True)
plt.tight_layout()
plt.savefig("Pr6_smoothed_plot.png")
plt.close()

def label_device_by_dB(dB):
    if dB+120 < 50:  #в файлі гучність записана мінусовою, тому коригуємо додаванням
        return "computer"
    else:
        return "air_conditioner"

df["device"] = df["Smoothed dB"].apply(label_device_by_dB)

df_clean = df.dropna(subset=["Smoothed dB", "device"])

X = df_clean[["Smoothed dB"]]
y = df_clean["device"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Оцінка
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
