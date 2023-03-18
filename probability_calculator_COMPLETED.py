import copy
import random
# Consider using the modules imported above.
# cleaned/removed comments. Rough version/development is commented out at the bottom
class Hat:
    '''represents a hat with different colored balls'''
    def __init__(self, **kwargs):
        '''initialize all attributes available to each object of Hat'''
        self.color = list(map(lambda x: x, kwargs.keys()))
        self.count = list(map(lambda x: x, kwargs.values())) 
        self.contents = []
        for color, count in zip(self.color, self.count):
            for number in range(count):
                self.contents.append(color)
        self.clone_contents = copy.deepcopy(self.contents) # needed to reset self.contents to original list
        

    def draw(self, number):
        '''removes balls at random'''
        self.drawn_balls = []
        if number <= len(self.contents):
            for num in range(number):
                x = random.choice(self.contents)
                self.contents.remove(x)
                self.drawn_balls.append(x)
            return (self.drawn_balls)
        else:
            return (self.contents)

def experiment(hat, expected_balls={}, num_balls_drawn=0, num_experiments=0):
    '''find probablity for drawn balls to be expected of given colors'''
    expected = Hat(**expected_balls) # this allows us to make a new instance of Hat using given dict of func experiment.
    m = 0
    for experiment_num in range(num_experiments):

        balls_drawn = hat.draw(num_balls_drawn)
        balls_list = [balls for balls in balls_drawn if balls in expected.contents] 
        # all(iterable) returns bool 
        check = all([balls_list.count(ball) >= expected.contents.count(ball) for ball in hat.clone_contents])
      
        if check:
            m += 1
        hat.contents = copy.copy(hat.clone_contents) #reset list for rerun of experiment
    
    return (m / num_experiments)

    






























# class Hat:
#     '''represents a hat with different colored balls'''
#     def __init__(self, **kwargs):
#         '''initialize all attributes available to each object of Hat'''
#         self.color = list(map(lambda x: x, kwargs.keys())) #kwargs.keys()      # I used lambdas just for more practice
#         self.count = list(map(lambda x: x, kwargs.values())) #kwargs.values()
#         self.contents = []
#         # self.conty = [[x for x in self.color] in range(self.count.pop())] tried using lambdas and different ways of making nested list comps. no luck
#         for color, count in zip(self.color, self.count):
#             for number in range(count):
#                 self.contents.append(color)
#         self.clone_contents = copy.deepcopy(self.contents) # needed to reset self.contents to original list
        

#     # def __repr__(self): # repr has __str__ as one of its 'attributes'
#         # return(f'color is {self.color} number is {self.count} the contents list is {self.contents}')

#     def draw(self, number):
#         '''removes balls at random'''
#         self.drawn_balls = []
#         if number <= len(self.contents):
#             for num in range(number):
#                 x = random.choice(self.contents)
#                 # print(f'length of self.contents{len(self.contents)}')
#                 self.contents.remove(x)
#                 self.drawn_balls.append(x)
#             # print(f'end length of self.contents {len(self.contents)}')
#             return (self.drawn_balls)
#         else:
#             return (self.contents)


# # hat = Hat(blue=5, black=4, green=5)
# # hat.draw(3)

# def experiment(hat, expected_balls={}, num_balls_drawn=0, num_experiments=0):
#    '''find probablity for drawn balls to be expected of given colors'''
#     expected = Hat(**expected_balls) # this allows us to make a new instance of Hat using given dict of func experiment.
#     # for color, count in expected_balls.items():
#     #         for number in range(count):
#     #             expected.append(color)
#     m = 0
#     for experiment_num in range(num_experiments):
#         balls_drawn = hat.draw(num_balls_drawn)
#         balls_list = [balls for balls in balls_drawn if balls in expected.contents] # can have multiple expressions in list comps
#         # if ball in expected.contents:
#         #     for ball in balls_drawn:           convt to list comprehension  lambdas dont work due to us assigning to a variable
#         #         drawn_balls.append(ball)
          # all(iterable) returns bool 
#         check = all([balls_list.count(ball) >= expected.contents.count(ball) for ball in hat.clone_contents])
#         # for balls in hat.clone_contents:
#         #     check = all(drawn_balls.count(balls) >= expected.count(balls))   cont to list comprehension
#         # hat.contents = copy.deepcopy(hat_copy)
#         # if expected.count(color) == balls_drawn.count(color):
#         if check:
#             m += 1
#             # count += 1
#             # print(count)
#             # expected.clear
#         hat.contents = copy.copy(hat.clone_contents)
#     probability = (m / num_experiments)
#     return probability

    

# # experiment(hat,{"blue":3,"black":1}, 3, 7)
           




