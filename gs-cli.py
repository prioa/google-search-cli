# google-seach-cli.py

import sys
import webbrowser 

base_url = "http://www.google.com/search?q="

if len(sys.argv) > 1:
    print("Opening Webbrowser...")
    for i in sys.argv[1:]:
        search_query = '+'.join(sys.argv[1:])
    webbrowser.open_new_tab(base_url + search_query)

else:
    print("please enter search term")
