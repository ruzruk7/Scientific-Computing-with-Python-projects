#completed budget app at top, bottom commented was the development
class Category:
    '''Class that initializes the budget app'''

    def __init__(self, category):
        '''Initialize instance variables'''
        self.category = category
        self.ledger = []
        self.sum1_balance = 0.0
    
    def __str__(self):
        '''Print the Budget object neatly formatted with all deposits and withdrawals'''
        headers = self.category.center(30, '*')
        descrip = list(map(lambda des: des['description'], self.ledger))
        amou = list(map(lambda amo: float(amo['amount']), self.ledger))
        sum1_balan = (f'{self.sum1_balance:.2f}')

        cat_1  = []
        for amoun, descript in zip(amou, descrip):
                cat_1.append(f'{descript[:23]:<23}{amoun:>7.2f}\n')
        budget_obj = (headers + '\n' + ''.join(cat_1).strip() + '\n' +'sum1: '+ str(sum1_balan))              #(f'{headers}{str(descrip):<23}{str(amou):>7.2f}')  #''.join(headers) + '\n' + ''.join(f'{descrip:<23}') +  ''.join(f'{amou:>7.2f}')
        return budget_obj

    def deposit(self, amount, description=''):
        '''Returns a dict with key amount, description; value numerical_amount, given_description'''
        self.dict1 = {}
        self.dict1["amount"] = amount
        self.dict1["description"] = description
        self.ledger.append(self.dict1)
        self.sum1_balance += amount
    
    def withdraw(self, amount, description=''):
        '''withdraw an amount and proivde a description(optional)'''
        self.dict2= {}
        self.dict2["amount"] = (amount * -1)
        self.dict2["description"] = description
        self.sum1_balance += (amount * -1)
        if self.check_funds(amount): 
            self.ledger.append(self.dict2)
            return print(f'{True}')
        if not self.check_funds(amount):
            return print(f'{False}')


    def get_balance(self):
        '''Return the sum1 balance'''
        return print(self.sum1_balance)
    
    def transfer(self, arbit_amount, diff_cat):
            '''Transfer funds from current category to another category'''
            if self.check_funds(arbit_amount): 
                self.withdraw(arbit_amount, (f'Transfer to {diff_cat.category.title()}'))
                diff_cat.deposit(arbit_amount, f'Transfer from {self.category.title()}')
                return print(f'{True}')
            if not self.check_funds(arbit_amount): 
                return print(f'{False}')
    
    def check_funds(self, amount):
        '''Check whether the entered amount is available'''
        if amount > self.sum1_balance:
            return False
        if amount <= self.sum1_balance: 
            return True


def create_spend_chart(categories):
    '''create a circle graph for all withdrawals from a given category'''
    withdrawals = []
    for category in categories:
        num_hold = 0
        for key in category.ledger:
            if key['amount'] < 0:
                num_hold += (abs(key['amount']))
        withdrawals.append(num_hold)
    sum1 = sum(withdrawals) 
    percent = [x/sum1 * 100 for x in withdrawals]

    catagory_name_length = []
    for category in categories:
        catagory_name_length.append(len(category.category))
    max_cat_name_length = max(catagory_name_length)
    
  
    string = "Percentage spent by category"
    for x in range(100, -1, -10):
        string += "\n" + str(x).rjust(3) + "|"
        for perc in percent:
            if perc > x:
                string += " o "
            else:
                string += "   "
        string += " "
    string += "\n    ----------"
  
    for z in range(max_cat_name_length):
        string += "\n    "
        for x in range(len(categories)):
            if z < catagory_name_length[x]:
                string += " " + categories[x].category[z] + " "
            else:
                string += "   "
        string += " "
    
    return string
    































# class Category:
#     '''Class that initializes the budget app'''

#     def __init__(self, category):
#         '''Initialize instance variables'''
#         self.category = category
#         self.ledger = []
#         self.sum1_balance = 0.0
    
#     def __str__(self):
#         '''Print the Budget object neatly formatted with all deposits and withdrawals'''
#         headers = self.category.center(30, '*')
#         descrip = list(map(lambda des: des['description'], self.ledger))
#         amou = list(map(lambda amo: float(amo['amount']), self.ledger))
#         sum1_balan = (f'{self.sum1_balance:.2f}')
#         # for indx in self.ledger:
#         #     amou.append(indx['amount'])           convt into lambda func :D
#         #     descrip.append(indx['description'])
#         cat_1  = []
#         for amoun, descript in zip(amou, descrip):
#                 cat_1.append(f'{descript[:23]:<23}{amoun:>7.2f}\n')
#         budget_obj = (headers + '\n' + ''.join(cat_1).strip() + '\n' +'sum1: '+ str(sum1_balan))              #(f'{headers}{str(descrip):<23}{str(amou):>7.2f}')  #''.join(headers) + '\n' + ''.join(f'{descrip:<23}') +  ''.join(f'{amou:>7.2f}')
#         return budget_obj

#     def deposit(self, amount, description=''):
#         '''Returns a dict with key amount, description; value numerical_amount, given_description'''
#         self.dict1 = {}
#         self.dict1["amount"] = amount
#         self.dict1["description"] = description
#         self.ledger.append(self.dict1)
#         self.sum1_balance += amount
#         # balance = dic1['amount'] 
#         # self.sum1_balance.append(dic1['amount'])
    
#     def withdraw(self, amount, description=''):
#         self.dict2= {}
#         self.dict2["amount"] = (amount * -1)
#         self.dict2["description"] = description
#         self.sum1_balance += (amount * -1)
#         if self.check_funds(amount): #if self.sum1_balance >= 0:
#             self.ledger.append(self.dict2)
#             return print(f'{True}')
#         if not self.check_funds(amount):# elif self.sum1_balance < 0:
#             return print(f'{False}')


#     def get_balance(self):
#         '''Return the sum1 balance'''
#         # for x in self.ledger:
#         #     for k in x.values():
#         #         if type(k) == int:
#         #             self.sum1_balance.append(k) 
#         # print(f'sum1 is: {math.fsum(self.sum1_balance)}')
#         return print(self.sum1_balance)
    
#     def transfer(self, arbit_amount, diff_cat):
#             '''Transfer funds from current category to another category'''
#             if self.check_funds(arbit_amount): #if (self.sum1_balance - arbit_amount) >= 0:
#                 self.withdraw(arbit_amount, (f'Transfer to {diff_cat.category.title()}'))
#                 diff_cat.deposit(arbit_amount, f'Transfer from {self.category.title()}')
#                 return print(f'{True}')
#             if not self.check_funds(arbit_amount): #elif (self.sum1_balance - arbit_amount) < 0:
#                 return print(f'{False}')
    
#     def check_funds(self, amount):
#         '''Check whether the entered amount is available'''
#         if amount > self.sum1_balance:# if amount is < 0
#             return False
#         if amount <= self.sum1_balance: # if amount is >= 0
#             return True


# def create_withdrawals_chart(categories):
#     '''create a bar graph for all withdrawals from a given category'''
#     withdrawals = []
#     category_name_length = []
#     for category in categories:
#         num_hold = 0
#         for letter in categories: # stores name size of budget obj name in a list
#             category_name_length.append(len(letter.category))
#         max_cat_name_length_cat_name = max(category_name_length)
#     # print(f'length of category obj name is: {max_cat_name_length_cat_name}')
#     for withdraw in category.ledger: # retreives all negative values of key['amount'] and stores absolute value in a list
#         if withdraw['amount'] < 0:
#             withdrawals.append(abs(withdraw['amount']))
#             num_hold += abs(withdraw['amount'])
#     sum1 = sum(withdrawals) # sum1 of withdrawal list to find %
#     percent = [x/sum1 *100 for x in withdrawals]   #stores percentabe amounts in a list using list comprehension     #(lambda i: i/sum1 * 100 for i in withdrawals)
#     # print(percent)
#     # print(num_hold)
#     # print(withdrawals)

#     string = 'Percentage spent by category'
#     for num in range(100, -1, -10): # this loop draws the y-axis at increments of 10
#         string += ('\n' + str(num).rjust(3) + '|')
#         for perc in percent: # this keeps drawing 3 spaces until the 'o' is greater than the range from the 1st for-loop.
#         # print(f'this is perc {perc}')
#             if perc >= num:
#                 string += ' o '
#             else:
#                 string += '   '
#         string += ' '
#     string += '\n    ----------'


#     for x in range(max_cat_name_length_cat_name): # x is a placeholder for us to be able to run the loop for len(budget object)
#         # print(f'xxxxx is{x}')
#         string +='\n    '
#         for c in range(len(categories)):
#             # print(f'ccccc is {c}')
#             if x < category_name_length[c]:   
#                 string += ' ' + categories[c].category[x]+ ' '
#                 # string += '\n    '
#             else:
#                 string += '   '
#         string += ' '
    

#     return print(string.rstrip())

# def create_spend_chart(categories):
#     '''create a circle graph for all withdrawals from a given category'''
#     withdrawals = []
#     for category in categories:
#         num_hold = 0
#         for key in category.ledger:
#             if key['amount'] < 0:
#                 num_hold += (abs(key['amount']))
#         withdrawals.append(num_hold)
#     sum1 = sum(withdrawals) # sum1 of withdrawal list to find %
#     percent = [x/sum1 * 100 for x in withdrawals]  #stores percentabe amounts in a list using list comprehension     #(lambda i: i/sum1 * 100 for i in withdrawals)

#     catagory_name_length = []
#     for category in categories:
#         catagory_name_length.append(len(category.category))
#     max_cat_name_length = max(catagory_name_length)
#     # print(percent)
#     # print(num_hold)
#     # print(withdrawals)
#     # print(max_cat_name_length)
  
#     string = "Percentage spent by category"
#     for x in range(100, -1, -10):# this keeps drawing 3 spaces until the 'o' is greater than the range from the 1st for-loop.
#         string += "\n" + str(x).rjust(3) + "|"
#         for perc in percent:
#             if perc > x:
#                 string += " o "
#             else:
#                 string += "   "
#         string += " "
#     string += "\n    ----------"
  
#     for z in range(max_cat_name_length):# z is a placeholder for us to be able to run the loop for len(budget.object)
#         # print(f'zzzz is{z}')
#         string += "\n    "
#         for x in range(len(categories)):
#             # print(f'xxxx is {x}')
#             if z < catagory_name_length[x]:
#                 string += " " + categories[x].category[z] + " "
#             else:
#                 string += "   "
#         string += " "
    
#     return string
    
# clothing = Category('clothing')
# food = Category('food')
# auto = Category('auto')
# food.deposit(1000, 'initial deposit')
# food.withdraw(10.15, 'groceries')
# food.withdraw(15.89, 'restaurand and more food')
# clothing.deposit(100, 'pants')
# clothing.withdraw(30)
# clothing.withdraw(20)
# food.transfer(50.00, clothing)
# auto.deposit(100)
# auto.withdraw(20)
# print(food.ledger)
# create_spend_chart([food, clothing])
# food.get_balance()
# print(clothing.ledger)
# food.check_funds(800)

