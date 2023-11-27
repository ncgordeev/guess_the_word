from config import WORDS_PATH, HISTORY_PATH
from functions.functions import load_data, mixing_word, save_statistic, get_statistic

if __name__ == '__main__':
    """
    Main function for this game
    """
    user_name = input("Please, enter your name ").capitalize()
    print(f"Hi, {user_name}! Let's start! Guess the word: ")
    user_score = 0
    words_list = load_data(WORDS_PATH)
    for word in words_list:
        word = word.rstrip()
        sample_word = mixing_word(word)
        user_answer = input(f"Use the correct word instead of the hidden one - {sample_word} \n")
        if user_answer == word:
            print(f"Right answer. You get 10 points!")
            user_score += 10
        else:
            print(f"Wrong! Right answer is - {word}")
    print(f"{user_name}, thank you for the game! Your score is {user_score}")
    user_statistic = f"{user_name} {user_score}\n"
    save_statistic(HISTORY_PATH, user_statistic)
    history = load_data(HISTORY_PATH)
    print(get_statistic(history))
