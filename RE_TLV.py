# A class to parse TLV records and provide high level access to their contents available in various useful formats
# September 25, 2021
# Able Kirby

import json
import base64

class RE_TLV:
    def __init__(self):
        self.raw = []

    # Simple Get methods
    def getAmmount(self):
        amt = ''
        try:
            amt = self.amt_paid_sat
        except:
            pass
        return amt

    def getAmmountInt(self):
        return int(self.getAmmount())

    def getDate(self):
        date = ''
        try:
            date = self.settle_date_str
        except:
            pass
        return date

    def getFeatures(self):
        features = ''
        try:
            features = self.features
        except:
            pass
        return features

    def getHtlcs(self):
        htlcs = ''
        try:
            htlcs = self.htlcs
        except:
            pass
        return htlcs


    # START - Low level functions to parse custom records
    def getCustomRecords(self):
        crecords = ''
        htlcs = self.getHtlcs()
        try:
            crecords = htlcs["custom_records"]
        except:
            pass
        return crecords

    # Normal Podcast 2.0 Record
    def get7629169(self):
        crecords = self.getCustomRecords()
        crecord = ''
        try:
            crecord = crecords["7629169"]
            crecord = base64.b64decode(crecord)
            crecord = json.loads(crecord)
        except:
            pass
        return crecord

    # Sender name
    def get7629171(self):
        crecords = self.getCustomRecords()
        crecord = ''
        try:
            crecord = crecords["7629171"]
            crecord = base64.b64decode(crecord)
            crecord = crecord.decode("utf-8")
        except:
            pass
        return crecord

    # Normal Pre-image record.
    def get5482373484(self):
        crecords = self.getCustomRecords()
        crecord = ''
        try:
            crecord = crecords["5482373484"]
            #crecord = base64.b64decode(crecord)
            #crecord = crecord.decode('utf-8')
        except:
            pass
        return crecord

    # whatsat Message
    def get34349334(self):
        crecords = self.getCustomRecords()
        crecord = ''
        try:
            crecord = crecords["34349334"]
            crecord = base64.b64decode(crecord)
            crecord = crecord.decode('utf-8')
        except:
            pass
        return crecord
    
    # whatsat signature
    def get34349337(self):
        crecords = self.getCustomRecords()
        crecord = ''
        try:
            crecord = crecords["34349337"]
            #crecord = base64.b64decode(crecord)
            #crecord = crecord.decode('utf-8')
        except:
            pass
        return crecord

    # whatsat sender pubkey
    def get34349339(self):
        crecords = self.getCustomRecords()
        crecord = ''
        try:
            crecord = crecords["34349339"]
            #crecord = base64.b64decode(crecord)
            #crecord = crecord.decode('utf-8')
        except:
            pass
        return crecord

    # Thunderhub (whatsat?) sender name
    def get34349340(self):
        crecords = self.getCustomRecords()
        crecord = ''
        try:
            crecord = crecords["34349340"]
            crecord = base64.b64decode(crecord)
            crecord = crecord.decode('utf-8')
        except:
            pass
        return crecord
    
    # Thunder-Hub Content Type
    def get34349345(self):
        crecords = self.getCustomRecords()
        crecord = ''
        try:
            crecord = crecords["34349345"]
            crecord = base64.b64decode(crecord)
            crecord = crecord.decode('utf-8')
        except:
            pass
        return crecord
    
    # Thunder-Hub Request Type
    def get34349347(self):
        crecords = self.getCustomRecords()
        crecord = ''
        try:
            crecord = crecords["34349347"]
            crecord = base64.b64decode(crecord)
            crecord = crecord.decode('utf-8')
        except:
            pass
        return crecord
    
    # More High-Level commands
    def getSenderName(self):
        name = ""

        # Check for boost-a-gram name first
        r = self.get7629169()
        try:
            name = r["sender_name"]
        except:
            pass

        if not name:
            try:
                name = self.get7629171()
            except:
                pass

        # Try thunderhub / whatsat 
        if not name:
            try:
                name =  self.get34349340()
            except:
                pass
        
        return name

    def getSenderApp(self):
        senderApp = ""

        # Try boost-a-gram app field first
        r7629169 = self.get7629169()
        try:
            senderApp = r7629169["app_name"]
        except:
            pass

        # Try whatsat
        if not senderApp:
            # Is this a whatsat message?
            if self.get34349339():
                senderApp = "Whatsat"
        
        return senderApp

    def getMessage(self):
        
        message = ""

        # Try Thunderhub Style
        try:
            message = self.get34349334()
        except:
            pass
        
        # Try message filed
        r7629169 = self.get7629169()
        try:
            message = r7629169["message"]
        except:
            pass

        return message

    def getRecordNum(self):
        recordNum = ""
        try:
            recordNum = self.add_index
        except:
            pass
        return recordNum

    def hasMessage(self):
        hasMessage = False
        if len(self.getMessage()) > 0:
            hasMessage = True
        return hasMessage

    def isBoost(self):
        isBoost = False
        r = self.get7629169()
        try:
            if r["action"] == "boost":
                isBoost = True
        except:
            pass
        return isBoost

    def isStream(self):
        isStream = False
        r = self.get7629169()
        try:
            if r["action"] == "stream":
                isStream = True
        except:
            pass
        return isStream

    @staticmethod
    # Method to import CSV format records, as downloaded from RTL (Ride The Lightning)
    def fromcsv(str):
        self = RE_TLV()
        self.raw = str

        str = str.split(',')

        #
        self.memo = str[0]
        self.r_preimage = str[1]
        self.r_hash = str[2]
        self.value = str[3]
        self.value_msat = str[4]
        self.settled = str[5]
        self.creation_date = str[6]
        self.settle_date = str[7]
        self.payment_request = str[8]
        self.description_hash = str[9]
        self.expiry = str[10]
        self.fallback_addr = str[11]
        self.cltv_expiry = str[12]
        self.route_hints = str[13]
        self.private = str[14]
        self.add_index = str[15]
        self.settle_index = str[16]
        self.amt_paid = str[17]
        self.amt_paid_sat = str[18]
        self.amt_paid_msat = str[19]
        self.state = str[20]
        
        # Parse semi-colon seperated JSON
        try:
            self.htlcs = json.loads(str[21].replace(';',',')[1:-1])
        except:
            self.htlcs = ""
        try:
            self.features = json.loads(str[22].replace(';',','))
        except:
            pass

        self.is_keysend = str[23]
        self.payment_addr = str[24]
        self.creation_date_str = str[25]
        self.settle_date_str = str[26]
        self.btc_value = str[27]
        self.btc_amt_paid_sat = str[28]        
        return self

    def fromJSON(tlvJSON):
        self = RE_TLV()
        self.raw = tlvJSON

        self.r_preimage = tlvJSON["rPreimage"]
        self.r_hash = tlvJSON["rHash"]
        self.value = tlvJSON["value"]
        try:
            self.settled = tlvJSON["settled"]
        except:
            self.settled = ""
        self.creation_date = tlvJSON["creationDate"]
        self.settle_date = tlvJSON["settleDate"]
        self.cltv_expiry = tlvJSON["cltvExpiry"]
        self.add_index = tlvJSON["addIndex"]
        self.settle_index = tlvJSON["settleIndex"]
        self.amt_paid = tlvJSON["amtPaid"]
        self.amt_paid_sat = tlvJSON["amtPaidSat"]
        self.amt_paid_msat = tlvJSON["amtPaidMsat"]
        self.state = tlvJSON["state"]
        self.htlcs = []
        self.value_msat = tlvJSON["valueMsat"]
        self.features = []
        self.is_keysend = tlvJSON["isKeysend"]
        self.payment_addr = tlvJSON["paymentAddr"]

        # Empty Fields
        self.memo = ""
        self.payment_request = ""
        self.description_hash = ""
        self.expiry = ""
        self.fallback_addr = ""
        self.route_hints = ""
        self.private = ""
        self.creation_date_str = ""
        self.settle_date_str = ""
        self.btc_value = ""
        self.btc_amt_paid_sat = "" 

        return self
        
        
        
        

        


