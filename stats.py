def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_count = {}
    words = text.split()
    for word in words:
        characters = list(word.lower())
        for character in characters:
            if character not in character_count:
                character_count[character] = 1
            else:
                character_count[character] += 1
    return character_count

def sort_on(items):
    return items["num"]

def sort_characters(dict):
    sorted = []
    for letter in dict.keys():
        item = {}
        item["char"] = letter
        item["num"] = dict[letter]
        sorted.append(item)
    sorted.sort(reverse=True, key=sort_on)
    return sorted

