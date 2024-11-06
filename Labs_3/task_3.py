# TODO  Напишите функцию count_letters
def count_letters (some_str):

    result_dict = {}
    for char in some_str.lower():
        if char.isalpha():
            result_dict[char] = result_dict.get(char, 0) + 1
    return result_dict

# TODO Напишите функцию calculate_frequencyсловарь

def calculate_frequency (some_dict):
    total_count = sum(some_dict.values())
    result_dict = { letter: round(count / total_count, 2) for letter, count in some_dict.items()}
    return result_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

count_char = count_letters(main_str)
frequency_char = calculate_frequency(count_char)
for char, probab in frequency_char.items():
    print(f"{char}: {probab}")