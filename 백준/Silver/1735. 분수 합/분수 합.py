import sys
A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())
def Greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def Least_Common_Multiple (numb1, numb2) :
    gcd = Greatest_common_divisor(numb1, numb2)
    lcm = int(numb1 * numb2 / gcd)

    return lcm

denominator = Least_Common_Multiple(B,D)
numerator = (A*(denominator // B))+ (C*(denominator // D))

# 기약분수로 만들기`

gcd = Greatest_common_divisor(numerator, denominator)

numerator = numerator// gcd
denominator = denominator // gcd

print(numerator, denominator)
