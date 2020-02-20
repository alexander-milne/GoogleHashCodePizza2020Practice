#import PizzaProblem
import random
import os
import sys

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

inputFileNames = {
    "a": "a_example",
    "b": "b_small",
    "c": "c_medium",
    "d": "d_quite_big",
    "e": "e_also_big",
    "f": "f_alex_test"
}

folder = ("/out")

alreadyComputedLowerSums= {}
#alreadyComputedMoreLowerSums= {}

def save_file(pizza_no_chosen, inputName, total_slices):
    outputFileName = "{}/{}/{}_out_{}.out".format(__location__,folder, inputName, "score_" + str(total_slices))
    with open(outputFileName, "w") as out:
        out.write('{}\n'.format(len(pizza_no_chosen)))
        for value in pizza_no_chosen.keys():
            out.write('{} '.format(value))
        #for slide in slideshow:
         #   out.write(str(slide) + "\n")
    #with open(outputFileName, "w") as out:
    #    out.write(str(len(slideshow)) + "\n")
    #    for slide in slideshow:
   #         out.write(str(slide) + "\n")

def computeLowerSums(max_slices, start, total_slices, slices_in_pizza):
    #print("start in computeLowerSums: {}".format(start))    
    if start in alreadyComputedLowerSums.keys():
        total_slices, pizza_no_chosen = alreadyComputedLowerSums[start]
        return total_slices, pizza_no_chosen
    
    pizza_no_chosen = {}
    for i in range(start, len(slices_in_pizza)):
        
        if i in alreadyComputedLowerSums.keys():
            total_slices_saved, pizza_no_chosen_saved = alreadyComputedLowerSums[start]
            pizza_no_chosen.append(pizza_no_chosen_saved)
            return total_slices + total_slices_saved, pizza_no_chosen
            break
        else:
            temp = total_slices + int(slices_in_pizza[i])
            if temp <= max_slices:
                total_slices = temp
                pizza_no_chosen[i]=slices_in_pizza[i]
                alreadyComputedLowerSums[i] = total_slices, pizza_no_chosen
            #print("slices_in_pizza[{}]: {}".format(i, slices_in_pizza[i]))
        #else:
            #print("skipped: {}".format(slices_in_pizza[i]))

    alreadyComputedLowerSums[start] = total_slices, pizza_no_chosen
    return total_slices, pizza_no_chosen

def moreComputeLowerSums(max_slices, start, slices_in_pizza):
    #print("start in moreComputeLowerSums: {}".format(start))
    total_slices = 0
    pizza_no_chosen = {}
    #slices_in_pizza = reversed(slices_in_pizza)
    #i = 0
    #while i <= len(slices_in_pizza) - 1:
    outputs = {}
    while (start<len(slices_in_pizza)-1):
        total_slices, new_pizza_no_chosen = computeLowerSums(max_slices, start, total_slices, slices_in_pizza)
        pizza_no_chosen.update(new_pizza_no_chosen)
        #print("total_slices: {}".format(total_slices))
        #print("pizzas_no_chosen: {}".format(pizza_no_chosen))
        outputs[total_slices] = pizza_no_chosen
                
        lastKey = list(pizza_no_chosen)[-1]
        lastVal = pizza_no_chosen.pop(lastKey)
        total_slices = total_slices-int(lastVal)
        start = lastKey+1
        print("keys: {}".format(list(outputs.keys())))
        max_score = max(list(outputs.keys()))
    return max_score, outputs[max_score]

def moreMoreComputeLowerSums(max_slices, slices_in_pizza):
    pizza_no_chosen = {}
    stop = round(len(slices_in_pizza)*0.1)
    outputs = {}
    for start in range(0, stop):
        print("start in moreMoreComputeLowerSums: {}".format(start))
        max_score, pizza_no_chosen = moreComputeLowerSums(max_slices, start, slices_in_pizza)
        outputs[max_score] = pizza_no_chosen
    
    print("moreMoreComputeLowerSums -> outputs dict, {}".format(outputs.keys()))
    max_score = max(list(outputs.keys()))
    return max_score, outputs[max_score]

def computeHigherSums(max_slices, slices_in_pizza):
    pizza_no_chosen = {}
    total_slices = 0
    #slices_in_pizza = reversed(slices_in_pizza)
    i = len(slices_in_pizza) - 1
    while i >= 0:
        temp = total_slices + int(slices_in_pizza[i])
        if temp <= max_slices:
            total_slices = temp
            pizza_no_chosen[i]=slices_in_pizza[i]
            i-=1
        else:
            i-=1
    return total_slices, pizza_no_chosen

def main_run():
    arguments = [x.lower() for x in sys.argv[1::]]
    if len(arguments) == 0:
        letter = "e"
    else:
        letter = arguments[0]

    print("\nSTARTED...")
    
    if not os.path.exists(folder):
        os.makedirs(folder)
    inputName = inputFileNames[letter]
    try:
        with open("input/{}.in".format(inputName), "r") as inputFile:
            #print("yes")
            file = inputFile.readlines()
            line1 = file[0]
            max_slices = int(line1.split(" ")[0])
            different_types_of_pizza = line1[1]
            slices_in_pizza = (file[1].split(" "))
            slices_in_pizza[-1] = slices_in_pizza[-1].strip()
            #print("slices_in_pizza: \n{}".format(slices_in_pizza))
            slices_in_pizza.reverse()
            #print("slices_in_pizza: \n{}".format(slices_in_pizza))

            max_score, pizza_no_chosen = moreMoreComputeLowerSums(max_slices, slices_in_pizza)
            #max_score, pizza_no_chosen = moreComputeLowerSums(max_slices, 0, slices_in_pizza)
            #max_score, pizza_no_chosen = computeHigherSums(max_slices, slices_in_pizza)
            print("score: {}".format(max_score))

    except IOError:
        print("!!! {}.in NOT FOUND IN INPUT FOLDER !!!".format(inputName))
        exit()

    output_keys = []
    print("list(pizza_no_chosen.keys()): {}".format(list(pizza_no_chosen.keys())))
    output_keys_reveesed = list(pizza_no_chosen.keys())
    for i in range(0, len(output_keys_reveesed)):
        new = len(slices_in_pizza)-output_keys_reveesed[i]-1
        #print("new: {}".format(new))
        output_keys.append(new)

    output_keys.reverse()
    save_file(output_keys, inputName, max_score)

    save_file(pizza_no_chosen, inputName, max_score)
    
if __name__ == "__main__":
    main_run()