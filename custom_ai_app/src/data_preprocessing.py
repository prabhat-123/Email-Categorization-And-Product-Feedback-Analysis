import json
import random 
import pandas as pd
import config as cfg

def text_reader(file_path):
    """
    Read a text file and split it into paragraphs.

    This function takes the path to a text file as input, reads the file line by
    line, and splits it into paragraphs based on consecutive empty lines (6 or more).
    Each paragraph is added to a list and returned.

    Args:
        file_path (str): The path to the text file to be read.

    Returns:
        list: A list of paragraphs extracted from the text file.
    """
    paragraphs = []
    with open(file_path, 'r') as file:
        paragraph = ''
        consecutive_newlines = 0
        for line in file:
            if line.strip():  
                paragraph += line
                consecutive_newlines = 0  
            else:
                consecutive_newlines += 1 
                if consecutive_newlines >= 6:
                    if paragraph:
                        paragraphs.append(paragraph.strip()) 
                        paragraph = ''  
                    consecutive_newlines = 0  
        if paragraph:
            paragraphs.append(paragraph.strip())
    return paragraphs


def replace_greetings(paragraph, greetings_phrases):
    """
    Replace greetings phrases in a paragraph with empty strings.

    This function takes a paragraph and a list of greetings phrases as input.
    It searches for occurrences of the greetings phrases within the paragraph
    and replaces them with empty strings, effectively removing the greetings.

    Args:
        paragraph (str): The paragraph containing text that may include greetings.
        greetings_phrases (list): A list of greetings phrases to be replaced.

    Returns:
        str: The modified paragraph with greetings phrases removed.
    """
    for phrase in greetings_phrases:
        if phrase in paragraph:
            paragraph = paragraph.replace(phrase, "")
    return paragraph

def replace_dissatisfaction_phrases(paragraph, replacable_dis_phrases,
                                    dissatisfaction_phrases):
    """
    Replace replaceable dissatisfaction phrases in a paragraph with random dissatisfaction phrases.

    This function takes a paragraph, a list of replaceable dissatisfaction phrases, and a list
    of potential dissatisfaction phrases as input. It searches for occurrences of the replaceable
    dissatisfaction phrases within the paragraph and randomly replaces them with phrases from the
    list of potential dissatisfaction phrases.

    Args:
        paragraph (str): The paragraph containing text that may include replaceable dissatisfaction phrases.
        replacable_dis_phrases (list): A list of replaceable dissatisfaction phrases to be replaced.
        dissatisfaction_phrases (list): A list of potential dissatisfaction phrases for replacement.

    Returns:
        str: The modified paragraph with replaceable dissatisfaction phrases replaced.
    """
    for phrase in replacable_dis_phrases:
        if phrase in paragraph:
            replacement = random.choice(dissatisfaction_phrases)
            paragraph = paragraph.replace(phrase, replacement, 1)
    return paragraph


def replace_help_phrases(paragraph, replacable_help_phrases, help_phrases):
    """
    Replace replaceable help phrases in a paragraph with random help phrases.

    This function takes a paragraph, a list of replaceable help phrases, and a list
    of potential help phrases as input. It searches for occurrences of the replaceable
    help phrases within the paragraph and randomly replaces them with phrases from the
    list of potential help phrases.

    Args:
        paragraph (str): The paragraph containing text that may include replaceable help phrases.
        replacable_help_phrases (list): A list of replaceable help phrases to be replaced.
        help_phrases (list): A list of potential help phrases for replacement.

    Returns:
        str: The modified paragraph with replaceable help phrases replaced.
    """
    for phrase in replacable_help_phrases:
        if phrase in paragraph:
            replacement = random.choice(help_phrases)
            paragraph = paragraph.replace(phrase, replacement, 1)
    return paragraph

def replace_expressions_of_thanks(paragraph, 
                                  replacable_exp_of_thanks_phrases, 
                                  expressions_of_thanks):
    """
    Replace replaceable expressions of thanks phrases in a paragraph with random expressions of thanks.

    This function takes a paragraph, a list of replaceable expressions of thanks phrases, and a list
    of potential expressions of thanks as input. It searches for occurrences of the replaceable
    expressions of thanks phrases within the paragraph and randomly replaces them with phrases from the
    list of potential expressions of thanks.

    Args:
        paragraph (str): The paragraph containing text that may include replaceable expressions of thanks phrases.
        replacable_exp_of_thanks_phrases (list): A list of replaceable expressions of thanks phrases to be replaced.
        expressions_of_thanks (list): A list of potential expressions of thanks for replacement.

    Returns:
        str: The modified paragraph with replaceable expressions of thanks phrases replaced.
    """
    for phrase in replacable_exp_of_thanks_phrases:
        if phrase in paragraph:
            replacement = random.choice(expressions_of_thanks)
            paragraph = paragraph.replace(phrase, replacement, 1)
    return paragraph


def replace_happy_subjects(paragraph, replacable_happy_subjects, happy_subjects):
    """
    Replace replaceable happy subjects in a paragraph with random happy subjects.

    This function takes a paragraph, a list of replaceable happy subjects, and a list
    of potential happy subjects as input. It searches for occurrences of the replaceable
    happy subjects within the paragraph and randomly replaces them with phrases from the
    list of potential happy subjects.

    Args:
        paragraph (str): The paragraph containing text that may include replaceable happy subjects.
        replacable_happy_subjects (list): A list of replaceable happy subjects to be replaced.
        happy_subjects (list): A list of potential happy subjects for replacement.

    Returns:
        str: The modified paragraph with replaceable happy subjects replaced.
    """
    for phrase in replacable_happy_subjects:
        if phrase in paragraph:
            replacement = random.choice(happy_subjects)
            paragraph = paragraph.replace(phrase, replacement, 1)
    return paragraph


if __name__ == "__main__":
    json_file =  open('phrase_alternatives.json', 'r')
    json_data = json.load(json_file)
    greetings_phrases = json_data["greetings_phrases"]
    dissatisfaction_phrases = json_data["dissatisfaction_phrases"]
    replacable_dis_phrases = json_data["replacable_dis_phrases"]
    help_phrases = json_data["help_phrases"]
    replacable_help_phrases = json_data["replacable_help_phrases"]
    expressions_of_thanks = json_data["expressions_of_thanks"]
    replacable_exp_of_thanks_phrases = json_data["replacable_exp_of_thanks_phrases"]
    happy_subjects = json_data["happy_subjects"]
    replacable_happy_subjects = json_data["replacable_happy_subjects"]
    paragraphs = text_reader(file_path = cfg.TEXT_FILE_PATH)
    for i, paragraph in enumerate(paragraphs):
        paragraph = replace_greetings(paragraph, greetings_phrases)
        paragraph = replace_dissatisfaction_phrases(paragraph, 
                                                    replacable_dis_phrases,
                                                    dissatisfaction_phrases
                                                    )
        paragraph = replace_help_phrases(paragraph, 
                                         replacable_help_phrases,
                                         help_phrases
                                         )
        paragraph = replace_expressions_of_thanks(paragraph,
                                                  replacable_exp_of_thanks_phrases,
                                                  expressions_of_thanks)
        paragraph = replace_happy_subjects(paragraph,
                                           replacable_happy_subjects,
                                           happy_subjects)
        paragraphs[i] = paragraph
        df = pd.read_csv(cfg.RAW_DATA_PATH)
        for i in range(len(df)):
            df.iloc[i, 2] = paragraphs[i]
        df.to_csv(cfg.CLEAN_DATA_PATH, index=False)



