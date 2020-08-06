score=0
time=0

while time<3 and score<2:
    import random
    computers=str(random.randint(1,3))
    users=str(input("1 is ✊, 2 is ✌, 3 is ✋, I want is: "))
    transfer={
        "1":"✊",
        "2":"✌",
        "3":"✋"
    }
    
    for user in users:
        user_str_output=transfer.get(user, user)
    comp_str_output=""
    for computer in computers:
        computer_str_output=transfer.get(computer, computer)

    print("> Me is %s, Raymond is %s" %(user_str_output, computer_str_output))

    if (user_str_output=="✊" and computer_str_output=="✌")or (user_str_output=="✌" and computer_str_output=="✋") or (user_str_output=="✋" and computer_str_output=="✊"):
        print(">>> I Win😁😁😁😁😁")
        score+=1
        time+=1
    elif user_str_output==computer_str_output:
        print(">> draw draw, Come on Again")
    else: 
        print(">>> Raymond Win😭😭😭😭😭😭")
        time+=1
    print(">>>> my score is %s won/2 won" %score)
if score>=2:
    print("Next Stage")
else:
    print("Sorry,🐷🐷🐷🐷🐷🐷Failed this Stage")