# 5) A building has 100 floors. One of the floors is the highest floor an egg 
# can be dropped from without breaking.If an egg is dropped from above that floor, 
# it will break. If it is dropped from that floor or below, it will be completely 
# undamaged and you can drop the egg again.
# Given two eggs, find the highest floor an egg can be dropped from without breaking, 
# with as few drops as possible.


neededDict = {}
# number of drops you need to make

def needed(eggs, floors):

    if (eggs, floors) in neededDict:
        return neededDict[(eggs, floors)]

    if eggs == 1:
        return floors

    if eggs > 1:

        minimum = floors
        for f in range(floors):
            #print(f)
            resultIfEggBreaks = needed(eggs - 1, f)
            resultIfEggSurvives = needed(eggs, floors - (f + 1))
            result = max(resultIfEggBreaks, resultIfEggSurvives)
            if result < minimum:
                minimum = result

        # 1 drop at best level f plus however many you need to handle all floors that remain unknown
        neededDict[(eggs, floors)] = 1 + minimum
        return 1 + minimum


print(needed(2, 100))

# print(neededDict)

