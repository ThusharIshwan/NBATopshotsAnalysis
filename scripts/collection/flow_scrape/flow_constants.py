from scripts.collection.flow_scrape.unpacking_functions import *

MIN_BLOCK = 7601063
MAX_BLOCK = 48560404
MAX_DF_SIZE = 1000000
MAX_RANGE = 249
MAX_THREADS = 50


spork_channel = {    
    -2 : {"node" : "access-001.candidate7.nodes.onflow.org:9000", "start_height": 4132133,"end_height": 4972986},
    -1 : {"node" : "access-001.candidate8.nodes.onflow.org:9000", "start_height": 4972987,"end_height": 6483245},
    0 : {"node" : "access-001.candidate9.nodes.onflow.org:9000", "start_height": 6483246,"end_height": 7601062},
    1 : {"node" : "access-001.mainnet1.nodes.onflow.org:9000", "start_height": 7601063,"end_height":8742958 },
    2 : {"node" : "access-001.mainnet2.nodes.onflow.org:9000", "start_height": 8742959,"end_height":9737132 },
    3 : {"node" : "access-001.mainnet3.nodes.onflow.org:9000", "start_height": 9737133,"end_height":9992019 },
    4 : {"node" : "access-001.mainnet4.nodes.onflow.org:9000", "start_height": 9992020,"end_height":12020338 },
    5 : {"node" : "access-001.mainnet5.nodes.onflow.org:9000", "start_height": 12020337,"end_height":12609236 },
    6 : {"node" : "access-001.mainnet6.nodes.onflow.org:9000", "start_height": 12609237,"end_height":13404173 },
    7 : {"node" : "access-001.mainnet7.nodes.onflow.org:9000", "start_height": 13404174,"end_height":13950741 },
    8 : {"node" : "access-001.mainnet8.nodes.onflow.org:9000", "start_height": 13950742,"end_height":14892103 },
    9 : {"node" : "access-001.mainnet9.nodes.onflow.org:9000", "start_height": 14892104,"end_height":15791890 },
    10 : {"node" : "access-001.mainnet10.nodes.onflow.org:9000", "start_height": 15791891,"end_height":16755601 },
    11 : {"node" : "access-001.mainnet11.nodes.onflow.org:9000", "start_height": 16755602,"end_height":17544522 },
    12 : {"node" : "access-001.mainnet12.nodes.onflow.org:9000", "start_height": 17544523,"end_height":18587477 },
    13 : {"node" : "access-001.mainnet13.nodes.onflow.org:9000", "start_height": 18587478,"end_height":19050752 },
    14 : {"node" : "access-001.mainnet14.nodes.onflow.org:9000", "start_height": 19050753,"end_height":21291691 },
    15 : {"node" : "access-001.mainnet15.nodes.onflow.org:9000", "start_height": 21291692,"end_height":23830812 },
    16 : {"node" : "access-001.mainnet16.nodes.onflow.org:9000", "start_height": 23830813,"end_height":27341469 },
    17 : {"node" : "access-001.mainnet17.nodes.onflow.org:9000", "start_height": 27341470,"end_height":31735954 },
    18 : {"node" : "access-001.mainnet18.nodes.onflow.org:9000", "start_height": 31735955,"end_height":35858810 },
    19 : {"node" : "access-001.mainnet19.nodes.onflow.org:9000", "start_height": 35858811,"end_height":40171633 },
    20 : {"node" : "access-001.mainnet20.nodes.onflow.org:9000", "start_height": 40171634,"end_height":44950206 },
    21 : {"node" : "access-001.mainnet21.nodes.onflow.org:9000", "start_height": 44950207,"end_height":47169686 },
    22 : {"node" : "access.mainnet.nodes.onflow.org:9000", "start_height": 47169687,"end_height": 99999999},
}


event_contract = {
    1: {"Code": "A.c1e4f4f4c4257510.Market.MomentPurchased",
        "Nickname": "V1Purchases",
        "InfoList": ["blockDay", "blockMonth", "blockYear", "blockHeight","tokenID","Price","transactionID"],
        "UnpackFunction": unpack_purchases },
    2: {"Code": "A.c1e4f4f4c4257510.TopShotMarketV2.MomentPurchased",
        "Nickname": "V2Purchases",
        "InfoList": ["blockDay", "blockMonth", "blockYear","blockHeight","tokenID","Price","transactionID"],
        "UnpackFunction": unpack_purchases },
    3: {"Code": "A.c1e4f4f4c4257510.TopShotMarketV3.MomentPurchased",
        "Nickname": "V3Purchases",
        "InfoList": ["blockDay", "blockMonth", "blockYear","blockHeight","tokenID","Price","transactionID"],
        "UnpackFunction": unpack_purchases },
    4: {"Code": "A.b8ea91944fd51c43.OffersV2.OfferCompleted",
        "Nickname": "V2Offers",
        "InfoList": ["blockDay", "blockMonth", "blockYear","blockHeight","tokenID","Price","transactionID"],
        "UnpackFunction": unpack_offers },
    5: {"Code": "A.b8ea91944fd51c43.Offers.OfferCompleted",
        "Nickname": "V1Offers",
        "InfoList": ["blockDay", "blockMonth", "blockYear","blockHeight","tokenID","Price","transactionID"],
        "UnpackFunction": unpack_offers },
    6: {"Code": "A.0b2a3299cc857e29.TopShot.MomentMinted",
        "Nickname": "MomentMinted",
        "InfoList": ["blockDay", "blockMonth", "blockYear", "blockHeight", "momentID", "playID", "setID", "serial", "subeditionID", "transactionID"],
        "UnpackFunction": unpack_mints },
    7: {"Code": "A.0b2a3299cc857e29.TopShot.PlayCreated",
        "Nickname": "PlayCreated",
        "InfoList": ["blockDay", "blockMonth", "blockYear", "blockHeight", "playID", "playerName", "date", "playType", "birthday",
                     "birthplace", "draftyear","team","position","height","totalyearsexp","season","transactionID"],
        "UnpackFunction": unpack_play },
    8: {"Code": "A.0b2a3299cc857e29.TopShot.SubeditionAddedToMoment",
        "Nickname": "SubeditionAddedToMoment",
        "InfoList": ["blockDay", "blockMonth", "blockYear", "blockHeight", "momentID", "subID", "transactionID"],
        "UnpackFunction": unpack_sub_add },
    9: {"Code": "A.0b2a3299cc857e29.TopShot.MomentDestroyed",
        "Nickname": "MomentDestroyed",
        "InfoList": ["blockDay", "blockMonth", "blockYear", "blockHeight", "id", "transactionID"],
        "UnpackFunction": unpack_id },
}