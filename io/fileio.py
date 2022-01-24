## 덮어쓰기, 새로 쓰기
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 30", file=score_file)
score_file.close()

## append
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 100\n")
score_file.write("사회 : 70")
score_file.close()

## read
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True: 
    line = score_file.readline()
    if not line:
        break
    print(line, end = "")
print()
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines: 
    print(line, end="")
print()
score_file.close()
