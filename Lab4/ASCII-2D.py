def get_char_art(char, symbol):
    art = []

    def get_ascii_art(symbol):
        if symbol == 'А':
            art = [
                f" {symbol} {symbol}  ",
                f"{symbol}{symbol}{symbol}{symbol}{symbol} ",
                f"{symbol}   {symbol} ",
                f"{symbol}   {symbol} ",
                f"{symbol}   {symbol}"
            ]
        elif symbol == 'Б':
            art = [
                f"{symbol}{symbol}{symbol}{symbol}{symbol} ",
                f"{symbol}     ",
                f"{symbol}{symbol}{symbol}{symbol}{symbol} ",
                f"{symbol}     {symbol}",
                f"{symbol}{symbol}{symbol}{symbol}{symbol} "
            ]
        elif symbol == 'В':
            art = [
                f"{symbol}{symbol}{symbol}{symbol}{symbol} ",
                f"{symbol}    {symbol}",
                f"{symbol}{symbol}{symbol}{symbol}{symbol} ",
                f"{symbol}    {symbol}",
                f"{symbol}{symbol}{symbol}{symbol}{symbol} "
            ]
        elif symbol == 'Г':
            art = [
                f"{symbol}{symbol}{symbol}{symbol}{symbol}",
                f"{symbol}     ",
                f"{symbol}     ",
                f"{symbol}     ",
                f"{symbol}     "
            ]
        elif symbol == 'Д':
            art = [
                f"  {symbol}{symbol}{symbol}{symbol} ",
                f" {symbol}   {symbol} ",
                f" {symbol}   {symbol} ",
                f"{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}",
                f"{symbol}     {symbol}"
            ]
        elif symbol == 'Е':
            art = [
                f"{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}",
                f"{symbol}     ",
                f"{symbol}{symbol}{symbol}{symbol}{symbol} ",
                f"{symbol}     ",
                f"{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}"
            ]
        elif symbol == 'Є':
            art = [
                f"  {symbol}{symbol}{symbol}{symbol} ",
                f" {symbol}     ",
                f"{symbol}{symbol}{symbol}{symbol}{symbol}{symbol} ",
                f" {symbol}     ",
                f"  {symbol}{symbol}{symbol}{symbol} "
            ]
        elif symbol == 'Ж':
            art = [
                f"{symbol} {symbol} {symbol}",
                f"   {symbol}   ",
                f"  {symbol}{symbol}{symbol}  ",
                f"   {symbol}   ",
                f"{symbol} {symbol} {symbol}"
            ]
        elif symbol == 'З':
            art = [
                f"{symbol}{symbol}{symbol}{symbol}{symbol} ",
                f"     {symbol}",
                f" {symbol}{symbol}{symbol}{symbol} ",
                f"     {symbol}",
                f"{symbol}{symbol}{symbol}{symbol}{symbol} "
            ]
        elif symbol == 'И':
            art = [
                f"{symbol}    {symbol}{symbol}",
                f"{symbol}   {symbol} {symbol}",
                f"{symbol}  {symbol}  {symbol}",
                f"{symbol} {symbol}   {symbol}",
                f"{symbol}{symbol}    {symbol}"
            ]
        elif symbol == 'І':
            art = [
                f" {symbol}{symbol}{symbol}{symbol} ",
                f"   {symbol}  ",
                f"   {symbol}  ",
                f"   {symbol}  ",
                f" {symbol}{symbol}{symbol}{symbol} "
            ]
        elif symbol == 'Ї':
            art = [
                f"  {symbol} {symbol}  ",
                f" {symbol}{symbol}{symbol}{symbol} ",
                f"   {symbol}  ",
                f"   {symbol}  ",
                f" {symbol}{symbol}{symbol}{symbol} "
            ]
        elif symbol == 'Й':
            art = [
                f" {symbol}{symbol}{symbol} ",
                f"     ",
                f"{symbol}  {symbol}{symbol}",
                f"{symbol} {symbol} {symbol}",
                f"{symbol}{symbol}  {symbol}"
            ]
        elif symbol == 'К':
            art = [
                f"{symbol}    {symbol}",
                f"{symbol}   {symbol} ",
                f"{symbol}{symbol}{symbol}{symbol}  ",
                f"{symbol}   {symbol} ",
                f"{symbol}    {symbol}"
            ]
        elif symbol == 'Л':
            art = [
                f"  {symbol}{symbol}{symbol}{symbol}  ",
                f" {symbol}   {symbol} ",
                f"{symbol}     {symbol}",
                f"{symbol}     {symbol}",
                f"{symbol}     {symbol}"
            ]
        elif symbol == 'М':
            art = [
                f"{symbol}     {symbol}",
                f"{symbol}{symbol}   {symbol}{symbol}",
                f"{symbol} {symbol} {symbol} {symbol}",
                f"{symbol}  {symbol}  {symbol}",
                f"{symbol}     {symbol}"
            ]
        elif symbol == 'Н':
            art = [
                f"{symbol}     {symbol}",
                f"{symbol}     {symbol}",
                f"{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}",
                f"{symbol}     {symbol}",
                f"{symbol}     {symbol}"
            ]
        elif symbol == 'О':
            art = [
                f" {symbol}{symbol}{symbol}{symbol}{symbol} ",
                f"{symbol}     {symbol}",
                f"{symbol}     {symbol}",
                f"{symbol}     {symbol}",
                f" {symbol}{symbol}{symbol}{symbol}{symbol} "
            ]
        elif symbol == 'П':
            art = [
                f"{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}",
                f"{symbol}     {symbol}",
                f"{symbol}     {symbol}",
                f"{symbol}     {symbol}",
                f"{symbol}     {symbol}"
            ]
        elif symbol == 'Р':
            art = [
                f"{symbol}{symbol}{symbol}{symbol}{symbol} ",
                f"{symbol}    {symbol}",
                f"{symbol}{symbol}{symbol}{symbol}{symbol} ",
                f"{symbol}     ",
                f"{symbol}     "
            ]
        elif symbol == 'С':
            art = [
                f" {symbol}{symbol}{symbol}{symbol}{symbol} ",
                f"{symbol}      ",
                f"{symbol}      ",
                f"{symbol}      ",
                f" {symbol}{symbol}{symbol}{symbol}{symbol} "
            ]
        elif symbol == 'Т':
            art = [
                f"{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}",
                f"   {symbol}   ",
                f"   {symbol}   ",
                f"   {symbol}   ",
                f"   {symbol}   "
            ]
        elif symbol == 'У':
            art = [
                f"{symbol}     {symbol}",
                f" {symbol}   {symbol} ",
                f"  {symbol} {symbol}  ",
                f"   {symbol}   ",
                f" {symbol}{symbol}{symbol}   "
            ]
        elif symbol == 'Ф':
            art = [
                f"   {symbol}   ",
                f" {symbol}{symbol}{symbol}{symbol}{symbol} ",
                f"{symbol}  {symbol}  {symbol}",
                f" {symbol}{symbol}{symbol}{symbol}{symbol} ",
                f"   {symbol}   "
            ]
        elif symbol == 'Х':
            art = [
                f"{symbol}     {symbol}",
                f" {symbol}   {symbol} ",
                f"  {symbol}{symbol}{symbol}  ",
                f" {symbol}   {symbol} ",
                f"{symbol}     {symbol}"
            ]
        elif symbol == 'Ц':
            art = [
                f"{symbol}     {symbol}",
                f"{symbol}     {symbol}",
                f"{symbol}     {symbol}",
                f"{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}",
                f"      {symbol}"
            ]
        elif symbol == 'Ч':
            art = [
                f"{symbol}     {symbol}",
                f"{symbol}     {symbol}",
                f" {symbol}{symbol}{symbol}{symbol}{symbol}{symbol}",
                f"      {symbol}",
                f"      {symbol}"
            ]
        elif symbol == 'Ш':
            art = [
                f"{symbol}  {symbol}  {symbol}",
                f"{symbol}  {symbol}  {symbol}",
                f"{symbol}  {symbol}  {symbol}",
                f"{symbol}  {symbol}  {symbol}",
                f"{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}"
            ]
        elif symbol == 'Щ':
            art = [
                f"{symbol}  {symbol}  {symbol}",
                f"{symbol}  {symbol}  {symbol}",
                f"{symbol}  {symbol}  {symbol}",
                f"{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}",
                f"      {symbol}"
            ]
        elif symbol == 'Ь':
            art = [
                f"{symbol}     {symbol}",
                f"{symbol}     {symbol}",
                f"{symbol}{symbol}{symbol}{symbol}{symbol}{symbol}",
                f"{symbol}     {symbol}",
                f"{symbol}     {symbol}"
            ]
        elif symbol == 'Ю':
            art = [
                f"{symbol}    {symbol}{symbol}{symbol}",
                f"{symbol}   {symbol}  {symbol}",
                f"{symbol}  {symbol}   {symbol}",
                f"{symbol} {symbol}    {symbol}",
                f"{symbol}{symbol}{symbol}{symbol}{symbol} "
            ]
        elif symbol == 'Я':
            art = [
                f" {symbol}{symbol}{symbol}{symbol}{symbol} ",
                f"{symbol}   {symbol} ",
                f"{symbol}   {symbol} ",
                f"{symbol}  {symbol}{symbol} ",
                f" {symbol}{symbol}{symbol}{symbol} "
            ]
        else:
            art = [" " * 5] * 5  # Випадок для незнайомих символів

        return art


def generate_ascii_art(text, symbol, alignment='l'):
    lines = [""] * 5  # Шаблон для рядків ASCII-арту
    for char in text:
        char_art = get_char_art(char, symbol)

        for i in range(len(lines)):
            lines[i] += char_art[i] + " "  # Додаємо пробіл між літерами

    # Вирівнювання
    max_length = max(len(line) for line in lines)
    if alignment == 'c':
        lines = [line.center(max_length) for line in lines]
    elif alignment == 'r':
        lines = [line.rjust(max_length) for line in lines]

    return "\n".join(lines)

def main():
    while True:
        try:
            # Запитуємо текст у користувача
            text = input("Введіть слово або фразу для ASCII-арту: ").upper()  # Перетворення на великі літери
            if not text:
                print("Помилка: Введіть хоча б один символ.")
                continue

            symbol = input("Введіть символ для заміни: ")
            if len(symbol) != 1:
                print("Помилка: Введіть тільки один символ для заміни.")
                continue

            alignment = input("Виберіть вирівнювання (l/c/r): ").lower()
            if alignment not in ['l', 'c', 'r']:
                print("Помилка: Невірне вирівнювання. Виберіть 'l', 'c' або 'r'.")
                continue

            # Генеруємо ASCII-арт
            ascii_art = generate_ascii_art(text, symbol, alignment)

            # Попередній перегляд
            print("\nПопередній перегляд ASCII-арту:")
            print(ascii_art)

            # Збереження у файл
            save_option = input("Бажаєте зберегти ASCII-арт у файл? (так/ні): ").lower()
            if save_option == "так":
                with open("ascii_art.txt", "w") as file:
                    file.write(ascii_art)
                print("ASCII-арт успішно збережено в файл 'ascii_art.txt'.")

            # Запит на повторне виконання
            repeat_option = input("Бажаєте виконати ще раз? (так/ні): ").lower()
            if repeat_option != "так":
                break

        except Exception as e:
            print(f"Помилка: {e}")

if __name__ == "__main__":
    main()