from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/?page_num={}'
teamgoallist = []
with open('teamgoallist.txt', 'w') as file:
    for i in range(1,26):
        urlpage = url.format(i)
        response = requests.get(urlpage)
        page = response.content
        soup = BeautifulSoup(page, 'lxml')
        tablerows = soup.find_all('tr', class_ ='team')
        for tabledata in tablerows:
            teamname = tabledata.find_next('td', class_='name').text.strip()
            teamgoal = tabledata.find_next('td', class_='gf').text.strip()
            teamgoallist.append(teamname + '-' + teamgoal)
            file.write(teamname + '-' + teamgoal + '\n')
df = pd.DataFrame({'Team Name':teamnames,'Team Goals':teamgoals})
df.to_csv('teamgoals.csv',index=True)
