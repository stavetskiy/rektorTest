def replace_vowels_with_spaces(text):
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    modified_text = ""
    for char in text:
        if char in vowels:
            modified_text += " "
        else:
            modified_text += char
    return modified_text

text = "Дан текст. Заменить пробелами все гласные буквы"
modified_text = replace_vowels_with_spaces(text)
print(modified_text)
