def find_shortest_and_longest_words(sentence):
    words = sentence.split()
    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)
    return shortest_word, longest_word

sentence = "В заданном предложении найти самое короткое и самое длинное слова"
shortest, longest = find_shortest_and_longest_words(sentence)
print("Самое короткое слово:", shortest)
print("Самое длинное слово:", longest)
