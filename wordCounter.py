# word_counter.py

def count_words(text):
    """
    Function to count the number of words in the given text.
    """
    if not text.strip():  # Check for empty input
        return 0
    words = text.split()  # Split the text into words
    return len(words)

def main():
    """
    Main function to handle user input and display word count.
    """
    print("Welcome to Word Counter!")
    text = input("Please enter a sentence or paragraph: ")
    word_count = count_words(text)
    print(f"Word count: {word_count}")

if __name__ == "__main__":
    main()
