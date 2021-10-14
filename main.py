 from bs4 import BeautifulSoup
import requests
import lxml # Used in BS4 on line 13
import collections
from collections import Counter #GeeksforGeeks
import split
import os


  # Stack overlow
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # if machine doesn't use windows
        command = 'cls'
    os.system(command)
# 
clearConsole()

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
} 
# from example code

search_history = []
print("Welcome to Reddit Scraper!")
print("Type the subreddit you want to scrap. Please spell it correctly or the scrapper might not be able to pull up anything. No spaces!")
print()
print("Type 'Commands' for commands")
print()
print("Type 'Exit' to end reddit scrapper.")
print()
print("Type 'Popular' to see top posts on Reddit and see popular keywords")
print()
print("You can also enter your subreddit and put a /new or /top to sort through posts")
print("Example: typing 'aww/new' gets you all the new posts for the aww subreddit")
print("Acceptable sortings are /new, /top, /hot and /rising")
print()

print("Remember! You can scroll to the bottom of the console to search again")
print()
search = input("Search.... ")
print()

while search != "Exit":
  if(search == "Popular"):
    url = 'https://www.reddit.com/r/popular/' 
   
    subreddit_keywords = []
    response = requests.get(url, headers=headers)
  # from example code
    soup = BeautifulSoup(response.content, 'lxml')
    print("r/"+search)
    for item in soup.select('.Post'):
      titles = item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text() #title
      titles = str(titles)
      subreddit_keywords.append(titles)
      listToStr = ' '.join(map(str, subreddit_keywords))
      #print(split_titles)
      split_it = listToStr.split()
    Counter = Counter(split_it)
    
        # most_common() produces k frequently encountered
        # input values and their respective counts.
    most_occur = Counter.most_common(15)
    print()
    print('----------------------------------------')
    print()      
    print("Most popular keywords: "+str(most_occur))
  
   

    
    

    

      #subreddit_keywords.append(titles)
    
    
    
    
    
  else:
    url = f'https://www.reddit.com/r/' +str(search) + '/' 
    print("r/"+ search)
    
  
  if(search == "Commands"):
    clearConsole()
    print("Commands")
    print()
    print("Type the subreddit you want to scrap. Please spell it correctly or the scrapper might not be able to pull up anything. No spaces!")
    print()
    print("Type 'Exit' to end reddit scrapper.")
    print()
    print("Type 'Popular' to see top posts on reddit.")
    print()
    print("Type Search History to see your search history")
    print()
    print("You can also enter your subreddit and put a /new or /top to sort through posts")
    print("Example: typing 'aww/new' gets you all the new posts for the aww subreddit")
    print("Acceptable sortings are /new, /top, /hot and /rising")
    print()
    print("Remember! You can scroll to the bottom of the console to search again")
    print()
    url = "https://www.reddit.com/dss"
  if(search == "Search History"):
    clearConsole()
    print("Search History")
    print()
    enumerate(search_history)
    print(search_history)
    url = "https://www.reddit.com/dss"
 


  response = requests.get(url, headers=headers)
# from example code
  soup = BeautifulSoup(response.content, 'lxml')
  search_history.append(search)
  
  #post_img = soup.select("span .SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
  #post_link = soup.select("span .chart-element__information__artist  ")
  
  for item in soup.select('.Post'):
    try:
        print()
        print('----------------------------------------')

       #{item.select('._3jOxDPIQ0KaOWpzvSQo-1s')[0].get_text()}
        print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text()) #title
        print()
        print(f"Posted {item.select('._3jOxDPIQ0KaOWpzvSQo-1s')[0].get_text()}") # date posted
        print()
        print(f"{item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text()} upvotes") # number of upvotes
        print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text()) # number of comments
        print()
        print(f"Link: {item.select('._3jOxDPIQ0KaOWpzvSQo-1s')[0]['href']}")	# Link to post
    except Exception as e:
        #raise e
        print('')
  print()
  print('----------------------------------------')
  search = input("Search.... ")
  clearConsole()
print("Thanks for using Reddit Scrapper. Goodbye")