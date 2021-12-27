# A Script to test the RE_TLV class
# September 25, 2021
# Able Kirby

# Instructions:
# Export invoices from RTL as a .csv file
# run      python RE_testTLV.py [csv file name]


from RE_TLV import RE_TLV
import sys

# Load RTL exported records
#fn = sys.argv[1]
fn = "merged.csv"
with open(fn,mode='r') as file:
    #file.seek(3) # discard BOM
    #file.readline() #discard first line (header)
    csvlines = file.readlines() 

print("")
appsum = []
apps = []
boostsum = []
boosters = []
episodes = []
episodesum = []
sats_of_unknown_origin = 0
unidentified_transactions = 0
print("---TLV Messages---")

# For every record in file
for line in csvlines:
    if line[0:3] != "ï»¿":
        
        mytlv = RE_TLV.fromcsv(line)
        asats = mytlv.getAmmountInt()
        # Collate sats by show
        ep = mytlv.getShowName() + " - " + mytlv.getEpName()
        try:
            ind = episodes.index(ep)
            episodesum[ind] += asats
        except:
            episodes.append(ep)
            episodesum.append(asats)
    else:
        print("BadLine")


# Print sats by episode
print("---Sats by Show Streaming Apps---")
for i in range(len(episodes)):
    print(episodes[i] + " = " + str(episodesum[i]) + " sats")
#print("\tTotal From Streams: " + str(sum(appsum)) + " sats")
print("")