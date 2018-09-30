import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    file = open(filename, "r")
    
    src = filename + "-src"
    comment = filename + "-cmt"

    src_file = open(src, "w")
    comment_file = open(comment, "w")

    split_file = filename.split(".") 
   
    cmt_list = []
    src_list = []

    if split_file[-1] == "py":
        for line in file:
            if "#" in line:
                cmt_list.append(line)
            elif len(line) > 0:
                src_list.append(line)

    cmt_list = (l.rstrip() for l in cmt_list)
    cmt_list = list(l for l in cmt_list if l)
    src_list = (l.rstrip() for l in src_list)
    src_list = list(l for l in src_list if l)


    for x in cmt_list:
        comment_file.write("%s\n"%x)

    for x in src_list:
        src_file.write("%s\n"%x)

    src_file.close()
    comment_file.close()
    file.close()
