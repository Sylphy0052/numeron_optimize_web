from ans.answer import Answer
from ans.user import User

if __name__ == "__main__":
    answer = Answer()
    user = User(answer.digit)
    while True:
        input_number = user.input_num()
        n_hit, n_blow = answer.answer(input_number)
        print(f"{n_hit}Hit {n_blow}Blow")
        if n_hit == 4:
            print("Correct numbers!!")
            break
