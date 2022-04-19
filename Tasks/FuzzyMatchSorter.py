from fuzzywuzzy import fuzz
from fuzzywuzzy import process


def rank_candidates(input_string: str, list_of_candidates: list) -> dict:
    """
    Give rank to each tuple in the given list
    :param input_string: fuzzy phrase
    :param list_of_candidates: list of object which will be candidates for the similarity operation.
    :return: dictionary with tuple of first and last names as key and a score as value.
    """
    output = {}

    for candidate in list_of_candidates:
        full_name_string = ' '.join(candidate)
        output[candidate] = fuzz.token_sort_ratio(full_name_string, input_string)

    return output


def sort_by_rank(ranked_candidates: dict) -> list:
    """
    Sorting candidates by their rank
    :param ranked_candidates:list of object which will be candidates for the similarity operation.
    :return: sorted list by the values of the dictionary.
    """
    return sorted(ranked_candidates.items(), key=lambda x: x[1], reverse=False)


def fuzzy_sort_and_match(input_string: str, list_of_candidates: list) -> list:
    """
    Searching for similar phrases upon the given input string, sort them by their rank and return them.
    :param input_string: fuzzy phrase
    :param list_of_candidates: list of object which will be candidates for the similarity operation.
    :return: list of sorted objects by their similarity rank.
    """

    ranked_candidates = rank_candidates(input_string, list_of_candidates)
    sort_candidates = sort_by_rank(ranked_candidates)

    return sort_candidates
