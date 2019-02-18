from operator import itemgetter
import sys
import os

def countWords(file):
    result = {}
    # count words
    for line in file:
        for word in line.split():
            if word in result.keys():
                result[word] += 1
            else:
                result[word] = 1

    # sort the result
    list_result = []
    for item in result:
        list_result.append([item, result[item]])

    result = sorted(list_result, key=itemgetter(1), reverse=True)
    result = tuple(result)
    return result

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    raise ValueError("-E- You have to give file name as a command line argument.")

file = open(filename)
result_tuple = countWords(file)

result_file_name = os.path.basename(file.name)
result_file_name = os.path.splitext(result_file_name)[0] + '_result.txt'

result_file = open(result_file_name, 'w')
for item in result_tuple:
    result_file.write("{0} = {1}\n".format(item[0], item[1]))