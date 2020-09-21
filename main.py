from plyer import notification
import requests
import bs4

def stat():
    Total_CoronaVirus_cases = data[0]
    Deaths = data[1]
    Recovered = data[2]
    
    #Return count of total covid cases, Deaths, Total Recovered cases in india
    return "Total cases : "+Total_CoronaVirus_cases+"\n" +"Total Deaths : "+Deaths +"\n"+"Total Recovered : "+Recovered



def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "icon.ico" ,
        timeout = 10
    )


if __name__ == "__main__":
    
    #make requests from web page
    result = requests.get('https://www.worldometers.info/coronavirus/country/india')

    #soup object
    soup = bs4.BeautifulSoup(result.text,'lxml')

    #find the div
    cases = soup.find_all('div',class_='maincounter-number')

    #data list
    data=[]
    for i in cases:
        span = i.find('span')
        data.append(span.string)

    notifyme("CoronaVirus Update",stat())




    

   

    

        

    
    
