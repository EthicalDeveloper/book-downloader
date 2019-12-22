from gather import get_catalog 
from nltk.tokenize import word_tokenize as tokenize
import tqdm



def load_fulltext(ebook_no):
     with open(f'./books/{ebook_no}.txt', "r", encoding = 'utf-8') as fh:
         return fh.read()






def get_search_index():
    index = {}
    for record in get_catalog():
        ebook_no = record['ebook_no']
        text = load_fulltext(ebook_no)
        for word in tokenize(text):
            if word not in index:
                index[word] = []
            index[word].append(ebook_no)
 

    return index



def select_candidates(index, query):
    candidates = []
    for word in word_tokenize(query):
        if word in index:
            for ebook_no in index[word]:
                candidates.append(ebook_no)
    return candidates


def print_results(candidates):
    records = {}
    for record in get_catalog():
        records[record['ebook_no']] = record

    for ebook_no in candidates:
        record = get_record[ebook_no]
        print (f'{record["title"]} by {record["author"]}')







def main():
    index = get_search_index()
    query = input ("Query:")
    candidates = select_candidates(index, query)

    print_results(candidates)


if __name__ == "__main__":
    main()