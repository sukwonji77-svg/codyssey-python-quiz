# Codyssey Python Quiz Game

## 프로젝트 개요
Python으로 만든 터미널 기반 4지선다 퀴즈 게임입니다.

## 퀴즈 주제 및 선정 이유
Python 기초 문법을 복습하기 위해 선정했습니다.

## 실행 방법
Python 3.10 이상 필요

python3 game.py

## 주요 기능
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 최고 점수 확인
5. 종료

## 파일 구조
- main.py: Quiz 클래스 및 기본 퀴즈
- game.py: QuizGame 클래스 및 메뉴
- state.json: 퀴즈 및 최고 점수 저장
- README.md: 프로젝트 설명
- .gitignore: Git 제외 파일 설정

## 데이터 저장
state.json 파일에 UTF-8로 저장합니다.
quizzes는 문제 목록, best_score는 최고 점수입니다.

## 예외 처리
잘못된 숫자, 빈 입력, Ctrl+C, EOF 및 JSON 파일 오류를 처리합니다.
