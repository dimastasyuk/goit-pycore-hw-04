

def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            total = 0
            count = 0

            for line in file:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1

            if count == 0:
                return 0, 0

            average = total / count
            return total, average

    except (FileNotFoundError, ValueError, UnicodeError, OSError) as e:
        print("Помилка:", e)
        return 0, 0


total, average = total_salary("salary_file.txt")

print(f"Загальна сума заробітної плати: {total}")
print(f"Середня заробітна плата: {average}")
