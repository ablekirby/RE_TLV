# A Script to test the RE_TLV class
# September 25, 2021
# Able Kirby

# Instructions:
# Export invoices from RTL as a .csv file
# run      python RE_testTLV.py [csv file name]


from RE_TLV import RE_TLV
import sys

# Load RTL exported records
fn = sys.argv[1]
with open(fn,mode='r') as file:
    file.seek(3) # discard BOM
    file.readline() #discard first line (header)
    csvlines = file.readlines() 

print("")
appsum = []
apps = []
boostsum = []
boosters = []
sats_of_unknown_origin = 0
unidentified_transactions = 0
print("---TLV Messages---")

# For every record in file
for line in csvlines:
    mytlv = RE_TLV.fromcsv(line)
    # Collate streaming sats by app
    if not mytlv.isBoost():
        app = mytlv.getSenderApp()
        asats = mytlv.getAmmountInt()
        if not app:
            app = "Unknown App"
        try:
            ind = apps.index(app)
            appsum[ind] += asats
        except:
            apps.append(app)
            appsum.append(asats)

    # Collate Boosts by name
    elif mytlv.isBoost():
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
        unresolved_transactions += 1

    # Print any messages
    if mytlv.hasMessage():
        print("Record Number: " + mytlv.getRecordNum())
        print("\tAmmount: " + mytlv.getAmmount() + " sats")
        print("\tDate: " + mytlv.getDate() + " UTC")
        print("\tSender Name: " + mytlv.getSenderName())
        print("\tSender App: " +  mytlv.getSenderApp())
        print("\tMessage Text: " + mytlv.getMessage())
        print("")

# Print unique list of Apps
print("---Sats From Streaming Apps---")
for i in range(len(apps)):
    print(apps[i] + " = " + str(appsum[i]) + " sats")
print("\tTotal From Streams: " + str(sum(appsum)) + " sats")
print("")

# Print unique list of Boosters
print("---Sats From Boosters---")
for i in range(len(boosters)):
    print(boosters[i] + " = " + str(boostsum[i]) + " sats")
print("\tTotal From Boosts: " + str(sum(boostsum)) + " sats")
print("")

# Print Everything else
print("---Sats of Unidentified Origin---")
print(str(sats_of_unknown_origin) + " sats in " + str(unidentified_transactions) + " transactions\n")