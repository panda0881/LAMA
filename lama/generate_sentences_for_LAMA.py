import ujson as json

def triplet_to_sentence(tmp_triplet):
    tmp_relation = tmp_triplet[1]
    if tmp_relation == 'AtLocation':
        return 'You are likely to find ' + tmp_triplet[0] + ' in [MASK].'
    elif tmp_relation == 'CapableOf':
        return tmp_triplet[0] + ' can [MASK].'
    elif tmp_relation == 'Causes':
        return tmp_triplet[0] + ' causes [MASK].'
    elif tmp_relation == 'CausesDesire':
        return tmp_triplet[0] + ' would make you want to [MASK].'
    elif tmp_relation == 'CreatedBy':
        return tmp_triplet[0] + ' is created by [MASK].'
    elif tmp_relation == 'DefinedAs':
        return tmp_triplet[0] + ' is defined as [MASK].'
    elif tmp_relation == 'Desires':
        return tmp_triplet[0] + ' desires [MASK].'
    elif tmp_relation == 'HasA':
        return tmp_triplet[0] + ' has [MASK].'
    elif tmp_relation == 'HasPrerequisite':
        return tmp_triplet[0] + ' requires [MASK].'
    elif tmp_relation == 'HasProperty':
        return tmp_triplet[0] + ' is [MASK].'
    elif tmp_relation == 'HasSubevent':
        return tmp_triplet[0] + ' includes [MASK].'
    elif tmp_relation == 'HasFirstSubevent':
        return tmp_triplet[0] + ' means firstly [MASK].'
    elif tmp_relation == 'HasLastSubevent':
        return tmp_triplet[0] + ' means lastly [MASK].'
    elif tmp_relation == 'InstanceOf':
        return tmp_triplet[0] + ' is an instance of [MASK].'
    elif tmp_relation == 'LocatedNear':
        return tmp_triplet[0] + ' is located near [MASK].'
    elif tmp_relation == 'MadeOf':
        return tmp_triplet[0] + ' is made of [MASK].'
    elif tmp_relation == 'MotivatedByGoal':
        return tmp_triplet[0] + ' is motivated by [MASK].'
    elif tmp_relation == 'PartOf':
        return tmp_triplet[0] + ' is part of [MASK].'
    elif tmp_relation == 'ReceivesAction':
        return tmp_triplet[0] + ' can be [MASK].'
    elif tmp_relation == 'UsedFor':
        return tmp_triplet[0] + ' is used for [MASK].'
    elif tmp_relation == 'IsA':
        return tmp_triplet[0] + ' is [MASK].'
    elif tmp_relation == 'NotIsA':
        return tmp_triplet[0] + ' is not [MASK].'
    elif tmp_relation == 'NotHasProperty':
        return tmp_triplet[0] + ' is not [MASK].'
    elif tmp_relation == 'NotCapableOf':
        return tmp_triplet[0] + ' cannot [MASK].'
    elif tmp_relation == 'RelatedTo':
        return tmp_triplet[0] + ' is related to [MASK].'
    else:
        print('We do not have pattern for relation:', tmp_relation)

all_triplets = list()
with open('test_e.txt', 'r') as f:
    for line in f:
        tmp_words = line[:-1].split('\t')
        all_triplets.append((tmp_words[1], tmp_words[0], tmp_words[2]))

all_sentences = list()
for tmp_triplet in all_triplets:
    all_sentences.append(triplet_to_sentence(tmp_triplet))

with open('test_e_sentences.json', 'w') as f:
    json.dump(all_sentences, f)



print('end')
