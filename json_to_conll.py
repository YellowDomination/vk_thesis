import codecs
import json
from nltk.tokenize import wordpunct_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import wordnet



nltk.download('maxent_treebank_pos_tagger')
nltk.download('punkt')
nltk.download('wordnet')


def dummy_tagger(tokens):
    return ['dummy_tag' for token in tokens]

tagger = nltk.data.load('taggers/maxent_treebank_pos_tagger/english.pickle')
#tagger = dummy_tagger
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def get_bio_tag(w_start, w_end, entities):
    for key, entity in entities.items():
        if not isinstance(entity['start'], int):
            raise Exception("Entitie start must be an integer")
        if 'end'not in entity or not isinstance(entity['end'], int):
            raise Exception("Entities end must be an integer")
        start = entity['start']
        end = entity['end']
        if entity['entity'] == 'Disease' or entity['type'] in ['Drugname']:
            if w_start > start and w_end <= end:
                adding = 'DIS' if entity['entity'] == 'Disease' else 'MED'
                return 'I-' + adding
            elif w_start == start and w_end <= end:
                adding = 'DIS' if entity['entity'] == 'Disease' else 'MED'
                return 'B-' + adding
    return 'O'

def get_token_position_in_text(token, w_start, text):
    delimitter_start = None
    while text[w_start:w_start+len(token)] != token or (delimitter_start == None and w_start != 0):
        w_start += 1
        delimitter_start = delimitter_start or w_start
    return w_start, w_start + len(token), text[delimitter_start:w_start]


def json_to_conll(corpus_json_location, output_location, by_sent = False):
    with codecs.open(corpus_json_location, encoding='utf-8') as in_file:
        reviews = map(json.loads, in_file.readlines())

    with codecs.open(output_location, 'w', encoding='utf-8') as out_file:
        for review in reviews:
            documents = sent_tokenize(review['text']) if by_sent else [review['text']]
            w_start = 0
            w_end = 0
            for document in documents:
                tokens = wordpunct_tokenize(document)
                corrected_tokens = tokens # map(correct, tokens)
                pos_tags = tagger.tag(corrected_tokens)
                for token, temp in zip(tokens, pos_tags):
                    token_corr = temp[0]
                    pos_tag = temp[1]
                    w_start, w_end, delimitter = get_token_position_in_text(token, w_start, review['text'])
                    bio_tag = get_bio_tag(w_start, w_end, review['entities'])
                    lemm = lemmatizer.lemmatize(token_corr, get_wordnet_pos(pos_tag))
                    out_file.write(u'{}\t{}\n'.format(token, bio_tag))
                    # out_file.write(u'{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(token, lemm, pos_tag, bio_tag, w_start, w_end, delimitter, review['id']))
                    w_start = w_end - 1
                out_file.write('\n')


def edits1(word):
    s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in s if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in s if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in s for c in alphabet if b]
    inserts    = [a + c + b     for a, b in s for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words):
    return set(w for w in words if w in NWORDS)

def correct(word):
    word = word.lower()
    candidates = known([word]) or known(edits1(word)) or    known_edits2(word) or [word] if word.isalpha() else [word]
    return max(candidates, key=NWORDS.get)


if __name__ == '__main__':
    json_to_conll('datasets/ChemText/0/test.json',  'datasets/ChemText/0/test.txt', by_sent = True)
    json_to_conll('datasets/ChemText/0/train.json', 'datasets/ChemText/0/train.txt', by_sent = True)
    json_to_conll('datasets/ChemText/1/test.json',  'datasets/ChemText/1/test.txt', by_sent = True)
    json_to_conll('datasets/ChemText/1/train.json', 'datasets/ChemText/1/train.txt', by_sent = True)
    json_to_conll('datasets/ChemText/2/test.json',  'datasets/ChemText/2/test.txt', by_sent = True)
    json_to_conll('datasets/ChemText/2/train.json', 'datasets/ChemText/2/train.txt', by_sent = True)
    json_to_conll('datasets/ChemText/3/test.json',  'datasets/ChemText/3/test.txt', by_sent = True)
    json_to_conll('datasets/ChemText/3/train.json', 'datasets/ChemText/3/train.txt', by_sent = True)
    json_to_conll('datasets/ChemText/4/test.json',  'datasets/ChemText/4/test.txt', by_sent = True)
    json_to_conll('datasets/ChemText/4/train.json', 'datasets/ChemText/4/train.txt', by_sent = True)