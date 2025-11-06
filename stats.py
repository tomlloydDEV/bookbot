def word_count(book_text):
    num_words = len(book_text.split())
    return num_words


def char_count(book_text):
    book_text = book_text.lower()
    chars = {}
    for c in book_text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1

    return chars


def chars_sorted(char_count: dict) -> list:
    items = [{"char": ch, "num": n} for ch, n in char_count.items()]

    def sort_on(d):
        return d["num"]

    items.sort(reverse=True, key=sort_on)
    return items
