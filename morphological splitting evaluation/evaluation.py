import os


def input_files(): # opens and reads input files
    stan = 'standard'
    test = 'test'
    files = {stan:[], test:[]}
    for key in files:
        f_path = input(f'Input {key} file directory: ')
        f_name = os.path.splitext(os.path.basename(f_path))[0]
        with open(f_path, 'r', encoding='utf-8') as file: # os.path -- make the path universal
            f_text = file.read()
        files[key] += [f_path, f_name, f_text]
    return files # returns a dictionary of files and corresponding paths, names, and texts


def initialize_evaluation(): # writes evaluetion file with zero values
    evaluation = {'Precision':0,
              'Recall':0,
              'F-measure':0,'CorrectMorphemes':0,
              'CorrectTags':0}
    with open('evaluation.txt', 'w', encoding='utf-8') as file:
        for key in evaluation:
            file.write(' '.join([key, '=', str(evaluation[key]), '\n']))
    return evaluation


def evaluate(file, standard): # evaluates two given texts
    file = file.strip()
    f_lines = file.split('\n')
    standard = standard.strip()
    s_lines = standard.split('\n')
    s_length = len(s_lines)
    if len(f_lines) != s_length: # check that the files have the same number of lines
        with open('evaluation.txt', 'a', encoding='utf-8') as file:
            file.write('\nError: wrong number of lines')
        return False
    else:
        for i in range(s_length):
            s_line = s_lines[i].strip()
            f_line = f_lines[i].strip()
            if not s_line: # check that either lines are both non-empty or both empty
                if not f_line:
                    continue
                else:
                    with open('evaluation.txt', 'a', encoding='utf-8') as file:
                        file.write(f'\nError: bad line {i+1}')
            elif not f_line:
                with open('evaluation.txt', 'a', encoding='utf-8') as file:
                        file.write(f'\nError: bad line {i+1}')

def main():
    initialize_evaluation()
    evaluate('a\n\n\nb','a\n\n\nc')

if __name__ == '__main__':
    main()
