from ans.answer import Answer
from ans.user import User

if __name__ == "__main__":
    answer = Answer()
    user = User(answer.digit)
    while True:
        input_number = user.input_num()
        print(input_number)
