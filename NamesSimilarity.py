from Tasks.FuzzyMatchSorter import *


def find_3_top_similar_names(input_string: str, fake_names: list) -> list:
    """
    Finding the top 3 similar names to the given input string.
    :param input_string: fuzzy name
    :param fake_names: list of tuples (first name, last name)
    :return: top 3 similar names to the fuzzy name
    """
    ranked_list = fuzzy_sort_and_match(input_string=input_string, list_of_candidates=fake_names)
    return ranked_list[-3:]
