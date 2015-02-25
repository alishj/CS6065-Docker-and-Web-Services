# Author: Sean Schatzman
# Cloud Computing Homework 2: Docker and Web Services
# Spirit Animal Generator
# Usage: Enter http://127.0.0.1:8080/spirit?animals= into your browser, adding to the end of the url one of the animals 
#           listed in the dictionary below (i.e. http://127.0.0.1:8080/spirit?animals=Bear )
# Output: Returns a JSON object containing spiritanimal.info description and urbandictionary.com meaning and examples for the animal.

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from bs4 import BeautifulSoup
import urlparse
import sys
import json
import requests

PORT = 8080

#Dictionary containing animals
animals = dict({
    "Bear": dict({"url":"http://www.spiritanimal.info/bear-spirit-animal/"}),
    "Butterfly": dict({"url":"http://www.spiritanimal.info/butterfly-spirit-animal/"}),
    "Cat": dict({"url":"http://www.spiritanimal.info/cat-spirit-animal/"}),
    "Coyote": dict({"url":"http://www.spiritanimal.info/coyote-spirit-animal/"}),
    "Crow": dict({"url":"http://www.spiritanimal.info/crow-spirit-animal/"}),
    "Deer": dict({"url":"http://www.spiritanimal.info/deer-spirit-animal/"}),
    "Dolphin": dict({"url":"http://www.spiritanimal.info/dolphin-spirit-animal/"}),
    "Dragonfly": dict({"url":"http://www.spiritanimal.info/dragonfly-spirit-animal/"}),
    "Fox": dict({"url":"http://www.spiritanimal.info/fox-spirit-animal/"}),
    "Frog": dict({"url":"http://www.spiritanimal.info/frog-spirit-animal/"}),
    "Hawk": dict({"url":"http://www.spiritanimal.info/hawk-spirit-animal/"}),
    "Horse": dict({"url":"http://www.spiritanimal.info/horse-spirit-animal/"}),
    "Hummingbird": dict({"url":"http://www.spiritanimal.info/hummingbird-spirit-animal/"}),
    "Lion": dict({"url":"http://www.spiritanimal.info/lion-spirit-animal/"}),
    "Owl": dict({"url":"http://www.spiritanimal.info/owl-spirit-animal/"}),
    "Panda": dict({"url":"http://www.spiritanimal.info/panda-spirit-animal/"}),
    "Sheep": dict({"url":"http://www.spiritanimal.info/sheep-spirit-animal/"}),
    "Snake": dict({"url":"http://www.spiritanimal.info/snake-spirit-animal/"}),
    "Spider": dict({"url":"http://www.spiritanimal.info/spider-spirit-animal/"}),
    "Tiger": dict({"url":"http://www.spiritanimal.info/tiger-spirit-animal/"}),
    "Turtle": dict({"url":"http://www.spiritanimal.info/turtle-spirit-animal/"}),
    "Wolf": dict({"url":"http://www.spiritanimal.info/wolf-spirit-animal/"}),
    "Whale": dict({"url":"http://www.spiritanimal.info/whale-spirit-animal/"}),
    "Panther": dict({"url":"http://www.spiritanimal.info/panther-spirit-animal/"})
})

class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.startswith("/spirit"):
            ws_url = urlparse.urlparse(self.path)
            getvars = urlparse.parse_qs(ws_url.query)
            try:
                self.send_response(200)
                self.send_header('Content-type','application/json')
                self.end_headers()
                
                user_animal = getvars['animals'][0]
                
                # Get description from spirit animal site
                spirit_url = animals[user_animal]['url']
                spirit_page = requests.get(spirit_url)
                spirit_html = spirit_page.content
                spirit_soup = BeautifulSoup(spirit_html)
                spirit_description = spirit_soup.find(id='article-intro-text').text.encode('ascii', 'ignore')
                resp_dict = dict({user_animal: dict({'spirit_description': spirit_description})})
                
                '''
                #Just felt like taking this Wiki part out
                # Get Wikipedia extract for animal 
                wiki_url = 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=' + user_animal
                r = requests.get(wiki_url)
                json_data = r.json()
                id_key = json_data['query']['pages'].keys().pop()
                extract = json_data['query']['pages'][id_key]['extract']
                #wiki_extract_html = '<b>From Wikipedia: </b><div><p>'+extract+'</p></div><br/>'
                '''
                
                # Get Urban Dictionary meaning and examples for animal
                urban_url = 'http://www.urbandictionary.com/define.php?term=' + user_animal
                urban_page = requests.get(urban_url)
                urban_html = urban_page.content
                urban_soup = BeautifulSoup(urban_html)
                urban_meaning = urban_soup.find_all('div',class_='meaning')[0].text.encode('ascii', 'ignore')
                urban_example = urban_soup.find_all('div',class_='example')[0].text.encode('ascii', 'ignore')
                resp_dict[user_animal]['urban_meaning'] = urban_meaning
                resp_dict[user_animal]['urban_example'] = urban_example
                
                self.wfile.write(json.dumps( resp_dict ))
                
                return
                
            except:
                e = sys.exc_info()[0]
                self.send_error(404,'Error, please try again' + str(e))

        self.send_error(404,'Resource Not Found')
        
if __name__ == "__main__":
    try:
        #Create a web server and define the handler to manage the incoming request
        server = HTTPServer(('', PORT), myHandler)
        print 'Started httpserver on port ' , PORT

        #Wait forever for incoming http requests
        server.serve_forever()

    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()