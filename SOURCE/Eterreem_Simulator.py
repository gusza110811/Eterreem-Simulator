from os import mkdir
import time

Eterreem = 0
GPU_name = "Grandpa's video card"
GPU_quality = 1


def new_game(save_name):
    global Eterreem
    global GPU_name
    global GPU_quality

    Eterreem = 0
    GPU_name = "Grandpa's video card"
    GPU_quality = 1
    save_game(save_name)
    Game()


def load_save(save_name):
    with open(f"saves/{save_name}/Eterreem.txt", "r") as Eterreem_r:
        global Eterreem
        Eterreem = int(Eterreem_r.read())
    with open(f"saves/{save_name}/GPU_name.txt", "r") as GPU_name_r:
        global GPU_name
        GPU_name = str(GPU_name_r.read())
    with open(f"saves/{save_name}/GPU_quality.txt", "r") as GPU_quality_r:
        global GPU_quality
        GPU_quality = int(GPU_quality_r.read())
    Game()


def save_game(save_name):
    try:
        mkdir(f"saves/{save_name}")
    except FileExistsError:
        pass

    with open(f"saves/{save_name}/Eterreem.txt", "w") as Eterreem_w:
        Eterreem_w.write(str(Eterreem))
    with open(f"saves/{save_name}/GPU_name.txt", "w") as GPU_name_w:
        GPU_name_w.write(str(GPU_name))
    with open(f"saves/{save_name}/GPU_quality.txt", "w") as GPU_quality_w:
        GPU_quality_w.write(str(GPU_quality))


def mine(amount):
    global Eterreem
    global GPU_quality
    save_game(name)
    for i in range(int(amount/GPU_quality)):
        Eterreem = Eterreem + GPU_quality
        print(f"you have {Eterreem}")
        save_game(name)
        time.sleep(1)


def buy_GPU(name, quality, price):
    global GPU_name
    global GPU_quality
    global Eterreem
    print(f"{name} costs {price} Eterreem")
    sure = input("are you sure? (y/n): ")
    if sure.lower() == "y":
        if Eterreem >= price:
            Eterreem -= price
            GPU_name = name
            GPU_quality = quality
            print(f"you have {Eterreem}")
            print(f"you have bought {GPU_name}")
        else:
            print("you dont have enough Eterreem")
            return
    else:
        return


def gpu_store():
    print("GPU store")
    print("warning: you can downgrade your GPU but it cant be undone")
    print("1. Intel 8bit GPU")
    print("2. Nvidia 8bit GPU")
    print("3. AMD 8bit GPU")
    print("4. Intel 16bit GPU")
    print("5. Nvidia 16bit GPU")
    print("6. AMD 16bit GPU")
    print("7. Intel 32bit GPU")
    print("8. Nvidia 64bit GPU")
    print("9. AMD 32bit GPU")
    print("10. Intel i1")
    print("11. Nvidia geforce gtx 110")
    print("12. AMD radeon rx 580")
    print("13. Intel i2")
    print("14. Nvidia geforce gtx 120")
    print("15. AMD radeon rx 590")
    print("16. Intel i5")
    print("17. Nvidia geforce gtx 130")
    print("18. AMD radeon rx 600")
    print("19. Intel i7")
    print("20. Nvidia geforce gtx 150")
    print("21. AMD radeon rx 790")
    print("22. Intel Titan X")
    print("23. Nvidia geforce gtx 1650")
    print("24. AMD radeon rx Vega")
    print("25. Intel Titan X TI")
    print("26. Nvidia geforce gtx 1800")
    print("27. Nvidia geforce gtx 1950")
    print("28. Nvidia geforce gtx 2070")
    print("29. Nvidia geforce gtx 2080")
    print("30. Intel Titan Y")
    print("31. Nvidia geforce gtx 2100")
    print("32. Nvidia geforce gtx 2150")
    print("33. Intel Titan Z")
    print("34. Raspberry ztx 102")
    print("35. Raspberry ztx 103")
    print("36. Raspberry ztx 110")
    print("37. Raspberry ztx 120")
    print("38. Raspberry ztx 130")
    print("39. Raspberry ztx 140")
    print("40. Intel Hyper 1")

    choice = input("what GPU do you want to buy? ")

    if choice == "0":
        return

    if choice == "1":
        buy_GPU("Intel 8bit GPU", 2, 120)
    elif choice == "2":
        buy_GPU("Nvidia 8bit GPU", 4, 480)
    elif choice == "3":
        buy_GPU("AMD 8bit GPU", 16, 1920)
    elif choice == "4":
        buy_GPU("Intel 16bit GPU", 64, 7680)
    elif choice == "5":
        buy_GPU("Nvidia 16bit GPU", 128, 15360)
    elif choice == "6":
        buy_GPU("AMD 16bit GPU", 256, 30720)
    elif choice == "7":
        buy_GPU("Intel 32bit GPU", 1024, 92160)
    elif choice == "8":
        buy_GPU("Nvidia 64bit GPU", 2048, 230400)
    elif choice == "9":
        buy_GPU("AMD 32bit GPU", 4096, 460800)
    elif choice == "10":
        buy_GPU("Intel i1", 8192, 1228800)
    elif choice == "11":
        buy_GPU("Nvidia geforce gtx 110", 16384, 2457600)
    elif choice == "12":
        buy_GPU("AMD radeon rx 580", 32768, 4915200)
    elif choice == "13":
        buy_GPU("Intel i2", 65536, 9830400)
    elif choice == "14":
        buy_GPU("Nvidia geforce gtx 120", 131072, 19660800)
    elif choice == "15":
        buy_GPU("Intel i5", 262144, 39321600)
    elif choice == "16":
        buy_GPU("Nvidia geforce gtx 130", 524288, 7864320)
    elif choice == "17":
        buy_GPU("AMD radeon rx 600", 1048576, 15728640)
    elif choice == "18":
        buy_GPU("Intel i7", 2097152, 31457280)
    elif choice == "19":
        buy_GPU("Nvidia geforce gtx 150", 4194304, 6291456)
    elif choice == "20":
        buy_GPU("AMD radeon rx 790", 8388608, 12582912)
    elif choice == "21":
        buy_GPU("Intel Titan X", 16777216, 25165824)
    elif choice == "22":
        buy_GPU("Nvidia geforce gtx 1650", 33554432, 50331648)
    elif choice == "23":
        buy_GPU("AMD radeon rx Vega", 67108864, 1006632960)
    elif choice == "24":
        buy_GPU("Intel Titan X TI", 134217728, 2013265920)
    elif choice == "25":
        buy_GPU("Nvidia geforce gtx 1800", 268435456, 4026531840)
    elif choice == "26":
        buy_GPU("Nvidia geforce gtx 1950", 536870912, 8053063680)
    elif choice == "27":
        buy_GPU("Nvidia geforce gtx 2070", 1073741824, 1610612736)
    elif choice == "28":
        buy_GPU("Nvidia geforce gtx 2080", 2147483648, 3221225472)
    elif choice == "29":
        buy_GPU("Nvidia geforce gtx 2100", 4294967296, 6442450944)
    elif choice == "30":
        buy_GPU("Intel Titan Y", 8589934592, 12884901888)
    elif choice == "31":
        buy_GPU("Nvidia geforce gtx 2100", 17179869184, 34359738368)
    elif choice == "32":
        buy_GPU("Nvidia geforce gtx 2150", 34359738368, 68719476736)
    elif choice == "33":
        buy_GPU("Intel Titan Z", 7378698752, 137438953472)
    elif choice == "34":
        buy_GPU("Raspberry ztx 102", 1407374883584, 28147497671088)
    elif choice == "35":
        buy_GPU("Raspberry ztx 103", 28147497671088, 562949953421312)
    elif choice == "36":
        buy_GPU("Raspberry ztx 110", 562949953421312, 1125899906842624)
    elif choice == "37":
        buy_GPU("Raspberry ztx 120", 1125899906842624, 2251799813685248)
    elif choice == "38":
        buy_GPU("Raspberry ztx 130", 2251799813685248, 4503599627370496)
    elif choice == "39":
        buy_GPU("Raspberry ztx 140", 4503599627370496, 9007199254740992)
    elif choice == "40":
        buy_GPU("Intel Hyper 1", 18014398509481984, 36028797018963968)
    else:
        print("invalid choice")
        gpu_store()


def profile():
    print("profile:")
    print(f"Eterreem: {Eterreem}")
    print(f"GPU name: {GPU_name}")
    print(f"GPU quality: {GPU_quality}")
    pause = input("press enter to continue")
    return


def Game():

    if __name__ != "__main__": return

    while 1:
        print("select action")
        print("1. buy GPU")
        print("2. start mining")
        print("3. profile")
        print("4. save")
        print("5. return to menu")
        choice = input(">>>")
        if choice == "1":
            gpu_store()
        elif choice == "2":
            mine(int(input("amount of Eterreem to mine: ")))
        elif choice == "3":
            profile()
        elif choice == "4":
            save_game(name)
        elif choice == "5":
            Menu()


def Menu():
    if __name__ != "__main__": return

    print("select action")
    print("1. new game")
    print("2. load game")
    print("3. exit")
    choice = input(">>>")
    global name
    if choice == "1":
        name = input("enter save name: ")
        new_game(name)
    elif choice == "2":
        name = input("enter save name: ")
        load_save(name)
    elif choice == "3":
        exit()

if __name__ == "__main__":
    Menu()