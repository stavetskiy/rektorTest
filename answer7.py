def replace_second_word_with_dollar(text):
    words = text.split()
    if len(words) >= 2:
        words[1] = "$"
    return " ".join(words)

text = "Дан текст. Заменить знаком $ второе слово"
modified_text = replace_second_word_with_dollar(text)
print(modified_text)
