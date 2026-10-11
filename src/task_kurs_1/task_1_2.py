# Напишите функцию count_morse_characters(), которая принимает строку,
# состоящую из символов азбуки Морзе, и возвращает количество символов
# (точек и/или тире) в ней.
# Пример строки азбуки Морзе:
#
# .--- .- ...- .-




def count_morse_characters(morse):
    number_characters = len(morse.replace(" ", ""))

    return number_characters



morse = str(input("Введите код морзе:"))
result = count_morse_characters(morse)
print(result)




