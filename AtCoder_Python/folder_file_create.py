import os
def save_file_at_new_dir(new_dir_path, new_filename, new_file_content, mode="w"):
    os.makedirs(new_dir_path, exist_ok=True)
    with open(os.path.join(new_dir_path, new_filename), mode) as f:
        f.write(new_file_content)
    print("create!")

def create(start, end, S):      # S:list
    for i in range(start, end + 1):
        for s in S:
            new_dir_path = "ABC0" + str(i)
            new_filename = "ABC_0" + str(i) + "_" + s + ".py"
            new_file_content = "ABC" + str(i) + s
            save_file_at_new_dir(new_dir_path, new_filename, new_file_content)
            

def main():
    start = 42
    end = 99
    S = ["A", "B", "C", "D"]
    create(start, end, S)

if __name__ == '__main__':
    main()