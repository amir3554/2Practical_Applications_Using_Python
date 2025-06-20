import imaplib
import imapclient
import pprint
import pyzmail



try:
    IMAP_Object = imapclient.IMAPClient('imap.example.com', ssl=True)
    IMAP_Object.login("amirdwikat@example.com", password='vmru kdjj mllu vcct')
    '''
    pprint.pprint(IMAP_Object.list_folders)
    IMAP_Object.select_folder("INBOX", readonly=True)
    IMAP_Object.search("ALL")
    IMAP_Object.search("ON 01-Jan-2025")
    IMAP_Object.search(["SINCE 04-Jul-2024", "BEFORE 04-Aug-2024", "UNSEEN"])
    IMAP_Object.search("SINCE 04-Dec-2024", "FROM hello@duolingo.com")
    IMAP_Object.search("SINCE 10-Nov-2024", "NOT FROM english-personlized-digest@quora.com")
    '''


    #pprint.pprint(IMAP_Object.list_folders()) 
    IMAP_Object.select_folder("INBOX", readonly=True)
    UIds = IMAP_Object.search("ALL")
    #print(len(UIds))


    row_massages = IMAP_Object.fetch(UIds, ["BODY[]"])
    row_massages_obj = pyzmail.PyzMessage.factory(row_massages[5555][b'BODY[]'])

    print(row_massages_obj.get_subject()) 
    print(row_massages_obj.get_addresses("From"))
    print(row_massages_obj.get_addresses("To"))

    print(row_massages_obj.text_part.get_payload().decode(row_massages_obj.text_part.charset))

except Exception as e:
    print(f"This is an error .... ->\n{e}")