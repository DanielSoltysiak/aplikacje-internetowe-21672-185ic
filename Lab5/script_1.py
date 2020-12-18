import requests
from bs4 import BeautifulSoup



def script( soup ):
    print( "Nazwa filmu", soup.select( "h1" )[ 0 ].text )
    print( "Opis:", soup.select( "p" )[ 0 ].text )