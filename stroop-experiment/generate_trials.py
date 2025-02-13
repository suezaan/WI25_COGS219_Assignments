def generate_trials(subj_code, seed, num_repetitions=25):
    '''
    _doc_: Writes a file named {subj_code_}trials.csv, one line per trial. 
    Creates a trials subdirectory if one does not exist
    
    subj_code: a string corresponding to a participant's unique subject code
    seed: an integer specifying the random seed
    num_repetitions: integer specifying total times that combinations of trial type (congruent vs. incongruent) and orientation (upright vs. upside_down) should repeat (total number of trials = 4 * num_repetitions) 
    '''
    import os
    import random

    # define general parameters and functions here
    stimuli = ['red', 'orange', 'yellow', 'green', 'blue'] 
    colors =  ['red', 'orange', 'yellow', 'green', 'blue']
    trial_types = ['congruent', 'incongruent']
    orientations = ['upright','upside_down']
    num_repetitions = int(num_repetitions)

    # set seed
    random.seed(int(seed))

    # define a function for incongrunt trial
    def make_incongruent(color,stimuli): # return cur_word a color (x stimuli)
        other_colors = [stimulus for stimulus in stimuli if stimulus != color]
        incongruent_color = random.choice(other_colors)
        return incongruent_color

    # create trials folder if it doesn't already exist
    try:
        os.mkdir('trials')
    except FileExistsError:
        print('opening file...')
    f = open(f'trials/{subj_code}_trials.csv','w')

    # write.header
    separator=','
    header = separator.join(['subj_code','seed','word','color','trial_type','orientation'])
    f.write(hearder+'\n')

    # write code to loop through creating and adding trials to the file here
    trials = []
    for i in range(num_repetitions):
        for cur_trial_type in trial_types:
            for cur_orientation in orientations:
                cur_word = random.choice(colors) # choose word 
                if cur_trial_type == 'incongruent':
                    cur_color = make_incongruent(cur_word,colors) 
                else:
                    cur_color = cur_word # match word and color (congruent trial)
                trials.append([subj_code,seed,cur_word,cur_trial_type,cur_orientation])

    # shuffle
    random.shuffle(trials)

    # write trials to file
    for cur_trial in trials:
        f.write(separator.join(map(str,cur_trial))+'\n')

    # close the file
    f.close()
