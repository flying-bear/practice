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
    evaluation = {'Hits':0,
                  'Deletions':0,
                  'Insertions':0,
                  'CorrectMorphemes':0,
                  'CorrectTags':0}
    with open('log.txt', 'w', encoding='utf-8') as file:
        for key in evaluation:
            file.write(' '.join([key, '=', str(evaluation[key]), '\n']))
    return evaluation


def list_boundaries_and_tags(line_list): # separates tags from morphemes in a given segmentation list
    morphemes = []
    line_data = {'boundaries':set(),
                 'tag_dict': {}}
    for el in line_list:
        segment = el.split('_')
        morphemes.append(segment[0])
        cursor = len(''.join(morphemes))
        line_data['boundaries'].add(cursor)
        if len(segment) == 2:
            tag = segment[1]
        else:
            tag = ''
        line_data['tag_dict'][segment[0]+'_'+str(cursor)] = tag
    return line_data


def compare_boundaries(f_bound, s_bound): # compares two given sets of boundaries
    loc_eval = {'Hits':0, 'Deletions':0, 'Insertions':0}
    loc_eval['Hits'] = len(s_bound.intersection(f_bound))
    loc_eval['Deletions'] = len(s_bound.difference(f_bound))
    loc_eval['Insertions'] = len(f_bound.difference(s_bound))
    return loc_eval


def check_morphs_and_tags(f_tag_dict, s_tag_dict): # compares morphemes and tags given two dicts
    loc_eval = {'CorrectMorphemes':0, 'CorrectTags':0}
    for key in s_tag_dict:
        if key in f_tag_dict:
            loc_eval['CorrectMorphemes'] += 1
            if s_tag_dict[key] == f_tag_dict[key]:
                loc_eval['CorrectTags'] += 1
    return loc_eval


def compare(f_line_list, s_line_list, evaluation):
    f_data = list_boundaries_and_tags(f_line_list)
    f_bound = f_data['boundaries']
    f_tags = f_data['tag_dict']
    s_data = list_boundaries_and_tags(s_line_list)
    s_bound = s_data['boundaries']
    s_tags = s_data['tag_dict']
    b_eval = compare_boundaries(f_bound, s_bound)
    loc_eval = check_morphs_and_tags(f_tags, s_tags)
    loc_eval.update(b_eval)
    for key in evaluation:
        evaluation[key] += loc_eval[key]
    return evaluation

def evaluate(file, standard, ev_dict): # evaluates two given texts
    file = file.strip()
    f_lines = file.split('\n')
    standard = standard.strip()
    s_lines = standard.split('\n')
    s_length = len(s_lines)
    if len(f_lines) != s_length: # check that the files have the same number of lines
        with open('log.txt', 'a', encoding='utf-8') as file:
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
                    with open('log.txt', 'a', encoding='utf-8') as file:
                        file.write(f'\nError: bad line {i+1}')
            elif not f_line:
                with open('log.txt', 'a', encoding='utf-8') as file:
                        file.write(f'\nError: bad line {i+1}')
            else:
                s_list = s_line.split('\t') # list with the word as 0 element
                f_list = f_line.split('\t')
                if s_list[0] != f_list[0]:
                    with open('log.txt', 'a', encoding='utf-8') as file:
                        file.write(f'\nError: bad line {i+1}')
                else:
                    ev_dict = compare(f_list[1:], s_list[1:], ev_dict) # compare segmentation lists (without words)
        return ev_dict

def main():
    evaluation = initialize_evaluation()
    files = input_files()
    print(evaluate(files['test'][2], files['standard'][2], evaluation))

if __name__ == '__main__':
    main()
