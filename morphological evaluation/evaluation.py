import os


evaluation = {'Precision':0,
              'Recall':0,
              'F-measure':0,'CorrectMorphemes':0,
              'CorrectTags':0}

def input_files(): # Opens and reads input files
    stan = 'standard'
    test = 'test'
    files = {stan:[], test:[]}
    for key in files:
        f_path = input(f'Input {key} file directory: ')
        f_name = os.path.splitext(os.path.basename(f_path))[0]
        with open(f_path, 'r', encoding='utf-8') as file: # os.path -- make the path universal
            f_text = file.read()
        files[key] += [f_path, f_name, f_text]
    return files

def initialize_evaluation(): # Writes evaluetion file with zero values
    with open('evaluation.txt', 'w', encoding='utf-8') as file:
        for key in evaluation:
            file.write(' '.join([key, '=', str(evaluation[key]), '\n']))

def main():
    print(input_files()['standard'][-1])

if __name__ == '__main__':
    main()
