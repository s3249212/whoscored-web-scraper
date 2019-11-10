import dryscrape

url = "https://www.whoscored.com/Players/13756/History/Mesut-%C3%96zil"

session = dryscrape.Session()
session.visit(url)
website_string = session.body()

print(website_string.replace('>', '>\n').replace('<', '\n<').replace('\n\n', '\n'))
