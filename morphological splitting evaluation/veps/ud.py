import re
from collections import Counter


def find_most_freq_POS(text):
    matches = re.findall('[A-Z]{2,6}', text)
    count = Counter(matches)
    most_freq_POS = count.most_common(1)[0][0]
    return most_freq_POS


def get_file_text(path):
    with open(path, 'r', encoding = 'utf-8') as file:
        return file.read()


def simple_baseline(empty_text, POS):
    lines = empty_text.split('\n')
    output = '\n'
    for line in lines:
        cells = line.split('\t')
        if len(cells) == 10:
          cells[2] = cells[1].lower()
          cells[3] = POS
          output += '\t'.join(cells) + '\n'
        else:
            if not line:
                output += '\n'
    return output[:-1]


def main():
    text = get_file_text('vep.train.ud')
    empty_text = get_file_text('vep.test.ud')
    with open('output.ud', 'w', encoding='utf-8') as file:
        file.write(simple_baseline(empty_text, find_most_freq_POS(text)))


if __name__ == '__main__':
    main()
