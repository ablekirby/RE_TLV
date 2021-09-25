# A Script to test the RE_TLV class
# September 25, 2021
# Able Kirby

# Instructions:
# Export invoices from RTL as a .csv file
# run      python RE_testTLV.py [csv file name]

from RE_TLV import RE_TLV
import json

# Load RTL exported records

tlv1 = {'rPreimage': 'ObShjs80OgFkpHVXC3Dxnpj3HGIjCdlK84S9X3Ws/tE=', 'rHash': 'oaX5dnvvLHzei6yLwqqWr/Tl7QkuSUVPfkQ+T+YYg5s=', 'value': '4', 'settled': True, 'creationDate': '1631639414', 'settleDate': '1631639414', 'cltvExpiry': '13', 'addIndex': '96', 'settleIndex': '96', 'amtPaid': '4000', 'amtPaidSat': '4', 'amtPaidMsat': '4000', 'state': 'SETTLED', 'htlcs': [{'chanId': '759373307773321217', 'htlcIndex': '73', 'amtMsat': '4000', 'acceptHeight': 700542, 'acceptTime': '1631639414', 'resolveTime': '1631639414', 'expiryHeight': 700585, 'state': 'SETTLED', 'customRecords': {'7629169': 'eyJwb2RjYXN0IjoiQWJsZUtyYWZ0IiwiZmVlZElEIjo0MDg4MDM4LCJlcGlzb2RlIjoiQSBIYW5nb3ZlciBTb25nIiwiYWN0aW9uIjoic3RyZWFtIiwidHMiOjEzODYsImFwcF9uYW1lIjoiQ3VyaW9DYXN0ZXIiLCJzcGVlZCI6MSwibmFtZSI6IkFibGUgS2lyYnkiLCJ1cmwiOiJodHRwczovL2ZlZWRzLmJ1enpzcHJvdXQuY29tLzE4MTk3NzMucnNzIiwic2VuZGVyX2lkIjoiVnVlTFU5Q0YyOGN3YWhUdkhVR0FUc0djIn0=', '5482373484': 'ObShjs80OgFkpHVXC3Dxnpj3HGIjCdlK84S9X3Ws/tE='}}], 'valueMsat': '4000', 'features': {'9': {'name': 'tlv-onion', 'isKnown': True}}, 'isKeysend': True, 'paymentAddr': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='}
tlv2 = {'rPreimage': 'PCv891DX0LO4A9HVapbanLUzNWDwBf49ygh6OBlPevQ=', 'rHash': 'MxNVl57VMDg7khorf35PG3F7zRg7/x1wPd1rElb8i5E=', 'value': '4', 'settled': True, 'creationDate': '1631639229', 'settleDate': '1631639229', 'cltvExpiry': '13', 'addIndex': '95', 'settleIndex': '95', 'amtPaid': '4000', 'amtPaidSat': '4', 'amtPaidMsat': '4000', 'state': 'SETTLED', 'htlcs': [{'chanId': '759494254085603328', 'htlcIndex': '108', 'amtMsat': '4000', 'acceptHeight': 700540, 'acceptTime': '1631639229', 'resolveTime': '1631639229', 'expiryHeight': 700583, 'state': 'SETTLED', 'customRecords': {'7629169': 'eyJwb2RjYXN0IjoiQWJsZUtyYWZ0IiwiZmVlZElEIjo0MDg4MDM4LCJlcGlzb2RlIjoiQSBIYW5nb3ZlciBTb25nIiwiYWN0aW9uIjoic3RyZWFtIiwidHMiOjEzOTEsImFwcF9uYW1lIjoiQ3VyaW9DYXN0ZXIiLCJzcGVlZCI6MSwibmFtZSI6IkFibGUgS2lyYnkiLCJ1cmwiOiJodHRwczovL2ZlZWRzLmJ1enpzcHJvdXQuY29tLzE4MTk3NzMucnNzIiwic2VuZGVyX2lkIjoiVnVlTFU5Q0YyOGN3YWhUdkhVR0FUc0djIn0=', '5482373484': 'PCv891DX0LO4A9HVapbanLUzNWDwBf49ygh6OBlPevQ='}}], 'valueMsat': '4000', 'features': {'9': {'name': 'tlv-onion', 'isKnown': True}}, 'isKeysend': True, 'paymentAddr': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='}
tlv3 = {'rPreimage': 'ldJLJLmVVPRNPIV5K8UFsEhfTXrZJStju6kcmrWOf7c=', 'rHash': 'k131WvvTIlZBVIIcE1qJCGfyKz5lrYHRcds3OeYdqTE=', 'value': '533', 'settled': True, 'creationDate': '1631639911', 'settleDate': '1631639911', 'cltvExpiry': '13', 'addIndex': '106', 'settleIndex': '106', 'amtPaid': '533000', 'amtPaidSat': '533', 'amtPaidMsat': '533000', 'state': 'SETTLED', 'htlcs': [{'chanId': '759494254085603328', 'htlcIndex': '110', 'amtMsat': '533000', 'acceptHeight': 700543, 'acceptTime': '1631639911', 'resolveTime': '1631639911', 'expiryHeight': 700586, 'state': 'SETTLED', 'customRecords': {'5482373484': 'ldJLJLmVVPRNPIV5K8UFsEhfTXrZJStju6kcmrWOf7c=', '7629169': 'eyJwb2RjYXN0IjoiQWJsZUtyYWZ0IiwiZmVlZElEIjo0MDg4MDM4LCJlcGlzb2RlIjoiQSBIYW5nb3ZlciBTb25nIiwiYWN0aW9uIjoiYm9vc3QiLCJ0cyI6MTg3OCwiYXBwX25hbWUiOiJDdXJpb0Nhc3RlciIsImJvb3N0X2xpbmsiOiJodHRwczovL2N1cmlvY2FzdGVyLmNvbS8jY2xpcC1jRzlrWTJGemREbzBNRGc0TURNNEptVndhWE52WkdVNlFuVjZlbk53Y205MWRDMDVNVFk0T0RVd0puUnBiV1U2TVRnM09BIiwic3BlZWQiOjEsInZhbHVlX21zYXQiOjUzMzAwMCwidmFsdWVfbXNhdF90b3RhbCI6MTExMTAwMCwidXJsIjoiaHR0cHM6Ly9mZWVkcy5idXp6c3Byb3V0LmNvbS8xODE5NzczLnJzcyIsIm5hbWUiOiJBYmxlIEtpcmJ5Iiwic2VuZGVyX2lkIjoiVnVlTFU5Q0YyOGN3YWhUdkhVR0FUc0djIn0='}}], 'valueMsat': '533000', 'features': {'9': {'name': 'tlv-onion', 'isKnown': True}}, 'isKeysend': True, 'paymentAddr': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='}
tlv4 = {'rPreimage': 'USghNLUon3hn0F4KJY5WBXdQGtsZ8U5LMhaiMU+6u6M=', 'rHash': 'dxO7bJ7PCbYN4dW0YlseYnqzrNj7w0AZblZ40+o8LLw=', 'value': '1584', 'settled': True, 'creationDate': '1631935403', 'settleDate': '1631935403', 'cltvExpiry': '13', 'addIndex': '225', 'settleIndex': '225', 'amtPaid': '1584000', 'amtPaidSat': '1584', 'amtPaidMsat': '1584000', 'state': 'SETTLED', 'htlcs': [{'chanId': '759494254085603328', 'htlcIndex': '147', 'amtMsat': '1584000', 'acceptHeight': 701034, 'acceptTime': '1631935403', 'resolveTime': '1631935403', 'expiryHeight': 701077, 'state': 'SETTLED', 'customRecords': {'5482373484': 'USghNLUon3hn0F4KJY5WBXdQGtsZ8U5LMhaiMU+6u6M=', '7629169': 'eyJwb2RjYXN0IjoiQWJsZUtyYWZ0IiwiZmVlZElEIjo0MDg4MDM4LCJlcGlzb2RlIjoiQm9vc3RpbmcgdGhlIEJyZWFkIiwiYWN0aW9uIjoiYm9vc3QiLCJ0cyI6MjM1MSwiYXBwX25hbWUiOiJDdXJpb0Nhc3RlciIsImJvb3N0X2xpbmsiOiJodHRwczovL2N1cmlvY2FzdGVyLmNvbS8jY2xpcC1jRzlrWTJGemREbzBNRGc0TURNNEptVndhWE52WkdVNlFuVjZlbk53Y205MWRDMDVNakUxTkRjekpuUnBiV1U2TWpNMU1RIiwic3BlZWQiOjEsInZhbHVlX21zYXQiOjE1ODQwMDAsInZhbHVlX21zYXRfdG90YWwiOjMzMDAwMDAsInVybCI6Imh0dHBzOi8vZmVlZHMuYnV6enNwcm91dC5jb20vMTgxOTc3My5yc3MiLCJuYW1lIjoiQWJsZSBLaXJieSIsInNlbmRlcl9pZCI6IlZ1ZUxVOUNGMjhjd2FoVHZIVUdBVHNHYyJ9'}}], 'valueMsat': '1584000', 'features': {'9': {'name': 'tlv-onion', 'isKnown': True}}, 'isKeysend': True, 'paymentAddr': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='}

mytlv = RE_TLV.fromJSON(tlv1)

print(mytlv.getAmmount())


# print("")
# appsum = []
# apps = []
# boostsum = []
# boosters = []
# sats_of_unknown_origin = 0
# unidentified_transactions = 0
# print("---TLV Messages---")

# # For every record in file
# for line in csvlines:
#     mytlv = RE_TLV.fromcsv(line)
#     # Collate streaming sats by app
#     if not mytlv.isBoost():
#         app = mytlv.getSenderApp()
#         asats = mytlv.getAmmountInt()
#         if not app:
#             app = "Unknown App"
#         try:
#             ind = apps.index(app)
#             appsum[ind] += asats
#         except:
#             apps.append(app)
#             appsum.append(asats)

#     # Collate Boosts by name
#     elif mytlv.isBoost():
#         booster = mytlv.getSenderName()
#         bsats = mytlv.getAmmountInt()
#         if not booster:
#             booster = "U.B.M. (Unknown Boosting Maniac)"
#         try:
#             ind = boosters.index(booster)
#             boostsum[ind] += bsats
#         except:
#             boosters.append(booster)
#             boostsum.append(bsats)
#     else:
#         sats_of_unknown_origin += mytlv.getAmmountInt()
#         unresolved_transactions += 1

#     # Print any messages
#     if mytlv.hasMessage():
#         print("Record Number: " + mytlv.getRecordNum())
#         print("\tAmmount: " + mytlv.getAmmount() + " sats")
#         print("\tDate: " + mytlv.getDate() + " UTC")
#         print("\tSender Name: " + mytlv.getSenderName())
#         print("\tSender App: " +  mytlv.getSenderApp())
#         print("\tMessage Text: " + mytlv.getMessage())
#         print("")

# # Print unique list of Apps
# print("---Sats From Streaming Apps---")
# for i in range(0,len(apps)-1):
#     print(apps[i] + " = " + str(appsum[i]) + " sats")
# print("\tTotal From Streams: " + str(sum(appsum)) + " sats")
# print("")

# # Print unique list of Boosters
# print("---Sats From Boosters---")
# for i in range(0,len(boosters)-1):
#     print(boosters[i] + " = " + str(boostsum[i]) + " sats")
# print("\tTotal From Boosts: " + str(sum(boostsum)) + " sats")
# print("")

# # Print Everything else
# print("---Sats of Unidentified Origin---")
# print(str(sats_of_unknown_origin) + " sats in " + str(unidentified_transactions) + " transactions\n")