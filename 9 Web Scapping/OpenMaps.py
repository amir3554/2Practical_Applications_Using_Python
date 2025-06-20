import webbrowser, sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    webbrowser.open(f'https://www.google.com/maps/place/{address}') 
 
else:
    print("You have not entered a value. ")