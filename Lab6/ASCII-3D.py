from ASCII_classes import Cube, Sphere, Pyramid

def main():
    while True:
        try:
            shape_type = input("Яку фігуру ви хочете створити? (куб/сфера/піраміда): ").strip().lower()
            
            if shape_type in ["куб", "сфера", "піраміда"]:
                try:
                    size = int(input("Введіть розмір фігури: "))
                    if size <= 0:
                        raise ValueError("Розмір фігури має бути додатнім числом.")
                    
                    color = input("Введіть колір фігури (введіть у форматі 'r g b'): ")
                    color_tuple = tuple(map(float, color.split()))  # конвертуємо колір у tuple

                    if len(color_tuple) != 3 or any(c < 0 or c > 1 for c in color_tuple):
                        raise ValueError("Колір повинен бути у форматі 'r g b' з значеннями від 0 до 1.")
                    
                    if shape_type == "куб":
                        shape = Cube(size, color_tuple)
                    elif shape_type == "сфера":
                        shape = Sphere(size, color_tuple)
                    elif shape_type == "піраміда":
                        shape = Pyramid(size, color_tuple)

                    shape_representation = shape.create_3d()

                    for line in shape_representation:
                        print(line)

                    # Виклик функції для малювання фігури з використанням Matplotlib
                    if shape_type == "куб":
                        shape.draw_matplotlib_cube()
                    # Для сфери та піраміди потрібно реалізувати подібні функції у відповідних класах.

                except ValueError as ve:
                    print(f"Помилка: {ve}")

        except Exception as e:
            print(f"Сталася помилка: {e}")

        another = input("Бажаєте створити ще одну фігуру? (так/ні): ").strip().lower()
        if another != "так":
            break

if __name__ == "__main__":
    main()