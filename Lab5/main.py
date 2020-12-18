from os import system, name
import requests
from bs4 import BeautifulSoup
from PIL import Image
import csv
import html_text
import webbrowser

from script_1 import script as script1
from script_2 import script as script2
from script_3 import script as script3
from script_4 import script as script4



page = requests.get( "https://www.filmweb.pl/film/Pok%C3%A9mon%3A+Film+pierwszy-1998-1506" )
soup = BeautifulSoup( page.content, "html.parser" )
scripts = [ script1, script2, script3, script4 ]



def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')



def main():
    end = False

    clear()

    while not end:
        print( "" )
        print( "Menu:" )
        print( " [1] Nazwa filmu i opis" )
        print( " [2] Powiązane filmy" )
        print( " [3] Wydobycie atrybutów alt/src ze wszystkich obrazków na stronie" )
        print( " [4] Skrypt 'web-scraping-example7'" )
        print( "  - - -" )
        print( " [q] Wyjście" )
        print( "" )

        choose = input( "Wprowadź pozycję z menu i zatwierdź enterem: " )

        print( "  -  Twoj wybor to: " + choose )

        if choose == "q":
            end = True

        else:
            try:
                print( "" )
                scripts[ int( choose ) - 1 ]( soup )
            except err:
                print( "  -  Coś poszło nie tak. Najprawdopodobniej wybrałeś niewłaściwą pozycję z menu" )

            print( "" )
            system( "pause" )

        clear()

    quit()



main()