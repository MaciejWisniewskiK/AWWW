from googlesearch import search

def genCommonPrefix(team_name):
    md = '---\n'
    md += f'layout: "team_page"\n'
    md += f'title: {team_name}\n'
    md += '---\n\n'
    md += f'Google search results on "{team_name} valorant team":\n\n'
    return md

def genTeamPage(team_number, team_name):
    md = genCommonPrefix(team_name)
    results = search(f'{team_name} valorant team', stop=5)
    for url in results:
        md += f'{team_number}. [{url}]({url})\n'
    
    file_path = f'page_files/team_pages/team_page{team_number}.md'
    with open(file_path, 'w') as file:
        file.write(md)
    #return md