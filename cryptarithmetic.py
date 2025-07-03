from itertools import permutations

def solve_cryptarithmetic():
    letters = 'SENDMORY'
    digits = range(10)

    for perm in permutations(digits, len(letters)):
        assign = dict(zip(letters, perm))

        if assign['S'] == 0 or assign['M'] == 0:
            continue
        send = assign['S']*1000 + assign['E']*100 + assign['N']*10 + assign['D']
        more = assign['M']*1000 + assign['O']*100 + assign['R']*10 + assign['E']
        money = assign['M']*10000 + assign['O']*1000 + assign['N']*100 + assign['E']*10 + assign['Y']

        if send + more == money:
            print("Solution Found:")
            print(f"SEND  = {send}")
            print(f"MORE  = {more}")
            print(f"MONEY = {money}")
            print("Letter-to-digit mapping:", assign)
            return

    print("No solution found.")

if __name__ == "__main__":
    solve_cryptarithmetic()
