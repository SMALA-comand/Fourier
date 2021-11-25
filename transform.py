import math


def compute_pol(a0, a1, om):
    x = []
    for i in range(0, len(a0)):
        x.append(pow(om, i*2))

    first = 0
    second = 0
    for i in range(0, len(a0)):
        first += a0[i]*x[i]
        second += a1[i]*x[i]

    return first + om*second


def fft(values):
    """

    :param values:
    :return:
    """
    while math.log2(len(values)) < math.ceil(math.log2(len(values))):
        values.append(0)

    n = len(values)
    omega = math.e ** (2 * math.pi * 1j / n)

    ans = [0]*n
    omg = [0]*n
    omg[0] = pow(omega, 0)
    for i in range(1, n):
        omg[i] = omg[i-1] * omega

    a0 = [values[i] for i in range(0, n, 2)]
    a1 = [values[i] for i in range(1, n, 2)]

    for i in range(0, n):
        x = omg[i]
        ans[i] = compute_pol(a0, a1, x)

    return ans, omg


if __name__ == '__main__':
    val = [1, 3, 2, 7, 5, 4, 3]
    a = fft(val)
    print(a)

