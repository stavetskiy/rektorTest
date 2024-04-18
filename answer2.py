def count_adjacent_pairs(text):
    pairs_count = {}
    for i in range(len(text)-1):
        pair = text[i:i+2]
        if pair in pairs_count:
            pairs_count[pair] += 1
        else:
            pairs_count[pair] = 1
    return pairs_count

text = "Текст для тестирования задания"
pairs_count = count_adjacent_pairs(text)

print("Частота встречаемости двухбуквенных сочетаний:")
for pair, count in pairs_count.items():
    print(f"{pair}: {count}")
