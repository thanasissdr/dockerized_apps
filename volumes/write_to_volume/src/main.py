import os.path as osp

if __name__ == "__main__":

    volume = "/src/data"  # volume inside the container
    filepath = osp.join(volume, "text.txt")

    with open(filepath, "a") as f:
        f.write("new string\n")
