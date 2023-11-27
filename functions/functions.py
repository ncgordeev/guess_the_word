from random import sample


def load_data(file_path: str) -> list:
    """
    Get the words list from file
    :return:
    """
    with open(file_path, encoding="utf-8") as words:
        return words.readlines()


def mixing_word(word: str) -> str:
    """
    Function for mixing the alphas in the word
    :param word:
    :return: str
    """
    mix_word = sample(word, len(word))
    return "".join(mix_word)


def save_statistic(file_path: str, statistic: str) -> None:
    """
    Function for saving game statistic
    :param file_path:
    :param statistic:
    :return: None
    """
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(statistic)


def get_statistic(statistic: list) -> str:
    """
    Function shows the total games statistics
    :param statistic:
    :return: str
    """
    max_points = 0
    games = len(statistic)
    for i in statistic:
        name, points = i.rstrip().split(" ")
        if int(points) > max_points:
            max_points = int(points)
        print(name, points)
    return f"Total games: {games}\n" f"Max record: {max_points}"
