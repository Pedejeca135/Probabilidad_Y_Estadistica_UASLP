"""
function to permute
"""
def permute(list):
    if len(list) == 0:
        return []
    elif len(list) == 1:
        return [list]
    else:
        res=[]
        for i in range(len(list)):
            x= list[i] 
            """
            print(list[i])
            print(list[:i]) 
            print(list[i+1:]) 
            """          
            nextToPermute = list[:i] + list[i+1:]
            #print(xs)
            for p in permute(nextToPermute):
                res.append([x]+p)
    return res

"""
function main() for executing the program.
"""
def main():    
    print("use * to exit capture mode")
    data = []
    #while loop for data request
    while True:
        variableInput = input("next element: ")
        if(variableInput == '*'):
            break
        else:
            data.append(variableInput)

    #permutation occurs
    print ('permutation')
    cont = 1
    for p in permute(data):
        print(str(cont) + ".-" + str(p))
        cont += 1
    
main()