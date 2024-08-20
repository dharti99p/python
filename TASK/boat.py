# # Input values
# boat_capacity = int(input("Enter the boat capacity: "))
# men = int(input("Enter the number of men: "))
# women = int(input("Enter the number of women: "))
# children = int(input("Enter the number of children: "))

# # Initial variables
# total_people = 0
# remaining_capacity = boat_capacity

# if men > 0 :
#     if boat_capacity > 0:
#         # Step 1: Pair men and women with children
#         while men > 0 and children >= 4 and remaining_capacity >= 5:
#             total_people += 5  # 1 man + 4 children
#             remaining_capacity -= 5
#             men -= 1
#             children -= 4

#         while women > 0 and children >= 4 and remaining_capacity >= 5:
#             total_people += 5  # 1 woman + 4 children
#             remaining_capacity -= 5
#             women -= 1
#             children -= 4

#         # Adding remaining women if any children are left
#         if children > 0:
#             while women > 0 and children >= 4 and remaining_capacity >= 5:
#                 total_people += 5  # 1 woman + 4 children
#                 remaining_capacity -= 5
#                 women -= 1
#                 children -= 4

#         while men > 0 and children >= 4 and remaining_capacity >= 5:
#             total_people += 5  # 1 man + 4 children
#             remaining_capacity -= 5
#             men -= 1
#             children -= 4

#         while women > 0 and children >= 4 and remaining_capacity >= 5:
#             total_people += 5  # 1 woman + 4 children
#             remaining_capacity -= 5
#             women -= 1
#             children -= 4

#         # Adding the remaining 1 woman if capacity allows
#         if women > 0 and remaining_capacity > 0:
#             total_people += 1
#             remaining_capacity -= 1
#             women -= 1

#     else :
#         print("boat capacity 0 ")

# else:
#     print("man is 0 ")



# # Result
# print("Total people on the boat:", total_people)
# print("Remaining boat capacity:", remaining_capacity)





boat_capacity = 50
men = 2
women = 6
child = 20

total_people = 0
remainig_capacity = boat_capacity

if boat_capacity > 0:
    if men > 0:
        if men > 0 and child >=4 and remainig_capacity >= 5:
            total_people += 5
            remainig_capacity -= 5
            men -= 1
            child -= 4
            print(men, child, remainig_capacity, total_people)
    else :
        print("your men capacity minimum 1")
else :
    print('your boat capacity minimum 1')