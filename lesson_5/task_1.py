sent = input("enter a two-word sentence: ").split(" ")
change_sent = " ! ".join(sent[-1::-1])
print(f'!{change_sent}!')
