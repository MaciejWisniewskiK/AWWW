# Code generated using chatGPT
from bs4 import BeautifulSoup

def extract_table_data(html_content, table_class):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table (adjust the tag and class based on your HTML structure)
    table = soup.find('table', class_=table_class)

    if table:
        # Extract data from the table
        table_data = []
        rows = table.find_all('tr')
        
        for row in rows:
            row_data = []
            cells = row.find_all(['td', 'th'])
            
            for cell in cells:
                
                images = cell.find_all('img')
                image_srcs = [img['src'] for img in images]

                divs = cell.find_all('div')
                div_texts = [div.get_text(strip=True) for div in divs]

                row_data.append(cell.get_text(strip=True))
                if len(image_srcs) > 0:
                    row_data.append(image_srcs[0])
                if len(div_texts) > 0:
                    row_data.append(div_texts)
            
            table_data.append(row_data)

        return table_data
    else:
        print("Table not found in the HTML")


# ['1', 'FNATICEurope', '//owcdn.net/img/62a40cc2b5e29.png', ['FNATICEurope', 'Europe'], '2000']
# [place, nameregion    ,               imgsrc              ,[  nameregion  ,   region], rating ]
# target: [(int) place, 'name', 'region', 'imgname']
def format_table(raw_table):
    formated_table = []
    
    for raw_row in raw_table:
        formated_row = [int(raw_row[0]), raw_row[1][:-len(raw_row[3][1])], raw_row[3][1], raw_row[2][len('//owcdn.net/img/'):]]
        formated_table.append(formated_row)

    return formated_table 




# ------------------ MAIN --------------------
        
# Read HTML content from file
table_class = 'wf-faux-table mod-teams mod-world'
file_path = 'content/index.html'
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()    

raw_table = extract_table_data(html_content, table_class)

# Print the extracted data
#for row in raw_table:
#    print(row)


final_table = format_table(raw_table)

#print('After format:')
for row in final_table:
    print(row)



    

