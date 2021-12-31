# A Script to test the RE_TLV class
# September 25, 2021
# Able Kirby

# Instructions:
# Export invoices from RTL as a .csv file
# run      python RE_testTLV.py [csv file name]


from RE_TLV import RE_TLV
import sys
from datetime import datetime, timezone
import pytz

# Load RTL exported records
#fn = sys.argv[1]
fn = "merged.csv"
#fn = "Invoices_20211209_to_20211215.csv"
with open(fn,mode='r') as file:
    #file.seek(3) # discard BOM
    #file.readline() #discard first line (header)
    csvlines = file.readlines() 

print("")
appsum = []
apps = []
boostsum = []
boosters = []
streamers = []
streamsum = []
sats_of_unknown_origin = 0
unidentified_transactions = 0
print("---TLV Messages---")

startdate = datetime(2021,12,22,19,0,tzinfo=pytz.timezone('US/Eastern'))
enddate = datetime(2021,12,29,19,0,tzinfo=pytz.timezone('US/Eastern'))

# For every record in file
mytlvs = []
for line in csvlines:
    mytlv = RE_TLV.fromcsv(line)
    if line[0:3] != "ï»¿":
        
        mytlv = RE_TLV.fromcsv(line)

        try:
            tlvdate = datetime.strptime(mytlv.getDate(), '%d/%b/%Y %H:%M')
            tlvdate = tlvdate.replace(tzinfo=timezone.utc)
            tlvdate = tlvdate.astimezone(pytz.timezone('US/Eastern'))

            if tlvdate > startdate and tlvdate <= enddate:
                mytlvs.append(mytlv)

        except:
            pass


    else:
        #print("BadLine")
        pass






    # Collate streaming sats by app
for mytlv in mytlvs:

    asats = mytlv.getAmmountInt()
    rdate = mytlv.getDate()


    app = mytlv.getSenderApp()
    asats = mytlv.getAmmountInt()
    streamer = mytlv.getSenderName()
    if not streamer:
        streamer = "Unknown Streamer"
    try:
        ind = streamers.index(streamer)
        streamsum[ind] += asats
    except:
        streamers.append(streamer)
        streamsum.append(asats)
        
        

    # Collate Boosts by name
    if mytlv.isBoost():
        booster = mytlv.getSenderName()
        bsats = mytlv.getAmmountInt()
        if not booster:
            booster = "U.B.M. (Unknown Boosting Maniac)"
        try:
            ind = boosters.index(booster)
            boostsum[ind] += bsats
        except:
            boosters.append(booster)
            boostsum.append(bsats)
    else:
        sats_of_unknown_origin += mytlv.getAmmountInt()
        unidentified_transactions += 1

    # Print any messages
    #if mytlv.hasMessage():
    #    # print("Record Number: " + mytlv.getRecordNum())
    #    print("\tShow Name: " + mytlv.getShowName())
    #    print("\tAmmount: " + mytlv.getAmmount() + " sats")
    #    print("\tDate: " + mytlv.getDate() + " UTC")
    #    print("\tSender Name: " + mytlv.getSenderName())
    #    print("\tSender App: " +  mytlv.getSenderApp())
    #    print("\tMessage Text: " + mytlv.getMessage())
    #    print("")



# Sort streamers by totals
streamsum, streamers = (list(t) for t in zip(*sorted(zip(streamsum, streamers),reverse=True)))

# Print unique list of Streamers
print("---Streamer Leaderboard---")
for i in range(len(streamers)):
    print(streamers[i] + " = " + str(streamsum[i]) + " sats")
print("\tTotal From Streams: " + str(sum(streamsum)) + " sats")
print("")


# Print unique list of Apps
#print("---Sats From Streaming Apps---")
#for i in range(len(apps)):
#    print(apps[i] + " = " + str(appsum[i]) + " sats")
#print("\tTotal From Streams: " + str(sum(appsum)) + " sats")
#print("")

# Print unique list of Boosters
#print("---Sats From Boosters---")
#for i in range(len(boosters)):
#    print(boosters[i] + " = " + str(boostsum[i]) + " sats")
#print("\tTotal From Boosts: " + str(sum(boostsum)) + " sats")
#print("")

# Print Everything else
#print("---Sats of Unidentified Origin---")
#print(str(sats_of_unknown_origin) + " sats in " + str(unidentified_transactions) + " transactions\n")
