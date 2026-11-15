
import json
from pathlib import Path
from main import Quiz, quizzes


class QuizGame:
    def __init__(self):
        self.file = Path(__file__).with_name("state.json")
        self.quizzes = quizzes.copy()
        self.best_score = None
        self.load()

    def load(self):
        if not self.file.exists():
            return

        try:
            with self.file.open("r", encoding="utf-8") as f:
                data = json.load(f)

            loaded = []
            for item in data["quizzes"]:
                if not isinstance(item["question"], str):
                    raise ValueError("잘못된 문제")
                if len(item["choices"]) != 4:
                    raise ValueError("선택지는 4개여야 합니다")
                if not all(isinstance(c, str) for c in item["choices"]):
                    raise ValueError("잘못된 선택지")
                if type(item["answer"]) is not int or not 1 <= item["answer"] <= 4:
                    raise ValueError("잘못된 정답")
                loaded.append(
                    Quiz(item["question"], item["choices"], item["answer"])
                )

            best = data["best_score"]
            if best is not None and (
                type(best) is not int or best < 0 or best > 100
            ):
                raise ValueError("잘못된 점수")

            self.quizzes = loaded
            self.best_score = best
            print("저장된 데이터를 불러왔습니다.")

        except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError):
            print("저장 파일 오류: 기본 퀴즈로 시작합니다.")

    def save(self):
        data = {
            "quizzes": [
                {
                    "question": q.question,
                    "choices": q.choices,
                    "answer": q.answer
                }
                for q in self.quizzes
            ],
            "best_score": self.best_score
        }

        try:
            temp = self.file.with_suffix(".tmp")
            with temp.open("w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            temp.replace(self.file)
        except OSError as e:
            print("파일 저장 실패:", e)

    def read_number(self, prompt, minimum, maximum):
        while True:
            value = input(prompt).strip()
            try:
                number = int(value)
                if minimum <= number <= maximum:
                    return number
            except ValueError:
                pass
            print(f"{minimum}~{maximum} 사이 숫자를 입력하세요.")

    def play(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0
        for i, q in enumerate(self.quizzes, 1):
            print(f"\n[문제 {i}/{len(self.quizzes)}]")
            q.show()
            answer = self.read_number("정답 (1~4): ", 1, 4)
            if q.check(answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답: {q.answer}번")

        percent = round(score / len(self.quizzes) * 100)
        print(f"결과: {score}/{len(self.quizzes)} ({percent}점)")

        if self.best_score is None or percent > self.best_score:
            self.best_score = percent
            print("새로운 최고 점수입니다!")
        self.save()

    def add_quiz(self):
        print("\n새로운 퀴즈 추가")

        while True:
            question = input("문제: ").strip()
            if question:
                break
            print("문제를 입력하세요.")

        choices = []
        for i in range(4):
            while True:
                choice = input(f"선택지 {i + 1}: ").strip()
                if choice:
                    choices.append(choice)
                    break
                print("선택지를 입력하세요.")

        answer = self.read_number("정답 번호 (1~4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        self.save()
        print("퀴즈가 추가되었습니다.")

    def show_list(self):
        print(f"\n등록된 퀴즈: {len(self.quizzes)}개")
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
        for i, q in enumerate(self.quizzes, 1):
            print(f"{i}. {q.question}")

    def show_score(self):
        if self.best_score is None:
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"최고 점수: {self.best_score}점")

    def run(self):
        try:
            while True:
                print("\n=== Codyssey Quiz Game ===")
                print("1. 퀴즈 풀기")
                print("2. 퀴즈 추가")
                print("3. 퀴즈 목록")
                print("4. 점수 확인")
                print("5. 종료")

                choice = self.read_number("선택: ", 1, 5)

                if choice == 1:
                    self.play()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_list()
                elif choice == 4:
                    self.show_score()
                elif choice == 5:
                    break

        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 안전하게 종료합니다.")
        finally:
            self.save()
            print("프로그램 종료")


if __name__ == "__main__":
    QuizGame().run()
