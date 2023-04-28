import random
import copy

class Hat:
    def __init__(self, **balls) : 
        self.balls, self.contents, count, self.ball_colors = balls, [], 0, list(balls.keys())
        for color in self.ball_colors: 
            self.ball_color = color
            count += 1
            ball_count = balls[self.ball_color]
            while ball_count > 0 :
                self.contents.append(self.ball_color)
                ball_count -= 1

    def draw(self, draw_number) :
        draw_contents = self.contents
        draw_contents_return = []
        if draw_number > len(draw_contents) :
            draw_contents_return = draw_contents
        else : 
            for i in range(draw_number): 
                draw_ball = random.choice(draw_contents)
                draw_contents.remove(draw_ball)
                draw_contents_return.append(draw_ball)
        return draw_contents_return 

    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    ball_count = []
    for i in hat.balls: 
        ball_count.append(hat.balls[i])

    expected_events_count, expected_colors, expected_number = 0, list(expected_balls.keys()), list(expected_balls.values())

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw_result = hat_copy.draw(num_balls_drawn) 
        expected_events_count += 1
        for color in expected_colors:
            count = draw_result.count(color)
            expect = expected_balls[color]
            if count < expect:
                expected_events_count -= 1
                break
                
    probability = expected_events_count/num_experiments
    
    return probability 
