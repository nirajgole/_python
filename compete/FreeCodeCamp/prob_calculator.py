import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **hat_contents):
        self.contents = []
        for k, v in hat_contents.items():
            for _ in range(v):
                self.contents.append(k)

    def draw(self, num_balls_drawn):
        ball_len = len(self.contents)
        if num_balls_drawn >= ball_len:
            return self.contents
        else:
            return random.sample(self.contents, num_balls_drawn)

        # r = []
        # for _ in range(0, num_balls_drawn):
        #     bid = random.randint(0, ball_len - 1)
        #     r.append(self.contents.pop(bid))
        #     ball_len -= 1

        # return r


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    draw_match_count = 0
    for _ in range(num_experiments):
        h=copy.deepcopy(hat)
        drawn_balls = h.draw(num_balls_drawn)
        flag = True
        for k, v in expected_balls.items():
            if drawn_balls.count(k) < v:
                flag = False
                break
        draw_match_count += flag
    return draw_match_count/num_experiments


hat = Hat(black=6, red=4, green=3)
print(hat.contents)
probability = experiment(hat=hat,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=5,
                         num_experiments=2000)
print(probability)

# hat_1 = Hat(red=5, blue=2)
# print(hat_1.contents)
# actual = hat_1.draw(2)
# print(actual)
# hat = Hat(red=5, blue=2)
# actual = hat.draw(2)
# print(actual)
# expected = ['blue', 'red']
# print(len(hat.contents))

hat = Hat(yellow=5, red=1, green=3, blue=9, test=1)
probability = experiment(hat=hat, expected_balls={
    "yellow": 2, "blue": 3, "test": 1}, num_balls_drawn=20, num_experiments=100)
print(len(hat.contents))
print(probability)  # expected = 1.0
