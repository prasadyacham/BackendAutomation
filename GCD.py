import sys

def _greatest_common_divisor_euclid(p,q):
    if q==0:
        return p
    else:
        remainder = p%q
        return _greatest_common_divisor_euclid(q,remainder)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map (int, input.split())
    print (_greatest_common_divisor_euclid(a,b))