#Execute the code directly
file = 'moby_dick.txt'
word = 'the '

with open(file, encoding='utf-8') as f:
    contents = f.read()
    words = contents.lower().count(word)
    print(f"the file {file} has {words} words")





#Execute the code by defining the function:
def count_common_words(filename, word):
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
        word_count = contents.lower().count(word)

        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)


filename = 'moby_dick.txt'
count_common_words(filename, 'the ')
