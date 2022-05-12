"""
Implementation by @Chonsawat Nakanam

"""

import argparse

parser = argparse.ArgumentParser(description='Input x1 x2 [threshold].')
parser.add_argument('-x1', '--data1', type=int, help='an integer for the x1')
parser.add_argument('-x2', '--data2', type=int, help='an integer for the x2')
parser.add_argument('-w1', '--weight1', type=float, help='an float of weight for the x1', default=1.5)
parser.add_argument('-w2', '--weight2', type=float, help='an float of weight for the x2', default=0.5)
parser.add_argument('-t', '--threshold', type=float, help='an threshold for the prediction')
parser.add_argument('-v', '--verbose', action='store_true')
args, unknown = parser.parse_known_args()


def get_u(x1, x2, w1=1.5, w2=0.5):
    return w1 * x1 + w2 * x2


def predict(u, threshold=0.5):
    if u >= threshold:
        pred = 1
    elif u < threshold:
        pred = 0
    else:
        raise ValueError("Value `u` cannot compare with `threshold`")
    return pred


x1 = args.data1
x2 = args.data2
w1 = args.weight1
w2 = args.weight2
threshold = args.threshold

if args.verbose:
    if threshold:
        print(f"Predict: {predict(get_u(x1,x2), threshold)}")
    else:
        print(f"Predict: {predict(get_u(x1, x2))}")