j = input("Você está em jejum s/n? ")
t = input("Trigiceres? ")
t = int(t) # converter pra int
if j == 's' :
    if t > 150:
        print("Está alto")
    else:
        print("está normal!")

else:
    if t > 175:
        print("Está alto")
    else:
        print("está normal!")   