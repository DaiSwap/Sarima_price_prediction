import random
list = [1,4,6]
list.append(random.randrange(len(list)))
print("the original list:"+str(list))
list.pop(random.randrange(len(list)))
print("the list after removing random number:"+str(list))
