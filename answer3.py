def replace_last_letter_with_space(text):
    words = text.split()
    modified_words = []
    for word in words:
        if len(word) > 1:
            modified_word = word[:-1] + " "
        else:
            modified_word = word
        modified_words.append(modified_word)
    return " ".join(modified_words)

text = "Дан текст. Заменить пробелом последнюю букву каждого слова"
modified_text = replace_last_letter_with_space(text)
print(modified_text)
