# total_amount = float(input("what is the total bill amount "))
# print(total_amount)
# level_of_service = (input("Level of service? "))
# if level_of_service == "good":
#     good = float(total_amount) * 0.20
#     print(f"{tip_amount}")
#     total_amount = float(tip_amount) + total_amount
#     print(total_amount)

# if level_of_service == "fair":
#     fair = float(total_amount) * 0.15
#     print(f"{tip_amount}")
#     total_amount = float(tip_amount) + total_amount
#     print(total_amount)

# if level_of_service == "bad":
#     bad = float(total_amount) * 0.10
#     print(f"{tip_amount}")
#     total_amount = float(tip_amount) + total_amount         
#     print(total_amount)

pre_tip_amount = float(input("how much did it cost? "))
level_of_service = input("how is the level of service? ")

if level_of_service == "good":
    tip_amount = (pre_tip_amount) * 0.2
    print(tip_amount)
    total_amount = tip_amount + pre_tip_amount
    print(total_amount)

if level_of_service == "fair":
    tip_amount = (pre_tip_amount) * 0.15
    print(tip_amount)
    total_amount = tip_amount + pre_tip_amount
    print(total_amount)

if level_of_service == "bad":
    tip_amount = (pre_tip_amount) * 0.10
    print(tip_amount)
    total_amount = tip_amount + pre_tip_amount
    print(total_amount)    
    