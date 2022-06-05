# Secret table

table: list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZ']
user_input: str = str(input('Plaintext: ')).upper()
foo: dict = {}

print('Decrypted: ', end='')

for char in user_input:
    t_count: int = 1
    for t in table:
        idx: int = 1
        for c in t:
            if char == c:
                hold: str = f'{t_count}' * idx
                print(hold, end=' ')

                key: str = str(t_count)
                if not key in foo:
                    foo[key] = 0

                foo[key] += 1

            idx += 1
        t_count += 1

for key in foo:
    if foo[key] == max(foo.values()):
        print(f'Max ocurrence: {key}')