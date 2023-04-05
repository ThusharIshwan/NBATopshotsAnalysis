import time
import math
import pandas as pd
from scripts.utils import distribute_elements, consolodate_data
from scripts.classes.threadwithreturn import ThreadWithReturn
from scripts.collection.flow_scrape.flow_constants import *
from scripts.collection.flow_scrape.server_connection import *

def procedure(start_block = MIN_BLOCK, end_block = MAX_BLOCK, max_df_size = MAX_DF_SIZE, output_message = "output", 
              event_num = 3, block_range = MAX_RANGE, threaded = True, max_tries=3):
    curr = start_block
    event_nickname = event_contract[event_num]["Nickname"]
    unpack_function = event_contract[event_num]["UnpackFunction"]
    frame_data_item_list = event_contract[event_num]["InfoList"]
    frame_data = {x:[] for x in frame_data_item_list}
    output_number = 1
    update_time = time.time()
    UPDATE_FREQ = 120
    missing_values = []
    spork = 0
    stub = create_spork_stub(spork)
    while (curr < end_block):
        if time.time() - update_time > UPDATE_FREQ:
            print(f"Update: {output_message} :  {round((curr-start_block)*100/(end_block-start_block), 2)}% complete")
            update_time = time.time()
        if len(frame_data[frame_data_item_list[0]]) > max_df_size:
            pd.DataFrame(frame_data).to_csv(f"output/{output_message}_{event_nickname}_{output_number}.csv", index = False)
            output_number+=1
            frame_data = {x:[] for x in frame_data_item_list}
        while (curr > spork_channel[spork]["end_height"]):
            spork+=1
            stub = create_spork_stub(spork)
            curr = max(spork_channel[spork]["start_height"],start_block)
        request = create_event_request(event_num, curr, curr+block_range)
        response = ""
        succ = False
        tries = 0
        while not succ and not tries >= max_tries:
            tries += 1
            try:
                response = stub.GetEventsForHeightRange(request)
                succ = True
            except:
                time.sleep(1)
                pass
            if tries == max_tries:
                print(f"COMPLETELY FAILED TO GET EVENTS: Current Spork {spork}, Current Block: {curr}, End Block: {curr+block_range}, Current Event: {event_num}")
                missing_values.append({"Spork": spork, "StartBlock": curr, "EndBlock": curr+block_range, "EventNumber": event_num})
        if not response == "":
            for x in response.results:
                p = unpack_function(x)
                if len(p[0]) > 0:
                    for i in range(len(frame_data_item_list)):
                        frame_data[frame_data_item_list[i]].extend(p[i])
        curr+=(block_range+1)
        if threaded:
            time.sleep(1)
    pd.DataFrame(frame_data).to_csv(f"output/{output_message}_{event_nickname}_{output_number}.csv", index = False)
    frame_data = {x:[] for x in frame_data_item_list}
    return missing_values


def single_spork_thread_dict(spork=22, event_num=3, min_block = MIN_BLOCK, max_block=MAX_BLOCK, thread_num = MAX_THREADS, max_range = MAX_RANGE, max_tries=3):
    start_block = max(spork_channel[spork]["start_height"], min_block)
    end_block = min(spork_channel[spork]["end_height"]+2, max_block+1)
    if end_block < start_block:
        return {}
    n_threads = thread_num
    thread_start_stop_numbers = [start_block + math.ceil(i*((end_block - start_block)/n_threads+1))  for i in range(0,n_threads+1)]
    thread_start_stops = {i:(thread_start_stop_numbers[i], thread_start_stop_numbers[i+1]-1) for i in range(0,n_threads)}
    thread_dict = {}
    for k, v in thread_start_stops.items() :
        thread_dict[k]= ThreadWithReturn(target=procedure, args=(v[0], v[1], MAX_DF_SIZE, f"output_spork{spork}_thread_{k}",event_num, max_range, max_tries))
    return thread_dict


def threaded_procedure(spork_list = range(-2,23), event_num=3, min_block = MIN_BLOCK, max_block = MAX_BLOCK, thread_num = MAX_THREADS, block_range=MAX_RANGE, max_tries=3, 
                       missing_thread_vals = [80,40,20,10,5,2,1]):
    start_time = time.time()
    missing_values = []
    thread_dict = {}
    for k in spork_list:
        thread_dict[k] = single_spork_thread_dict(k,event_num,min_block,max_block,thread_num,block_range,max_tries)
    for k, v in thread_dict.items():
        for k2, v2 in v.items():
            print(f"Starting thread {k2} for Spork {k}")
            v2.start()
    for k, v in thread_dict.items():
        for k2, v2 in v.items():
            missing_values.extend(v2.join())
            print(f"Finished thread {k2} for Spork {k}")
    missing_id = 1
    for m in missing_values:
        m["missingID"] = missing_id
        missing_id += 1
    missing_fin = threaded_missing_procedure(missing_values, event_num,block_range=block_range, thread_nums_list=missing_thread_vals)
    print(time.time() - start_time)
    nickname = event_contract[event_num]["Nickname"]
    consolodate_data(f"_{nickname}_")
    return missing_fin


def missing_procedure(missing_values,event, threads=1, block_range = MAX_RANGE):
    missing_fin = []
    for m in missing_values:
        missing_id = m["missingID"]
        missing_fin.extend(procedure(start_block = m["StartBlock"], end_block=m["EndBlock"], 
                                     output_message=f"missing_{threads}_{missing_id}",event_num=event,block_range=block_range))
    return missing_fin


def threaded_missing_procedure(missing_values, event, thread_nums_list = [80,40,20,10,5,2,1], block_range = MAX_RANGE):
    missing_fin = missing_values
    missing_temp = []
    i_curr = 0
    while i_curr <= len(thread_nums_list)-1 and len(missing_fin) > 0:
        m_list = distribute_elements(missing_fin, thread_nums_list[i_curr])
        thread_dict = {}
        for i in range(thread_nums_list[i_curr]):
            thread_dict[i] = ThreadWithReturn(target=missing_procedure, args=(m_list[i], event, thread_nums_list[i_curr], block_range))
        for k,v in thread_dict.items():
            print(f"Missing Values, Threads: {k+1}/{thread_nums_list[i_curr]}, Start")
            v.start()
        for k,v in thread_dict.items():
            print(f"Missing Values, Threads: {k+1}/{thread_nums_list[i_curr]}, Join")
            missing_temp.extend(v.join())
        missing_fin = missing_temp
        missing_temp = []
        missing_id = 1
        for m in missing_fin:
            m["missingID"] = missing_id
            missing_id += 1
        i_curr+=1
    return missing_fin


def all_threaded_procedure():
    for i in event_contract.keys():
        threaded_procedure(event_num=i)



m = threaded_procedure(event_num=7, min_block=7601063, thread_num=5)