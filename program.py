import dir
import images

menu = True
while menu != 0:
    print('''
    0 - Exit. 
    1 - Create Dir.
    2 - Del Dir.
    3 - Load Images.
    4 - Create DB Image Hash.
    5 - Compare Images.
    6 - Find Similar.
    ''')
    menu = int(input("Choice an item:"))

    if menu == 0:
        menu = False
    elif menu == 1:
        dir.create_dir()
    elif menu == 2:
        dir.del_dir()
    elif menu == 3:
        images.load_images()
    elif menu == 4:
        images.create_db_image_hash()
    elif menu == 5:
        print("TODO")
    elif menu == 6:
        images.find_similar()





