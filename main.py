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

def main_run():
    arguments = [x.lower() for x in sys.argv[1::]]
    if len(arguments) == 0:
        letter = "f"
    else:
        letter = arguments[0]

    print("\nSTARTED...")
    
    if not os.path.exists(folder):
        os.makedirs(folder)
    inputName = inputFileNames[letter]
    try:
        with open("input/{}.in".format(inputName), "r") as inputFile:
            print("yes")
            file = inputFile.readlines()
            line1 = file[0]
            max_slices = int(line1.split(" ")[0])
            different_types_of_pizza = line1[1]
            slices_in_pizza = (file[1].split(" "))
            slices_in_pizza[-1] = slices_in_pizza[-1].strip()
            print("max_slices: {}, pizza_types: {}".format(max_slices, different_types_of_pizza))
            print("slices_in_pizza: {}".format(slices_in_pizza))

            total_slices = 0
            pizza_no_chosen = {}
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
            i = 0
            lastElem = list(pizza_no_chosen.keys())[-1]
            pizza_no_chosen2 = pizza_no_chosen
            for i in range(len(slices_in_pizza)-lastElem):
                pizza_no_chosen2.pop

            print("total_slices: {}".format(total_slices))
            print("pizzas_no_chosen: {}".format(pizza_no_chosen))

            
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