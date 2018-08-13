from urllib.request import urlopen
from bs4 import BeautifulSoup

def getVideoLinksAndNames(pageURL):
    links = []
    htmlPage = urlopen(pageURL)
    bsPage = BeautifulSoup(htmlPage, 'html.parser')
    
    links =  bsPage.tbody.tr.find_all('a');

    impLinks = []
    for i in range(0, len(links), 3):
        impLinks.append(links[i])

    for i in range(len(impLinks)):
        impLinks[i]['href'] = "https://nptel.ac.in" + impLinks[i]['href']
        #print(impLinks[i]['href'])

    for link in impLinks:
        #print(link['href'])
        count = 0
        index = 0
        for l in range(len(link['href'])):
            if(link['href'][l] == '='):
                count += 1
            if(count == 3):
                index = l
                break
    names = []
    for i in range(len(impLinks)):
        names.append(impLinks[i]['href'][index::])

 
    return(impLinks, names)
    
def downloadVideos(videoLinks, names):
    for i in range(len(videoLinks)):
        web_file = urlopen(videoLinks[i]['href'].replace(' ', '%20'))
        print(str(i+1)+". Conneted...")
        local_file = open(str(i+1)+'. ' + names[i]+'.mp4', 'wb')
        print("Downloading "+names[i])
        local_file.write(web_file.read())
        print(names[i]+" downloaded")
        web_file.close()
        local_file.close()
    print("All File Downloaded !")


if __name__ == '__main__':
    pageURL = 'https://nptel.ac.in/courses/nptel_download.php?subjectid=106106183'
    videoLinks, names = getVideoLinksAndNames(pageURL)
    downloadVideos(videoLinks, names)
    #print(videoLinks[0]['href'])
