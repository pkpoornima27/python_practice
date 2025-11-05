##12. Count Words in a File
def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            print(f"Number of words in '{filename}': {len(words)}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = input("Enter the file name: ")
count_words_in_file(filename)

