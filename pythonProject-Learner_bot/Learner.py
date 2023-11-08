import json
import sys
from difflib import get_close_matches

# ANSI colors
RESET = "\033[0m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
YELLOW = "\033[1;33m"


def load_knowledge_base(file_path: str) -> dict:
    """
    Load the `json` file
    :param file_path: The file path to the `json` file
    :return: The data dictionary
    """
    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data


def save_knowledge_base(file_path: str, data: dict) -> None:
    """
    Save all data in the memory
    :param file_path: The file path to the `json` file
    :param data: The provided data
    :return: None
    """
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions):
    """
    Find the most suitable answers
    :param user_question: The question of a user
    :param questions: The list of questions
    :return: The best match or None
    """
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict):
    """
    Get answer for the question
    :param question: The asked question
    :param knowledge_base: The data `json` file
    :return: The answer or None
    """
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None


def chat_bot() -> None:
    """
    Create chatbot which learns with responses
    :return: None
    """
    knowledge_base: dict = load_knowledge_base("knowledge_base.json")

    while True:
        user_input: str = input("You: ")
        if user_input.casefold() == "quit":
            break
        best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f"Bot: {answer}")
        else:
            print("Bot:", GREEN, "I do not know the answer. Could you teach me?", RESET)
            new_answer: str = input("Type the answer or \"skip\" to skip: ")

            if new_answer.casefold() != "skip":
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base("knowledge_base.json", knowledge_base)
                print("Bot: ", GREEN, "Thank you! I learned a new response!", RESET)


if __name__ == "__main__":
    try:
        chat_bot()
    except KeyboardInterrupt:
        print(RED, "\rCode interrupted!", RESET, end="")
        sys.exit(1)
