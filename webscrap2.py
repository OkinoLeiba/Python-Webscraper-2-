#import the modules
import json, re
from urllib import request, parse


class HTMLParser(HTMLParser):
    from html.parser import HTMLParser
    def handle_starttag(self, tag, attrs) -> None:
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag) -> None:
        print("End tag  :", tag)

        print("Data     :", data)

    def handle_comment(self, data) -> None:
        print("Comment  :", data)

    def handle_charref(self, name) -> None:
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data) -> None:
        print("Decl     :", data)




#Option 1: Search data from url request by parser
def user_parser(data) -> None:
    """
    param = parse.urlencode(search_param = input("Input Search Parameters: "))
    param_url = data % param
    with urllib.request.urlopen(param_url) as file:
        print(file.read().decode('utf-8'))
    """
    search_param = input("Input Search Parameters: ")
    #parse_data = HTMLParser.feed(url_data)


    parser = HTMLParser()
    #parser.feed(data=url_data)
    parser.feed(data)
    



    def handle_data(self, url_data) -> None:
        self.url_data = url_data
        print(re.findall(search_param, self.url_data))
           

#Option 2: Search data from url request by REGEX
def search(str_data) -> None:
    param = input("Input Search Parameters: ")
    print(re.findall(param, str_data))
    print(re.findall("<"+param+">", str_data))     #(^[a-zA-Z0-9_ ]*$)</"+param+">", str_data))


    

    
#Tokenize url data by start and end tag
def tokenize(str_data, url_data) -> List:
    return token_specification = []



#URL builder: user-defined header 
def url_builder(input_url) -> None:
    url_builder = request.build_opener()
    #define and append header fields as needed
    url_builder.addheaders = ([("User-Agent", "Mozilla/5.0")])
    #("Upgrade", "HTTPS/1.3")]),("Accept-Language", "en_US")
    #url_builder.open(input_url)
  
    #Build data packet and convert to JSON
    with request.urlopen(input_url) as file:
        data = file.read()
        str_data = data.decode("utf-8")
      
        

    with url_builder.open(input_url) as file:
        data = file.read()
        url_data = data.decode("utf-8")

    #search(str_data)
    user_parser(data)
   
    



#Get the feed
#http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc
#https://www.youtube.com/watch?v=PxVQvCoMfIA&ab_channel=AceKxNightcore
input_url = input("Input URL: ")
url_builder(input_url)


#req = request.open(input_url)
#req.text

#with request.urlopen(input_url) as file:
#       data = json.load(file.read())

## Convert to a Python dictionary
#data = json.loads(reg.text)

