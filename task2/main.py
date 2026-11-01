
def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat)

    except (FileNotFoundError, OSError, ValueError) as error:
        print(f"Помилка читання файлу: {error}")

    return cats


cats_info = get_cats_info("cats_file.txt")
for cat in cats_info:
    print(cat)
