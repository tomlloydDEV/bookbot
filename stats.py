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
