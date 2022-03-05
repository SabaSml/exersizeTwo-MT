snakelength = int(input("enter the number of ur snake \n"))
snakeBody = "🟨"
bodySnake = "🟩"

for i in range(snakelength):
    if (i % 2 == 1):
        print(snakeBody, end="")
    else:
        print(bodySnake, end="")