def get_text_words(text: str):
    words = text.split()
    return len(words)


def get_characters(text: str):
    chars: dict[str, int] = {}
    for char in text:
        if not char.isalpha():
            continue
        char = char.lower()
        chars[char] = chars.get(char, 0) + 1

    return chars


def get_characters_sorted(text: str):
    chars = get_characters(text)
    sorted_chars = sorted(chars.items(), key=lambda item: item[1], reverse=True)
    key_value = "\n".join(f"{char}: {count}" for char, count in sorted_chars)
    return key_value
