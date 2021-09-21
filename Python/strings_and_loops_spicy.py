print("type in your text, then press enter:")
for x in input(): # yeah this works for some reason
    if x == ' ': print('-') # If it's a space, it turns into a dash
    else: print(x) # prints thhe characters one by one
