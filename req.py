print("Calculo de resistencias equivalentes")

restype =input("Enter \"p\"  for parallel and \"s\" for serie ");
res_sizeStr= input("Enter, How many resistences?")
res_size=int(res_sizeStr)
if restype == 's':
    resistence=0;
    for i in range (0,res_size):
        res = input("Enter a resistence value: ")
        res = int(res)
        resistence=resistence+res;
    print("The resistence equivalen is")
    print(resistence)
else:
    resistence = 0;
    for i in range(0, res_size):
        res = input("Enter a resistence value: ")
        res = int(res)
        resistence = resistence + 1/res;
    resistence=1/resistence
    print("The resistence equivalen is")
    print(resistence)


