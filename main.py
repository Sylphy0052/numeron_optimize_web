from ans.ai import AI
from ans.answer import Answer
from ans.user import User

if __name__ == "__main__":
    answer = Answer()
    user = User(answer.digit)
    ai = AI(answer.digit)
    while True:
        # input_number = user.input_num()
        # input_number = ai.input_random()
        # input_str = ""
        # for n in input_number:
        #     input_str += str(n)
        # print(f"Input {input_str}")
        print(f"Recommend: {ai.recommend_number()}")
        input_number = ai.input_num()
        n_hit, n_blow = answer.answer(input_number)
        ai.feedback(input_number, n_hit, n_blow)
        print(f"{n_hit}Hit {n_blow}Blow")
        print(ai)
        if n_hit == 4:
            print("Correct numbers!!")
            break
