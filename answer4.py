def replace_letters_with_spaces(text):
    modified_text = ""
    for char in text:
        if char.lower() in ['a', 'b', 'c', 'd', 'k', 'l', 'm', 'n']:
            modified_text += " "
        else:
            modified_text += char
    return modified_text

text = "Дан текст. Заменить пробелами буквы от 'a' до 'd' и от 'k' до 'n'"
modified_text = replace_letters_with_spaces(text)
print(modified_text)
