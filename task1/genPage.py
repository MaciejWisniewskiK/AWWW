from getTable import get_table
from genTeamPage import genTeamPage

import shutil

def getFrontMatter():
    ret =  '---\n'
    ret += 'layout: home\n'
    ret += 'title: "10 highest rated european Valorant teams"\n'
    ret += '---\n\n'
    return ret

def getTitleAndDesc():
    #ret =  '# 10 highest rated european Valorant teams\n'
    ret = getFrontMatter()
    ret += 'Scrapped from [vlr](https://www.vlr.gg/rankings).\n\n'
    return ret

#table = [(int) place, 'name', 'region', 'imgname']
def genOneElement(element):
    ret =  f'## {element[0]}. {element[1]} <img src="team_logos/{element[3]}" width="20" height="20">\n'
    ret += f' Region: {element[2]}  \n'
    ret += f' [More info on {element[1]}](team_pages/team_page{element[0]}.md)\n\n'

    shutil.copy(f'content/{element[3]}', f'page_files/team_logos/{element[3]}')
    
    return ret

def genMarkdown(dest_file, regen_subpages):
    table = get_table()
    markdown_list = getTitleAndDesc()

    for element in table:
        print(f'Working on {element[1]}')
        markdown_list += genOneElement(element)
        if regen_subpages:
            genTeamPage(element[0], element[1])
    
    with open(dest_file, 'w') as file:
        file.write(markdown_list)


if __name__ == '__main__':
    regen_subpages = input('Regenerate subpages? (y/n): ').lower() == 'y'
    dest_file = 'page_files/index.md'
    genMarkdown(dest_file, regen_subpages)