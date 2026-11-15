
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        print("\n" + self.question)
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

    def check(self, answer):
        return self.answer == answer


quizzes = [
    Quiz("Python에서 출력하는 함수는?",
         ["input", "print", "open", "len"], 2),
    Quiz("Python에서 리스트를 만드는 기호는?",
         ["{}", "()", "[]", "<>"], 3),
    Quiz("Python에서 조건문을 시작하는 키워드는?",
         ["if", "for", "def", "class"], 1),
    Quiz("Python에서 반복문에 사용하는 키워드는?",
         ["return", "import", "except", "for"], 4),
    Quiz("Python에서 함수를 정의하는 키워드는?",
         ["func", "def", "function", "make"], 2)
]


def play_quiz():
    score = 0

    for quiz in quizzes:
        quiz.show()

        while True:
            try:
                answer = int(input("정답 (1~4): ").strip())
                if 1 <= answer <= 4:
                    break
                print("1~4 사이 숫자를 입력하세요.")
            except ValueError:
                print("숫자를 입력하세요.")

        if quiz.check(answer):
            print("정답입니다!")
            score += 1
        else:
            print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

    print(f"\n결과: {len(quizzes)}문제 중 {score}문제 정답")


if __name__ == "__main__":
    play_quiz()
