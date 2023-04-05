import grpc
import flow.access.access_pb2 as pb
import flow.access.access_pb2_grpc as gpb
from scripts.collection.flow_scrape.flow_constants import spork_channel, event_contract

def create_spork_stub(n):
    channel = grpc.insecure_channel(spork_channel[n]["node"])
    return gpb.AccessAPIStub(channel)


def create_event_request(n, sb, eb):
    return pb.GetEventsForHeightRangeRequest(type = event_contract[n]["Code"], start_height = sb, end_height = eb)