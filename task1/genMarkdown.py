from get_table import get_table

def getTitleAndDesc():
    ret =  '# 10 highest rated european Valorant teams\n'
    ret += 'Scrapped from [vlr](https://www.vlr.gg/rankings) \n'
    return ret

#table = [(int) place, 'name', 'region', 'imgname']
def genOneElement(element):
    ret =  f'## {element[0]}. {element[1]} <img src="content/{element[3]}" width="20" height="20">\n'
    ret += f' ### Region: {element[2]}\n'
    return ret

def genMarkdown(dest_file):
    table = get_table()
    markdown_list = getTitleAndDesc()

    for element in table:
        markdown_list += genOneElement(element)
    
    with open(dest_file, 'w') as file:
        file.write(markdown_list)


if __name__ == '__main__':
    dest_file = input('Enter destination file path: ')
    genMarkdown(dest_file)