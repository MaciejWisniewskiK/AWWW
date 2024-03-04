from get_table import get_table
import shutil

def getTitleAndDesc():
    ret =  '# 10 highest rated european Valorant teams\n'
    ret += 'Scrapped from [vlr](https://www.vlr.gg/rankings).\n\n'
    return ret

#table = [(int) place, 'name', 'region', 'imgname']
def genOneElement(element):
    ret =  f'## {element[0]}. {element[1]} <img src="team_logos/{element[3]}" width="20" height="20">\n'
    ret += f' ### Region: {element[2]}\n'

    shutil.copy(f'content/{element[3]}', f'page_files/team_logos/{element[3]}')
    
    return ret

def genMarkdown(dest_file):
    table = get_table()
    markdown_list = getTitleAndDesc()

    for element in table:
        markdown_list += genOneElement(element)
    
    with open(dest_file, 'w') as file:
        file.write(markdown_list)


if __name__ == '__main__':
    #dest_file = input('Enter destination file path: ')
    dest_file = 'page_files/index.md'
    genMarkdown(dest_file)