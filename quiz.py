
print("=== Codyssey Python Quiz ===")

questions = [
    ["Python에서 화면에 출력하는 함수는?", "print"],
    ["Python에서 사용자 입력을 받는 함수는?", "input"],
    ["Python에서 정수를 나타내는 자료형은?", "int"]
]

score = 0

for question in questions:
    answer = input(question[0] + " ")

    if answer.strip().lower() == question[1]:
        print("정답입니다!")
        score += 1
    else:
        print("오답입니다. 정답:", question[1])

print("====================")
print("최종 점수:", score, "/", len(questions))

print("=== Codyssey Python Quiz ===")

score = 0

answer = input("Q1. Python에서 화면에 글자를 출력하는 함수는? ")

if answer == "print":
    print("정답입니다!")
    score = score + 1
else:
    print("오답입니다. 정답은 print입니다.")

print("최종 점수:", score)
