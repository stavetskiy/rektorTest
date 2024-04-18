def replace_digits_with_spaces(text):
    modified_text = ""
    for char in text:
        if char.isdigit():
            modified_text += " "
        else:
            modified_text += char
    return modified_text

text = "Дан текст 123. Заменить пробелами все цифры"
modified_text = replace_digits_with_spaces(text)
print(modified_text)
