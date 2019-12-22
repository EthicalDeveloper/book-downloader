import csv
import requests
import tqdm


def get_catalog():
    with open('./catalog.csv') as catalog_csv:
        records = []
        for record in csv.DictReader(catalog_csv):
            records.append(record)
        return records
    




def get_fulltext_url(ebook_no):
    base_url = 'http://aleph.gutenberg.org'
    directory = '/'.join(ebook_no[:-1])
    print("Process...")
    yield f'{base_url}/{directory}/{ebook_no}/{ebook_no}.txt'
    yield f'{base_url}/{directory}/{ebook_no}/{ebook_no}-0.txt'


def fetch_fulltext(ebook_no):
    for url in get_fulltext_url(ebook_no):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text

        except requests.HTTPError:
            continue

    raise LookupError("Cannot find this book" + ebook_no)


def save_fulltext(ebook_no, text):
    with open('./books/' + ebook_no + '.txt', 'w') as book_txt:
        book_txt.write(text)

    



def main():
    
    for record in tqdm.tqdm(get_catalog()):
       ebook_no = record["ebook_no"]
       print(ebook_no,record)
       text = fetch_fulltext(ebook_no)
       save_fulltext(ebook_no,text)



if __name__ == "__main__":
    main()
