

def find_common_participants(first_str, second_str, separator = ","):
    common_participants = sorted(set(first_str.split(separator)) & set(second_str.split(separator)))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group,participants_second_group, "|")