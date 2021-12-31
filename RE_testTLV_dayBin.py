# A Script to test the RE_TLV class
# September 25, 2021
# Able Kirby

# Instructions:
# Export invoices from RTL as a .csv file
# run      python RE_testTLV.py [csv file name]


from RE_TLV import RE_TLV
import sys
from datetime import datetime, timezone, timedelta
import pytz
import matplotlib.pyplot as plt

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


rdates = []
sdates_RE = []
sdates_AK = []
sdates_AW = []
sdates = []
days_back = 60
rnow = datetime.now()
rnow = rnow.replace(tzinfo=pytz.timezone('US/Eastern'))
for i in range(0,days_back):
    rdates.append(rnow - timedelta(i))
    sdates.append(0)
    sdates_RE.append(0)
    sdates_AK.append(0)
    sdates_AW.append(0)


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

            for i in range(1,days_back):
                if tlvdate > rdates[i] and tlvdate <= rdates[i-1]:

                    showname = mytlv.getShowName()

                    if showname == "Rare Encounter":
                        sdates_RE[i] += mytlv.getAmmountInt()
                    elif showname == "AbleKraft":
                        sdates_AK[i] += mytlv.getAmmountInt()
                    elif showname == "Stay Awhile":
                        sdates_AW[i] += mytlv.getAmmountInt()

                    sdates[i] += mytlv.getAmmountInt()


            mytlvs.append(mytlv)
        except:
            pass


    else:
        #print("BadLine")
        pass

# Print by day
for i in range(1,days_back):
    print(rdates[i].strftime("%b %d") + " = " + str(sdates[i]) + " sats")

# Chart
plt.plot(rdates,sdates, label = "Total")
plt.plot(rdates,sdates_RE, label = "Rare Encounter")
plt.plot(rdates,sdates_AK, label = "AbleKraft")
plt.plot(rdates,sdates_AW, label = "Able and The Wolf")
plt.grid()
plt.xlabel('Date')
plt.ylabel('Sats')
plt.title("Able Kirby [node]\nLast 60 days of activity from " + fn)
plt.legend()
plt.show()