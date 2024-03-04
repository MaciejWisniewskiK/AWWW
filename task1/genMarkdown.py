from get_table import get_table

#table = [(int) place, 'name', 'region', 'imgname']
def genMarkdown(dest_file):
    table = get_table()
    markdown_list = ""
    for element in table:
        markdown_list += f"{element[0]} {element[1]}\n"
    
    with open(dest_file, 'w') as file:
        file.write(markdown_list)


if __name__ == "__main__":
    dest_file = input("Enter destination file path: ")
    genMarkdown(dest_file)