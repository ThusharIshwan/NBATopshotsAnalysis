import pandas as pd
from os import listdir, path, remove
import datetime
from scripts.utils import consolodate_data

# Loading the play data
play_df = pd.read_csv("data/play_data/Play_File_0.csv")
play_info = play_df[["playID", "playerName", "playType", "date"]].copy(deep=True)
play_info.rename(columns={"date":"playDate"}, inplace=True)

# Loading the player popularity indicators
player_pop_data = pd.read_csv("data\player_indeps.csv")
players_with_PIE = list(player_pop_data["player"])

### Getting the supplies from the moment data
play_df = pd.read_csv("data/play_data/Play_File_0.csv")
play_info = play_df[["playID", "playerName", "playType", "date"]].copy(deep=True)
play_info.rename(columns={"date":"playDate"}, inplace=True)


play_counts = {}
edition_counts = {}
type_counts = {}
player_counts = {}
for x in listdir("data/moment_data"):

    df = pd.merge(pd.read_csv(f"data/moment_data/{x}"), play_info, on= "playID",how="left")
    df["subeditionID"] = df["subeditionID"].fillna(0)
    play_count_curr = df.groupby("playID").agg({"momentID": "count"}).reset_index()
    edition_counts_curr = df.groupby(["playID", "subeditionID"]).agg({"momentID": "count"}).reset_index()
    type_count_curr = df.groupby("playType").agg({"momentID": "count"}).reset_index()
    player_count_curr = df.groupby("playerName").agg({"momentID": "count"}).reset_index()

    for r in play_count_curr.iterrows():
        if r[1]["playID"] in play_counts.keys():
            play_counts[r[1]["playID"]] += r[1]["momentID"]
        else:
            play_counts[r[1]["playID"]]  = r[1]["momentID"]
    
    for r in edition_counts_curr.iterrows():
        if (r[1]["playID"], r[1]["subeditionID"]) in edition_counts.keys():
            edition_counts[(r[1]["playID"], r[1]["subeditionID"])] += r[1]["momentID"]
        else:
            edition_counts[(r[1]["playID"], r[1]["subeditionID"])]  = r[1]["momentID"]
    
    for r in type_count_curr.iterrows():
        if r[1]["playType"] in type_counts.keys():
            type_counts[r[1]["playType"]] += r[1]["momentID"]
        else:
            type_counts[r[1]["playType"]]  = r[1]["momentID"]
    
    for r in player_count_curr.iterrows():
        if r[1]["playerName"] in player_counts.keys():
            player_counts[r[1]["playerName"]] += r[1]["momentID"]
        else:
            player_counts[r[1]["playerName"]]  = r[1]["momentID"]

    
supplies_frame = pd.DataFrame(index = pd.MultiIndex.from_tuples(edition_counts.keys(), names=["playID","editionID"])).reset_index()
supplies_frame["editionSupply"] = supplies_frame.apply(lambda x: edition_counts[(x["playID"], x["editionID"])],axis=1)
supplies_frame["playSupply"] = supplies_frame["playID"].apply(lambda x: play_counts[x])



### Transforming the transaction data
min_date = datetime.date(2022,12,1)
max_date = datetime.date(2022,12,1)
play_edition_pair_list = []
tot_max=0
for x in listdir("data/transaction_data"):
    mf = int(f"{x[17:-7]}")
    print(mf)
    o = int(f"{x[-5:-4]}")
    txn_df = pd.read_csv(f"data/transaction_data/{x}")

    moment_df = pd.read_csv(f"data/moment_data/Moment_File_{mf}.csv")
    moment_info = moment_df[["momentID","playID", "subeditionID"]]

    re_df = pd.merge(txn_df, moment_info, left_on="tokenID", right_on="momentID", how="left").drop("tokenID", axis=1)
    re_df["subeditionID"] = re_df["subeditionID"].fillna(0)

    re_df2 = re_df.groupby(["playID", "subeditionID", "blockDay", "blockMonth", "blockYear"]).agg({"Price":["sum", "count"]}).reset_index()
    re_df2.columns=["playID","editionID", "day", "month", "year", "price_sum", "price_count"]


    re_df2 = pd.merge(re_df2, play_info,on="playID")
    re_df2["playDate"] = re_df2["playDate"].apply(lambda x: datetime.datetime.strptime(x[0:x.find(" ")], "%Y-%m-%d").date())
    re_df2["date"] = re_df2.apply(lambda x: datetime.date(x["year"], x["month"], x["day"]),axis=1)
    re_df2.drop(["day", "month", "year"],axis=1,inplace=True)
    re_df2 = pd.merge(re_df2, supplies_frame, on= ["playID","editionID"])
    re_df2["typeSupply"] = re_df2["playType"].apply(lambda x: type_counts[x])
    re_df_fin = re_df2[re_df2["playerName"].isin(players_with_PIE)].copy(deep=True)
    re_df_fin["playerSupply"] = re_df_fin["playerName"].apply(lambda x: player_counts[x])

    
    re_df_fin["playID"] = re_df_fin["playID"].apply(int)
    re_df_fin["editionID"] = re_df_fin["editionID"].apply(int)

    print(re_df_fin[re_df_fin["editionID"] != 0])
    if min(re_df_fin["date"]) < min_date:
        min_date = min(re_df_fin["date"])
    if max(re_df_fin["date"]) > max_date:
        max_date = max(re_df_fin["date"])

    play_edition_pair = list(set(list(zip(re_df_fin["playID"], re_df_fin["editionID"]))))
    for p,e in play_edition_pair:
        re_df_fin[(re_df_fin["playID"]==p) & (re_df_fin["editionID"]==e)].to_csv(f"data/txn_data/unconsolodated/txn_data_{p}_{e}_{mf}_{o}.csv", index=False)

    play_edition_pair_list.extend(play_edition_pair)
    play_edition_pair_list = list(set(play_edition_pair_list))
    tot_max += len(re_df_fin)

for k,v in play_edition_pair_list:
    consolodate_data(f"txn_data_{k}_{v}_", in_folder="data/txn_data/unconsolodated", out_folder="data/txn_data/play_consolodated")


date_range = [min_date + datetime.timedelta(days=x) for x in range((max_date-min_date).days + 1)]
for f in listdir("data/txn_data/play_consolodated"):
    t_df = pd.read_csv(f"data/txn_data/play_consolodated/{f}")
    t_df_re = t_df.groupby(["date", "editionID"]).agg({"price_sum":"sum", "price_count":"sum"}).reset_index().sort_values(["editionID","date"])
    t_df_re["date"] = t_df_re["date"].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").date())
    t_df_re["price"] = t_df_re["price_sum"]/t_df_re["price_count"]
    t_df_re.drop(["price_sum","price_count"],axis=1,inplace=True)

    t_df_re = pd.merge(pd.DataFrame({"date":date_range}), t_df_re, how="outer")
    #t_df_re.fillna(method="ffill",inplace=True)

    for c in [x for x in list(t_df.columns) if not x in ['price_sum', 'price_count', "date", "editionID"]]:
        t_df_re[c] = t_df[c][0]
    
    t_df_re = pd.merge(t_df_re.rename(columns={"playerName":"player"}),player_pop_data,on="player" )
    t_df_re.to_csv(f"data/txn_data/play_consolodated/{f}", index=False)










































