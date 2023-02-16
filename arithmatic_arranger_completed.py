# import error_finder
import copy
def arithmetic_arranger(math_probs, show_answer=False):
    # error_finder.list_length(math_probs)
    arragned_problems =''
    if len(math_probs) > 5:
        arragned_problems = 'Error: Too many problems.'
        return print(arragned_problems)

    first_list = list(map(lambda fr: fr.split()[0], math_probs))
    operand_list = list(map(lambda op: op.split()[1], math_probs))
    second_list = list(map(lambda sc: sc.split()[2], math_probs))
    print(operand_list)
    isdigi = list()
    for x in math_probs:
        dig = x.split()
        isdigi.extend([dig[0], dig[2]])
    if not all(map(lambda v: v.isdigit(), isdigi)):
        arragned_problems = 'Error: Numbers must only contain digits.'
        return print(arragned_problems)
    if not all(map(lambda dig_count: len(dig_count) <= 4, isdigi)):
        arragned_problems = 'Error: Numbers cannot be more than four digits.'
        return print(arragned_problems)
    #error_finder.add_sub_only(operand_list)
    top = []
    mid= []
    bot = []
    solu = []
    for fir, oper, sec in zip(first_list, operand_list, second_list):
        distance = max((len(fir), len(sec))) + 2
        top.append(f"{fir: >{distance}}")
        mid.append(f"{oper:<1}{sec: >{distance - 1}}")
        bot.append(f"{'':-<{distance}}")
        if oper == '+':
            solution = int(fir) + int(sec)
            solu.append(f"{solution: >{distance}}")
        elif oper == '-':
            solution = int(fir) - int(sec)
            solu.append(f"{solution: >{distance}}")
        else:
            arragned_problems = 'Error: Operator must be \'+\' or \'-\'.'
            return print(arragned_problems)
    if not show_answer:
        arragned_problems = '    '.join(top) + '\n' + '    '.join(mid) + '\n' +'    '.join(bot)
        return print(arragned_problems)
    if show_answer: 
        arragned_problems ='    '.join(top) + '\n' + '    '.join(mid) + '\n' +'    '.join(bot) + '\n' + '    '.join(solu)
        return print(arragned_problems)
arithmetic_arranger(["1 + 12", '129 + 232'], True)
