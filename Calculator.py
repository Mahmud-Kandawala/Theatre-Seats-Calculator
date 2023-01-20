Hall = 300
Mezzanine = 100

while Hall or Mezzanine !=0: 
    info = int(input("\nEnter 1 for Hall or enter 2 for Mezzanine ==>" ))
    Adults = int(input("Number of adults? ==> "))
    Children = int(input("Number of children? ==> "))

    if info == 1:
       if Hall < (Adults + Children):
            print("Refused, not enough seats in the required area, check the available area, and then enter again")
            continue
       else:
            adultSum = Adults * 10
            childrenSum = Children * 7

            total = adultSum + childrenSum
            totalPeople = Adults + Children
            Hall = Hall - totalPeople

            print("\nGreat, you got", Adults, "adult tickets for $", adultSum, "and", Children, "child tickets for $",childrenSum, "so your total is $",total)
            print("Remaning Seats: Hall", Hall, "Mezzanine", Mezzanine)


    elif info == 2:
        if Mezzanine < (Adults + Children):
            print("Refused, not enough seats in the required area, check the available area, and then enter again")
            continue
        else:

            adultsum = Adults * 8
            childrenSum = Children * 5

            total = adultsum + childrenSum
            totalPeople = Adults + Children
            Mezzanine = Mezzanine - totalPeople

            print("\nGreat, you got", Adults, "adult tickets for $", adultsum, "and", Children, "child tickets for $", childrenSum, "so your total is $", total)
            print("Remaning Seats: Hall", Hall, "Mezzanine", Mezzanine)
                
    else:
        wrong = input("\nWrong selection made, enter any letter or number to be prompted again ==> ")
        

print("\n0 Halls and 0 Mezzanine seats available. Thank you for your bussiness.")