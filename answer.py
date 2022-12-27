from ans.ai import AI
from ans.user import User

if __name__ == "__main__":
    while True:
        digit_s = input("Digit >")
        try:
            digit = int(digit_s)
        except Exception:
            continue
        break
    user = User(digit)
    ai = AI(digit)
    while True:
        input_number = ai.input_num()
        while True:
            ans = input("n_hit,n_blow >")
            ans = ans.rstrip()
            if ans.count(",") != 1:
                continue
            try:
                hit, blow = ans.split(",")
                n_hit, n_blow = int(hit), int(blow)
            except Exception:
                continue
            if 0 <= n_hit <= 4 and 0 <= n_blow <= 4:
                break
        ai.feedback(input_number, n_hit, n_blow)
        print(f"{n_hit}Hit {n_blow}Blow")
        ai.print_option()
        if n_hit == 4:
            break
