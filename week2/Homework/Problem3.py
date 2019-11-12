import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", help="simple sentence", type=str)
parser.add_argument("first_word", help="replaced word", type=str)
parser.add_argument("Second word", help="replacing word", type=str)

args = parser.parse_args()

print('The given text: ', args.text)
print('First word: ', args.first_word)
print('Second word: ', args.Second word)
print('Output string: ', args.text.replace(args.first_word, args.second_word))
