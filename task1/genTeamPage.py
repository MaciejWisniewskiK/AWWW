from googlesearch import search

def genTeamPage(team_number, team_name):
    md = f'Google search results on "{team_name} valorant team":\n\n'
    results = search(f'{team_number}. {team_name} valorant team', stop=5)
    for url in results:
        md += f'[{url}]({url})\n'
    
    file_path = f'page_files/team_pages/team_page{team_number}.md'
    with open(file_path, 'w') as file:
        file.write(md)
    #return md