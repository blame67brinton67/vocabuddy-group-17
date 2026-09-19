import json
import random
from pathlib import Path


def load_vocabulary():
	vocabulary_path = Path(__file__).with_name("vocabularies.json")
	with vocabulary_path.open(encoding="utf-8") as vocabulary_file:
		return json.load(vocabulary_file)


def ask_question(vocabulary):
	english_word, correct_chinese = random.choice(list(vocabulary.items()))
	chinese_words = list(vocabulary.values())
	wrong_choices = [word for word in chinese_words if word != correct_chinese]
	choices = random.sample(wrong_choices, min(3, len(wrong_choices)))
	choices.append(correct_chinese)
	random.shuffle(choices)

	print(f"\nEnglish word: {english_word}")
	labels = "ABCD"
	for label, choice in zip(labels, choices):
		print(f"{label}. {choice}")

	answer = input("Your answer: ").strip().upper()
	correct_label = labels[choices.index(correct_chinese)]
	if answer == correct_label:
		print("Correct!")
	else:
		print(f"Wrong. The correct answer is {correct_label}.")


def main():
	vocabulary = load_vocabulary()
	if not vocabulary:
		print("vocabularies.json is empty.")
		return
	ask_question(vocabulary)


if __name__ == "__main__":
	main()
