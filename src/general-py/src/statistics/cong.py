def congruent_polynomial(range_, natural_N):
    expression = [(35 - (3 * i)) / 10 for i in range(1, range_ + 1)]
    return [[(i + 1), expression[i]] for i in range(len(expression)) if expression[i] in natural_N]


R = 10  # 1 < z <= 10
N = [(i + 1) for i in range(R)]
result = congruent_polynomial(R, N)[0]

result.insert(0, (R - result[0] - result[1]))
print(f"x, y, z: {set(r_i for r_i in result)}")
