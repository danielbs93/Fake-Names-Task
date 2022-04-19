import time
from pprint import pprint

from scrapper.generator import NamesGenerator
from NamesSimilarity import find_3_top_similar_names
from config import configApp

if __name__ == '__main__':
    names_scrapper = NamesGenerator()
    fake_names = None

    t0 = time.time()

    if names_scrapper.populate_names_from_url():

        # Get random names from the provided URL
        fake_names = names_scrapper.names

        # Get the fuzzy name
        input_string = configApp.INPUT_STRING

        # Print top 3 similar names according to the given fuzzy name
        top_3 = find_3_top_similar_names(input_string=input_string, fake_names=fake_names)
        top_3.reverse()

        print(f'Fuzzy word: {input_string}')
        print([f'{record[0]} with rank: {record[1]}' for record in top_3], sep="\n")

        print(f'Total time of operation: {round(time.time() - t0, 2)} seconds')

    else:
        print("Failed to scrap names")

