def main():
    with open('evn.test.morph', 'r', encoding='utf-8') as file:
        text = file.read()
    lines = text.split('\n')
    for i in range(len(lines)):
        if lines[i]:
            lines[i] += '\t' + lines[i]
    with open('output.morph', 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))

if __name__ == '__main__':
    main()
