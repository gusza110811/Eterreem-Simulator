from os import mkdir
import time
import json

GPU_list = []

with open('resource/GPU.json', 'r') as file:
    GPU_list = json.load(file)

Eterreem = 0
GPU_name = GPU_list[0]['name']
GPU_quality = 1

name = ""


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
    if quality > GPU_quality:
        sure = input("are you sure? (y/n): ")
    else:
        sure = input("you are buying a GPU that worse than your current one, \n please confirm that you want it (y/n)")
    if sure.lower() == "y":
        if Eterreem >= price:
            Eterreem -= price
            GPU_name = name
            GPU_quality = quality
            print(f"you have {Eterreem}")
            print(f"you have bought {GPU_name} with the quality of {quality}")
        else:
            print("you dont have enough Eterreem")
            return
    else:
        return


def gpu_store():
    while 1:
        print("GPU store")
        print(f"your current GPU: {GPU_name} \n Its quality: {GPU_quality}")
        print("warning: you can downgrade your GPU but it cantnot be undone")
        for i in range (1,len(GPU_list)):
            print(f"{i}. {GPU_list[i]['name']} price: {GPU_list[i]['price']} quality: {GPU_list[i]['quality']}")

        choice = int(input("what GPU do you want to buy? enter 0 to exit: "))

        if choice == 0:
            break

        buy_GPU(GPU_list[choice]['name'],GPU_list[choice]['quality'],GPU_list[choice]['price'])
        break


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
    global name
    if __name__ != "__main__": return
    while True:
        print("select action")
        print("1. new game")
        print("2. load game")
        print("3. exit")
        choice = input(">>>")
        if choice == "1":
            name = input("enter save name: ")
            new_game(name)
        elif choice == "2":
            name = input("enter save name: ")
            try:
                with open(f"saves/{name}/Eterreem.txt", "r"):
                    pass  # check if file exists
                load_save(name)
            except FileNotFoundError:
                print("save not found")
        elif choice == "3":
            exit()


if __name__ == "__main__":
    Menu()
