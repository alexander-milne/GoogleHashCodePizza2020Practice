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
    pizza_no_chosen = {}
    for i in range(start, len(slices_in_pizza)):                
        temp = total_slices + int(slices_in_pizza[i])
        if temp <= max_slices:
            total_slices = temp
            pizza_no_chosen[i]=slices_in_pizza[i]
            #print("slices_in_pizza[{}]: {}".format(i, slices_in_pizza[i]))
        #else:
            #print("skipped: {}".format(slices_in_pizza[i]))
    return total_slices, pizza_no_chosen

def main_run():
    arguments = [x.lower() for x in sys.argv[1::]]
    if len(arguments) == 0:
        letter = "b"
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
            #print("max_slices: {}, pizza_types: {}".format(max_slices, different_types_of_pizza))
            #print("slices_in_pizza: {}".format(slices_in_pizza))

            total_slices = 0
            pizza_no_chosen = {}
            #slices_in_pizza = reversed(slices_in_pizza)
            #i = 0
            #while i <= len(slices_in_pizza) - 1:
            start = 0
            output = {}
            while (start<len(slices_in_pizza)-1):
                total_slices, new_pizza_no_chosen = computeLowerSums(max_slices, start, total_slices, slices_in_pizza)
                pizza_no_chosen.update(new_pizza_no_chosen)
                #print("total_slices: {}".format(total_slices))
                #print("pizzas_no_chosen: {}".format(pizza_no_chosen))
                output[total_slices] = pizza_no_chosen
                
                lastKey = list(pizza_no_chosen)[-1]
                lastVal = pizza_no_chosen.pop(lastKey)
                total_slices = total_slices-int(lastVal)
                start = lastKey+1
            #pizza_no_chosen2 = pizza_no_chosen
            #lastKey = list(pizza_no_chosen)[-1]
            #lastVal = pizza_no_chosen2.pop(lastKey)
            #print("lastKey: {}, lastVal: {}".format(lastKey, lastVal))
            
            #total_slices2 = total_slices-int(lastVal)
            #print("total_slices2: {}".format(total_slices2))
            #i = 0
            
            #for i in range(len(slices_in_pizza)-lastKey+1, len(slices_in_pizza)):
            #    temp = total_slices2 + int(slices_in_pizza[i])
            #    if temp <= max_slices:
            #        total_slices2 = temp
            #        pizza_no_chosen2[i]=slices_in_pizza[i]
            #        print("slices_in_pizza[{}]: {}".format(i, slices_in_pizza[i]))
            #    else:
            #        print("skipped: {}".format(slices_in_pizza[i]))
            #    print("slices_in_pizza[{}]: {}".format(i, slices_in_pizza[i]))
           # print("total_slices2: {}".format(total_slices2))
           # print(pizza_no_chosen2)
            #print("total_slices: {}".format(total_slices))
            #print("pizzas_no_chosen: {}".format(pizza_no_chosen))

            
            #for line in inputFile:
           #     if (lineNumber == 0):
           #         line1 = line.split(" ")
           #         max_slices = line1[0]
           #         different_types_of_pizza = line1[1]
                    
            #    else:
            #        slices_in_pizza = line.split(" ")
            #    lineNumber += 1
           # print("max_slices: {}, pizza_types: {}".format(max_slices, different_types_of_pizza))
           # print("slices_in_pizza: {}".format(slices_in_pizza))

            #photos = []
            #lineNumber = 0
            #for line in file:
                #if (lineNumber != 0):
                    #photos.append(Photo(lineNumber-1, line))
                #lineNumber += 1
            
    except IOError:
        print("!!! {}.txt NOT FOUND IN INPUT FOLDER !!!".format(inputName))
        exit()

    save_file(pizza_no_chosen, inputName, total_slices)
    


if __name__ == "__main__":
    main_run()