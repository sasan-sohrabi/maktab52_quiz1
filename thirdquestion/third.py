import argparse

def swapcase_decorators(gen):
    def inner(*args, **kwargs):
        word = gen(*args, **kwargs)
        return word.swapcase()
    return inner


@swapcase_decorators
def duplicate_words_gen(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        for word in text:
            for w in word:
                if word.count(w) > 1:
                    yield word


if __name__ == "__main__":
    # Define parse args for python script
    parser = argparse.ArgumentParser(description='swapcase')

    parser.add_argument('-f', '--file', action='store', metavar="FILE PATH",
                        help='swapcase', required=True)

    args = parser.parse_args()

    print(duplicate_words_gen(args.file))

