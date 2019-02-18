from operator import itemgetter
import sys

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


filename = 'file.txt'
if len(sys.argv) == 1:
    filename = sys.argv[0]
else:
    raise ValueError("-E- You have to give file name as a command line argument.")

file = open(filename)
result = countWords(file)

result_file_name = file.name + '_result'
print(result_file_name)
print(result)