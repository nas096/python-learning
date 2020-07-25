from Question import Question

question_prompts = [
    "Ai đặt tên cho dòng sông?\n(a) Đen Vâu\n(b) Tác giả\n(c) Bộ giáo dục\n\n",
    "Vector là gì?\n(a) Là số học\n(b) Là hình học\n(c) Hông biết :D\n\n",
    "Ai thông minh hơn học sinh lớp năm\n(a) HS lớp 1\n(b) HS lớp 5\n(c) Người lớn\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got" + str(score) + "/" + str(len(questions)) + "correct"))
run_test(questions)

