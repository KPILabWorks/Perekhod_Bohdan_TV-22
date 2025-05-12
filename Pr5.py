import numpy as np
#Завдання знайти температуру в пропущені часові точки за допомогою інтерполяції
data = [14, np.nan , 16, np.nan , 25]  #Як приклад взято температуру за день (12:00, 13, 14, 15, 16)

def interpolation(data):
    result = data.copy()
    for i in range(len(data)):
        if data[i] is np.nan:
            prev = i - 1
            while prev >= 0 and data[prev] is np.nan:
                prev -= 1
            next = i + 1
            while next < len(data) and data[next] is np.nan:
                next += 1

            if prev >= 0 and next < len(data):
                prev_val = data[prev]
                next_val = data[next]
                gap = next - prev
                step = (next_val - prev_val) / gap
                result[i] = prev_val + step * (i - prev)
    return result

interpolated = interpolation(data)
print(interpolated)
