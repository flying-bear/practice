import re
from collections import Counter


def get_file_text(path):
    with open(path, 'r', encoding = 'utf-8') as file:
        return file.read()


def copy(test_text):
    print('creating the copy file')
    lines = test_text.split('\n')
    output = []
    for i in range(len(lines)):
        if lines[i]:
            word = lines[i].split('\t')[0]
            output.append(str(word))
    return '\n'.join(output)

def get_dict(train_text, test_text):
    print('getting dictionary for the complex file')
    dictionary = {}
    words = sorted(list(set([word for word in copy(test_text).split('\n')])))
    for word in words:
        print('working on: ' + word)
        regex = f'\t(.*?)\t{word}\t'
        matches = re.findall(regex, train_text)
        if matches:
            form = Counter(matches).most_common(1)[0][0]
            if form and form != '\t':
                dictionary[word] = form
            else:
                dictionary[word] = word
        else:
            dictionary[word] = word
    return dictionary

def compl(test_text, dictionary):
    print('creating the complex file')
    lines = test_text.split('\n')
    output = []
    for i in range(len(lines)):
        if lines[i]:
            word = lines[i].split('\t')[0]
            output.append(dictionary[word])
    return '\n'.join(output)


def main():
    train = get_file_text('vep.train.ud')
    test = get_file_text('vep.test.syn')
    dictionary = get_dict(train, test)
    with open('output_copy.syn', 'w', encoding='utf-8') as file:
        file.write(copy(test))
    with open('output_complex.syn', 'w', encoding='utf-8') as file:
        file.write(compl(test, dictionary))


if __name__ == '__main__':
    main()
