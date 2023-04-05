import pandas as pd
import datetime
from os import listdir
from scripts.utils import make_file_safe


def get_total_aggregate_data(to_file=True, filename = "graphs/overview_total.csv"):
    total_volume = {}
    for f in listdir("transformed_data"):
        df = pd.read_csv(f"transformed_data/{f}")
        g = df.groupby(["blockYear","blockMonth","blockDay"]).agg({"Price":"sum", "Market" : "count"}).sort_index().reset_index()
        for x in g.iterrows():
            d = datetime.date(int(x[1]["blockYear"]), int(x[1]["blockMonth"]), int(x[1]["blockDay"]))
            if d not in total_volume.keys():
                total_volume[d]  = x[1]["Price"]
            else:
                total_volume[d] += x[1]["Price"]
    d = []
    m = []
    y = []
    p = []
    for k, v in total_volume.items():
        d.append(k.day)
        m.append(k.month)
        y.append(k.year)
        p.append(v)
    df = pd.DataFrame({"year":y,"month":m,"day":d,"value":p})
    if to_file:
        df.to_csv(filename)
    return total_volume


def get_player_aggregate_data(total_count, to_file=True, filename = f"graphs/player_overviews/file.csv"):
    p_count = {}
    for f in listdir("transformed_data"):
        df = pd.read_csv(f"transformed_data/{f}")
        g = df.groupby(["blockYear","blockMonth","blockDay", "playerName"]).agg({"Price":"sum", "Market" : "count"}).reset_index()
        for x in g.iterrows():
            d = (datetime.date(int(x[1]["blockYear"]), int(x[1]["blockMonth"]), int(x[1]["blockDay"])), x[1]["playerName"])
            if d not in p_count.keys():
                p_count[d]  = x[1]["Price"]
            else:
                p_count[d] += x[1]["Price"]
    d = []
    m = []
    y = []
    player = []
    price = []
    tp = []
    perc = []
    for k, v in p_count.items():
        d.append(k[0].day)
        m.append(k[0].month)
        y.append(k[0].year)
        player.append(k[1])
        price.append(v)
        tp.append(total_count[k[0]])
        perc.append(v/total_count[k[0]])
    df = pd.DataFrame({"year":y,"month":m,"day":d, "player" : player,"value":price, "total_value" : tp, "perc": perc})
    df.to_csv(filename, index = False)
    return df


def split_player_aggregate():
    df = pd.read_csv(f"graphs/player_overviews/file.csv")
    for p in set(df["player"]):
        f_name = make_file_safe(p)
        df_sub = df[df["player"] == p]
        df_sub.to_csv(f"graphs/player_overviews/{f_name}.csv", index=False)


def get_total_volume(days=30, max_day = datetime.date(2023,3,15),format_string = '%Y-%m-%d'):
    df=pd.read_csv(f"graphs/overview_total.csv")
    df["date"] = df["date"].apply(lambda x: datetime.datetime.strptime(x, format_string).date())
    total = df.loc[df["date"] >= max_day-datetime.timedelta(days), ["value"]].sum()["value"]
    return total


def get_player_volume(name, days=30, max_day = datetime.date(2023,3,15)):
    df = pd.read_csv(f"graphs/player_overviews/{make_file_safe(name)}.csv")
    df["date"] = df.apply(lambda x : datetime.date(x["year"],x["month"],x["day"]), axis=1 )
    p_total = df.loc[df["date"] >= max_day-datetime.timedelta(days), ["value"]].sum()["value"]
    return p_total


def get_player_volume_percent(days=30):
    play_data = pd.read_csv("data/play_data/Play_File_0.csv")
    perc_dict = {}
    tot = get_total_volume(days)
    for player in [x for x in set(play_data["playerName"]) if not pd.isna(x) and not x in ["Luka Doncic", "Stephen Curry"]]:
        p_tot = get_player_volume(player,days=days)
        p_perc = p_tot/tot
        perc_dict[player] = {"perc" : p_perc}
    return pd.DataFrame.from_dict(perc_dict,orient="index").sort_values("perc").reset_index().rename(columns={"index":"player"})