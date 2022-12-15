def masterList():
    with open("archive.txt", "r") as archive, open("master_list.txt", "r+") as list:
        master = list.read()
        for line in archive:
            if line in master:
                print("line found")
            else:
                print("line not found" +repr(line))
                if "\n" not in line:
                    line = line + "\n"
                list.write(line)


    archive.close()
    list.close()

