import math

test_cases = int(input())

for case in range(test_cases):
    v_0, theta, x_1, h_1, h_2 = input().split()

    v_0 = float(v_0)
    theta = float(theta)
    x_1 = float(x_1)
    h_1 = float(h_1)
    h_2 = float(h_2)
    g = 9.81


    for t in range(20):
        x_t = v_0*t*math.cos(theta)
        y_t = v_0*t*math.sin(theta)-1/2*g*t**2
        print(x_t, y_t)