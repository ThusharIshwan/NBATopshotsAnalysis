from scripts.collection.flow_scrape.server_connection import *
from scripts.collection.flow_scrape.flow_constants import spork_channel

def spork_test(event = 3):
    failing_sporks = []
    for k,v in spork_channel.items():
        print(f"Testing spork: {k}")
        stub = create_spork_stub(k)
        request = create_event_request(event,v["start_height"],v["start_height"]+200)
        try:
            response = stub.GetEventsForHeightRange(request)
        except:
            failing_sporks.append(k)
            print(f"spork {k} failed :(")
    return failing_sporks

def single_spork_test(spork = 22, min_block = 0, max_block = 0, event = 1):
    if min_block==0:
        min_block = spork_channel[spork]["start_height"]
        max_block = min_block + 249
    stub = create_spork_stub(spork)
    request = create_event_request(event, min_block, max_block)
    response = stub.GetEventsForHeightRange(request)
    return response


#json.loads(single_spork_test(spork =1, min_block=7643233,max_block=7643233+1,event=7).results[0].events[0].payload)["value"]["fields"]