def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def word_count(book_text):
  num_words = len(book_text.split())
  return num_words

def main():
  book_text = get_book_text("books/frankenstein.txt")
  num_words = word_count(book_text)
  print(f"Found {num_words} total words")

main()
