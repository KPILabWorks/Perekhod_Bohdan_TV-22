import pandas as pd
import string

# Функция для очистки текста
def clean_text(text):
    if not isinstance(text, str):  # Проверка, если текст не строка
        return ""
    text = text.lower().strip()  # Приводим к нижнему регистру и убираем пробелы
    text = text.translate(str.maketrans("", "", string.punctuation))  # Убираем пунктуацию
    return text

# Чтение файла
input_file = "text.txt"
output_file = "output.txt"

# Читаем текстовый файл в DataFrame (каждая строка — отдельная запись)
df = pd.DataFrame({"text": open(input_file, "r", encoding="utf-8").readlines()})

# Применяем функцию очистки с использованием .apply()
df["cleaned_text"] = df["text"].apply(clean_text)

# Записываем результат в новый файл
df["cleaned_text"].to_csv(output_file, index=False, header=False, encoding="utf-8")

print(f"Обработанный текст сохранён в {output_file}")
