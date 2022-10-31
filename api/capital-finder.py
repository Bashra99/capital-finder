from http.server import BaseHTTPRequestHandler
from urllib import parse 
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
       s= self.path
       url_components = parse.urlsplit(s)
       query_string_list = parse.parse_qsl(url_components.query)
       dictionary = dict(query_string_list)

       if 'country' in dictionary:
            country = dictionary['country']
            url=f'https://restcountries.com/v3.1/name/{country}'
            response = requests.get(url)
            data = response.json()
            capital =str(data[0]['capital'][0])
            massage=f'The capital of {country} is {capital}.'
       elif 'capital' in dictionary:
            capital = dictionary['capital']
            url=f'https://restcountries.com/v3.1/capital/{capital}'
            response = requests.get(url)
            data = response.json()
            country = data[0]['name']['common']
            massage=f'{capital} is the capital of {country}.'
       else:
           massage="please enter country or capital"



       self.send_response(200)
       self.send_header('Content-type','text/plain')
       self.end_headers()
       self.wfile.write(str(massage).encode())
       return
