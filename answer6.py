def replace_second_letter_with_space(text):
    words = text.split()
    modified_words = []
    for word in words:
        if len(word) > 1:
            modified_word = word[0] + " " + word[2:]
        else:
            modified_word = word
        modified_words.append(modified_word)
    return " ".join(modified_words)

text = "Дан текст. Заменить пробелом вторую букву каждого слова"
modified_text = replace_second_letter_with_space(text)
print(modified_text)
