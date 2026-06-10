text = input("Enter a text: ")

total_words = len(text.split())
total_characters = len(text)
total_sentences = text.count(".")

print("Total words:", total_words)
print("Total characters:", total_characters)
print("Total sentences:", total_sentences)