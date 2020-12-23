import re
import random

source = "words.txt"

f = open("words.txt", "r", encoding ="utf-8")
data = f.read()

english_words = re.findall("[a-z]+", data)
ja = re.findall("\t.*\n", data)

meanings = []
for word in ja:
  meanings.append(re.sub("\t|\n", "", word))

words_dict = dict(zip(english_words, meanings))

n_questions = 50

with open("英単語テスト_01.txt", "w") as f:
  f.write("第1回英単語テスト\n\n")

  for question_num in range(n_questions):
    question_word = random.choice(english_words)
    correct_answer = words_dict[question_word]

    meanings_copy = meanings.copy()
    meanings_copy.remove(correct_answer)
    wrong_answers = random.sample(meanings_copy, 3)
    answer_options = [correct_answer] + wrong_answers

    random.shuffle(answer_options)
    
    f.write("問{}. {}\n\n".format(question_num+1, question_word))
    for i in range(4):
      f.write("{}. {}\n".format(i+1, answer_options[i]))
    f.write("\n\n")