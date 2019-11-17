import os
def save_file_at_new_dir(new_dir_path, new_filename, new_file_content, mode="w"):
    os.makedirs(new_dir_path, exist_ok=True)
    with open(os.path.join(new_dir_path, new_filename), mode) as f:
        f.write(new_file_content)
    print("create!")

def create(start, end, S):      # S:list
    for i in range(start, end + 1):
        for s in S:
            new_dir_path = "ARC" + str(i).zfill(3)
            new_filename = "ARC_" + str(i).zfill(3) + "_" + s + ".cpp"
            new_file_content = "// ARC" + str(i).zfill(3) + s
            save_file_at_new_dir(new_dir_path, new_filename, new_file_content)
            

def main():
    start = 1
    end = 103
    S = ["A", "B", "C", "D"]
    create(start, end, S)

if __name__ == '__main__':
    main()