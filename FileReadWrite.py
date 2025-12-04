# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()


# f = open("demo.txt", "w")
# f.write("This is Murari Pathak.\n\nIt's great to see you bro!")
# f.close()


# f = open("demo.txt", "a")
# f.write("\n\nLet's have some adventure bro!")
# f.close()

# f = open("demo.txt", "r")
# data = f.read()
# new_data = data.replace("Murari", "Kumar")
# print(new_data)
# f.close()

# def check_word_exists():
#     with open("demo.txt", "r") as f:
#         word = "Murari"
#         data = f.read()
#         if(data.find(word)):
#             print(f"Found {word}")
#         else:
#             print(f"Not found {word}")
# check_word_exists()


def check_which_line():
    word = "great"
    with open("demo.txt", "r") as f:
        data = True
        line_no = 1
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no = line_no + 1
    return -1

check_which_line()