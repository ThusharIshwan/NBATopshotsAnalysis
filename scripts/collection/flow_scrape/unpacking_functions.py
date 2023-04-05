import datetime
import json
from scripts.utils import to_hex

def unpack_purchases(block_result):
    day_list = []
    month_list = []
    year_list = []
    bh_list = []
    id_list = []
    pr_list = []
    tx_list = []
    day = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).day
    month = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).month
    year = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).year
    bh = block_result.block_height
    for e in block_result.events:
        id = ""
        pr = ""
        payload_fields = json.loads(e.payload)["value"]["fields"]
        for p in payload_fields:
            if p["name"] == "id":
                id = p["value"]["value"]
            elif p["name"] == "price":
                pr = p["value"]["value"]
        day_list.append(day)
        month_list.append(month)
        year_list.append(year)
        bh_list.append(bh)
        id_list.append(id)
        pr_list.append(pr)
        tx_list.append(to_hex(e.transaction_id))
    return [day_list, month_list, year_list, bh_list, id_list, pr_list, tx_list]


def unpack_offers(block_result):
    day_list = []
    month_list = []
    year_list = []
    bh_list = []
    id_list = []
    pr_list = []
    tx_list = []
    day = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).day
    month = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).month
    year = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).year
    bh = block_result.block_height
    for e in block_result.events:
        id = ""
        pr = ""
        payload_fields = json.loads(e.payload)["value"]["fields"]
        bought = False
        for p in payload_fields:
            if p["name"] == "purchased":
                if p["value"]["value"]:
                    bought = True
                else:
                    break
            if p["name"] == "nftId":
                id = p["value"]["value"]["value"]
            elif p["name"] == "offerAmount":
                pr = p["value"]["value"]
        if bought:
            day_list.append(day)
            month_list.append(month)
            year_list.append(year)
            bh_list.append(bh)
            id_list.append(id)
            pr_list.append(pr)
            tx_list.append(to_hex(e.transaction_id))
        bought = False
    return [day_list, month_list, year_list, bh_list, id_list, pr_list, tx_list]


def unpack_mints(block_result):
    #"blockTimestamp": [], "blockHeight": [], "momentID": [], "playID": [], "setID": [], "serial": [], "subeditionID": []
    day_list = []
    month_list = []
    year_list = []
    bh_list = []
    mo_list = []
    pid_list = []
    set_list = []
    ser_list = []
    sub_list = []
    tx_list = []
    day = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).day
    month = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).month
    year = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).year
    bh = block_result.block_height
    for e in block_result.events:
        mo = ""
        pid = ""
        set = ""
        ser = ""
        sub = ""
        payload_fields = json.loads(e.payload)["value"]["fields"]
        for p in payload_fields:
            if p["name"] == "momentID":
                mo = p["value"]["value"]
            elif p["name"] == "playID":
                pid = p["value"]["value"]
            elif p["name"] == "setID":
                set = p["value"]["value"]
            elif p["name"] == "serialNumber":
                ser = p["value"]["value"]
            elif p["name"] == "subeditionID":
                sub = p["value"]["value"]
        day_list.append(day)
        month_list.append(month)
        year_list.append(year)
        bh_list.append(bh)
        mo_list.append(mo)
        pid_list.append(pid)
        set_list.append(set)
        ser_list.append(ser)
        sub_list.append(sub)
        tx_list.append(to_hex(e.transaction_id))
    return [day_list, month_list, year_list, bh_list, mo_list, pid_list, set_list, ser_list, sub_list, tx_list]


def unpack_general(block_result):
    day_list = []
    month_list = []
    year_list = []
    bh_list = []
    tx_list = []
    day = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).day
    month = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).month
    year = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).year
    bh = block_result.block_height
    for e in block_result.events:
        day_list.append(day)
        month_list.append(month)
        year_list.append(year)
        bh_list.append(bh)
        tx_list.append(to_hex(e.transaction_id))
    return [day_list, month_list, year_list, bh_list, tx_list]


def unpack_sub_add(block_result):
    day_list = []
    month_list = []
    year_list = []
    bh_list = []
    mo_list = []
    sid_list = []
    tx_list = []
    day = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).day
    month = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).month
    year = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).year
    bh = block_result.block_height
    for e in block_result.events:
        mo = ""
        sid = ""
        payload_fields = json.loads(e.payload)["value"]["fields"]
        for p in payload_fields:
            if p["name"] == "momentID":
                mo = p["value"]["value"]
            elif p["name"] == "subeditionID":
                sid = p["value"]["value"]
        day_list.append(day)
        month_list.append(month)
        year_list.append(year)
        bh_list.append(bh)
        mo_list.append(mo)
        sid_list.append(sid)
        tx_list.append(to_hex(e.transaction_id))
    return [day_list, month_list, year_list, bh_list, mo_list, sid_list, tx_list]


def unpack_id(block_result):
    day_list = []
    month_list = []
    year_list = []
    bh_list = []
    id_list = []
    tx_list = []
    day = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).day
    month = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).month
    year = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).year
    bh = block_result.block_height
    for e in block_result.events:
        mo = ""
        payload_fields = json.loads(e.payload)["value"]["fields"]
        for p in payload_fields:
            if p["name"] == "id":
                mo = p["value"]["value"]
        day_list.append(day)
        month_list.append(month)
        year_list.append(year)
        bh_list.append(bh)
        id_list.append(mo)
        tx_list.append(to_hex(e.transaction_id))
    return [day_list, month_list, year_list, bh_list, id_list, tx_list]

def unpack_play(block_result):
    day_list = []
    month_list = []
    year_list = []
    bh_list = []
    id_list = []
    pn_list = []
    dt_list = []
    pt_list = []
    tx_list = []
    bd_list = []
    bp_list = []
    dy_list = []
    tam_list = []
    pp_list = []
    h_list = []
    tye_list = []
    sea_list = []



    day = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).day
    month = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).month
    year = datetime.date.fromtimestamp(block_result.block_timestamp.seconds).year
    bh = block_result.block_height
    for e in block_result.events:
        id = ""
        player_name = ""
        date = ""
        play_type = ""
        birthday = ""
        birthplace = ""
        draftyear = ""
        team = ""
        position = ""
        height = ""
        yearsexp = ""
        season = ""
        #
        payload_fields = json.loads(e.payload)["value"]["fields"]
        for p in payload_fields:
            if p["name"] == "id":
                id = p["value"]["value"]
            elif p["name"] == "metadata":
                data = p["value"]["value"]
                for d in data:
                    if d["key"]["value"] == "FullName":
                        player_name = d["value"]["value"]
                    elif d["key"]["value"] == "DateOfMoment":
                        date = d["value"]["value"]
                    elif d["key"]["value"] == "PlayType":
                        play_type = d["value"]["value"]
                    elif d["key"]["value"] == "Birthdate":
                        birthday = d["value"]["value"]
                    elif d["key"]["value"] == "Birthplace":
                        birthplace = d["value"]["value"]
                    elif d["key"]["value"] == "DraftYear":
                        draftyear = d["value"]["value"]
                    elif d["key"]["value"] == "TeamAtMoment":
                        team = d["value"]["value"]
                    elif d["key"]["value"] == "PlayerPosition":
                        position = d["value"]["value"]
                    elif d["key"]["value"] == "Height":
                        height = d["value"]["value"]
                    elif d["key"]["value"] == "TotalYearsExperience":
                        yearsexp = d["value"]["value"]
                    elif d["key"]["value"] == "NbaSeason":
                        season = d["value"]["value"]        
        day_list.append(day)
        month_list.append(month)
        year_list.append(year)
        bh_list.append(bh)
        id_list.append(id)
        pn_list.append(player_name)
        dt_list.append(date)
        pt_list.append(play_type)
        bd_list.append(birthday)
        bp_list.append(birthplace)
        dy_list.append(draftyear)
        tam_list.append(team)
        pp_list.append(position)
        h_list.append(height)
        tye_list.append(yearsexp)
        sea_list.append(season)
        tx_list.append(to_hex(e.transaction_id))
    return [day_list, month_list, year_list, bh_list, id_list, pn_list, dt_list, pt_list, 
            bd_list, bp_list, dy_list, tam_list, pp_list, h_list, tye_list, sea_list, tx_list]