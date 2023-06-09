# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flow/access/access.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flow.entities import account_pb2 as flow_dot_entities_dot_account__pb2
from flow.entities import block_header_pb2 as flow_dot_entities_dot_block__header__pb2
from flow.entities import block_pb2 as flow_dot_entities_dot_block__pb2
from flow.entities import collection_pb2 as flow_dot_entities_dot_collection__pb2
from flow.entities import event_pb2 as flow_dot_entities_dot_event__pb2
from flow.entities import execution_result_pb2 as flow_dot_entities_dot_execution__result__pb2
from flow.entities import transaction_pb2 as flow_dot_entities_dot_transaction__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x66low/access/access.proto\x12\x0b\x66low.access\x1a\x1b\x66low/entities/account.proto\x1a flow/entities/block_header.proto\x1a\x19\x66low/entities/block.proto\x1a\x1e\x66low/entities/collection.proto\x1a\x19\x66low/entities/event.proto\x1a$flow/entities/execution_result.proto\x1a\x1f\x66low/entities/transaction.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\r\n\x0bPingRequest\"\x0e\n\x0cPingResponse\"0\n\x1bGetLatestBlockHeaderRequest\x12\x11\n\tis_sealed\x18\x01 \x01(\x08\"\'\n\x19GetBlockHeaderByIDRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"/\n\x1dGetBlockHeaderByHeightRequest\x12\x0e\n\x06height\x18\x01 \x01(\x04\"r\n\x13\x42lockHeaderResponse\x12)\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x1a.flow.entities.BlockHeader\x12\x30\n\x0c\x62lock_status\x18\x02 \x01(\x0e\x32\x1a.flow.entities.BlockStatus\"G\n\x15GetLatestBlockRequest\x12\x11\n\tis_sealed\x18\x01 \x01(\x08\x12\x1b\n\x13\x66ull_block_response\x18\x02 \x01(\x08\">\n\x13GetBlockByIDRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x1b\n\x13\x66ull_block_response\x18\x02 \x01(\x08\"F\n\x17GetBlockByHeightRequest\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\x1b\n\x13\x66ull_block_response\x18\x02 \x01(\x08\"f\n\rBlockResponse\x12#\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x14.flow.entities.Block\x12\x30\n\x0c\x62lock_status\x18\x02 \x01(\x0e\x32\x1a.flow.entities.BlockStatus\"&\n\x18GetCollectionByIDRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"C\n\x12\x43ollectionResponse\x12-\n\ncollection\x18\x01 \x01(\x0b\x32\x19.flow.entities.Collection\"I\n\x16SendTransactionRequest\x12/\n\x0btransaction\x18\x01 \x01(\x0b\x32\x1a.flow.entities.Transaction\"%\n\x17SendTransactionResponse\x12\n\n\x02id\x18\x01 \x01(\x0c\"#\n\x15GetTransactionRequest\x12\n\n\x02id\x18\x01 \x01(\x0c\"?\n\x1cGetTransactionByIndexRequest\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\x0c\x12\r\n\x05index\x18\x02 \x01(\r\"3\n\x1fGetTransactionsByBlockIDRequest\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\x0c\"a\n\x1aTransactionResultsResponse\x12\x43\n\x13transaction_results\x18\x01 \x03(\x0b\x32&.flow.access.TransactionResultResponse\"H\n\x14TransactionsResponse\x12\x30\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x1a.flow.entities.Transaction\"F\n\x13TransactionResponse\x12/\n\x0btransaction\x18\x01 \x01(\x0b\x32\x1a.flow.entities.Transaction\"\xf6\x01\n\x19TransactionResultResponse\x12\x30\n\x06status\x18\x01 \x01(\x0e\x32 .flow.entities.TransactionStatus\x12\x13\n\x0bstatus_code\x18\x02 \x01(\r\x12\x15\n\rerror_message\x18\x03 \x01(\t\x12$\n\x06\x65vents\x18\x04 \x03(\x0b\x32\x14.flow.entities.Event\x12\x10\n\x08\x62lock_id\x18\x05 \x01(\x0c\x12\x16\n\x0etransaction_id\x18\x06 \x01(\x0c\x12\x15\n\rcollection_id\x18\x07 \x01(\x0c\x12\x14\n\x0c\x62lock_height\x18\x08 \x01(\x04\"$\n\x11GetAccountRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\"=\n\x12GetAccountResponse\x12\'\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x16.flow.entities.Account\"1\n\x1eGetAccountAtLatestBlockRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\":\n\x0f\x41\x63\x63ountResponse\x12\'\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x16.flow.entities.Account\"G\n\x1eGetAccountAtBlockHeightRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0c\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x04\"F\n!ExecuteScriptAtLatestBlockRequest\x12\x0e\n\x06script\x18\x01 \x01(\x0c\x12\x11\n\targuments\x18\x02 \x03(\x0c\"T\n\x1d\x45xecuteScriptAtBlockIDRequest\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\x0c\x12\x0e\n\x06script\x18\x02 \x01(\x0c\x12\x11\n\targuments\x18\x03 \x03(\x0c\"\\\n!ExecuteScriptAtBlockHeightRequest\x12\x14\n\x0c\x62lock_height\x18\x01 \x01(\x04\x12\x0e\n\x06script\x18\x02 \x01(\x0c\x12\x11\n\targuments\x18\x03 \x03(\x0c\"&\n\x15\x45xecuteScriptResponse\x12\r\n\x05value\x18\x01 \x01(\x0c\"X\n\x1eGetEventsForHeightRangeRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x14\n\x0cstart_height\x18\x02 \x01(\x04\x12\x12\n\nend_height\x18\x03 \x01(\x04\">\n\x1bGetEventsForBlockIDsRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x11\n\tblock_ids\x18\x02 \x03(\x0c\"\xd3\x01\n\x0e\x45ventsResponse\x12\x33\n\x07results\x18\x01 \x03(\x0b\x32\".flow.access.EventsResponse.Result\x1a\x8b\x01\n\x06Result\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\x0c\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x04\x12$\n\x06\x65vents\x18\x03 \x03(\x0b\x32\x14.flow.entities.Event\x12\x33\n\x0f\x62lock_timestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x1d\n\x1bGetNetworkParametersRequest\"0\n\x1cGetNetworkParametersResponse\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\t\"\'\n%GetLatestProtocolStateSnapshotRequest\";\n\x1dProtocolStateSnapshotResponse\x12\x1a\n\x12serializedSnapshot\x18\x01 \x01(\x0c\"7\n#GetExecutionResultForBlockIDRequest\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\x0c\"]\n!ExecutionResultForBlockIDResponse\x12\x38\n\x10\x65xecution_result\x18\x01 \x01(\x0b\x32\x1e.flow.entities.ExecutionResult2\xd9\x13\n\tAccessAPI\x12;\n\x04Ping\x12\x18.flow.access.PingRequest\x1a\x19.flow.access.PingResponse\x12\x62\n\x14GetLatestBlockHeader\x12(.flow.access.GetLatestBlockHeaderRequest\x1a .flow.access.BlockHeaderResponse\x12^\n\x12GetBlockHeaderByID\x12&.flow.access.GetBlockHeaderByIDRequest\x1a .flow.access.BlockHeaderResponse\x12\x66\n\x16GetBlockHeaderByHeight\x12*.flow.access.GetBlockHeaderByHeightRequest\x1a .flow.access.BlockHeaderResponse\x12P\n\x0eGetLatestBlock\x12\".flow.access.GetLatestBlockRequest\x1a\x1a.flow.access.BlockResponse\x12L\n\x0cGetBlockByID\x12 .flow.access.GetBlockByIDRequest\x1a\x1a.flow.access.BlockResponse\x12T\n\x10GetBlockByHeight\x12$.flow.access.GetBlockByHeightRequest\x1a\x1a.flow.access.BlockResponse\x12[\n\x11GetCollectionByID\x12%.flow.access.GetCollectionByIDRequest\x1a\x1f.flow.access.CollectionResponse\x12\\\n\x0fSendTransaction\x12#.flow.access.SendTransactionRequest\x1a$.flow.access.SendTransactionResponse\x12V\n\x0eGetTransaction\x12\".flow.access.GetTransactionRequest\x1a .flow.access.TransactionResponse\x12\x62\n\x14GetTransactionResult\x12\".flow.access.GetTransactionRequest\x1a&.flow.access.TransactionResultResponse\x12p\n\x1bGetTransactionResultByIndex\x12).flow.access.GetTransactionByIndexRequest\x1a&.flow.access.TransactionResultResponse\x12w\n\x1eGetTransactionResultsByBlockID\x12,.flow.access.GetTransactionsByBlockIDRequest\x1a\'.flow.access.TransactionResultsResponse\x12k\n\x18GetTransactionsByBlockID\x12,.flow.access.GetTransactionsByBlockIDRequest\x1a!.flow.access.TransactionsResponse\x12M\n\nGetAccount\x12\x1e.flow.access.GetAccountRequest\x1a\x1f.flow.access.GetAccountResponse\x12\x64\n\x17GetAccountAtLatestBlock\x12+.flow.access.GetAccountAtLatestBlockRequest\x1a\x1c.flow.access.AccountResponse\x12\x64\n\x17GetAccountAtBlockHeight\x12+.flow.access.GetAccountAtBlockHeightRequest\x1a\x1c.flow.access.AccountResponse\x12p\n\x1a\x45xecuteScriptAtLatestBlock\x12..flow.access.ExecuteScriptAtLatestBlockRequest\x1a\".flow.access.ExecuteScriptResponse\x12h\n\x16\x45xecuteScriptAtBlockID\x12*.flow.access.ExecuteScriptAtBlockIDRequest\x1a\".flow.access.ExecuteScriptResponse\x12p\n\x1a\x45xecuteScriptAtBlockHeight\x12..flow.access.ExecuteScriptAtBlockHeightRequest\x1a\".flow.access.ExecuteScriptResponse\x12\x63\n\x17GetEventsForHeightRange\x12+.flow.access.GetEventsForHeightRangeRequest\x1a\x1b.flow.access.EventsResponse\x12]\n\x14GetEventsForBlockIDs\x12(.flow.access.GetEventsForBlockIDsRequest\x1a\x1b.flow.access.EventsResponse\x12k\n\x14GetNetworkParameters\x12(.flow.access.GetNetworkParametersRequest\x1a).flow.access.GetNetworkParametersResponse\x12\x80\x01\n\x1eGetLatestProtocolStateSnapshot\x12\x32.flow.access.GetLatestProtocolStateSnapshotRequest\x1a*.flow.access.ProtocolStateSnapshotResponse\x12\x80\x01\n\x1cGetExecutionResultForBlockID\x12\x30.flow.access.GetExecutionResultForBlockIDRequest\x1a..flow.access.ExecutionResultForBlockIDResponseBL\n\x1aorg.onflow.protobuf.accessZ.github.com/onflow/flow/protobuf/go/flow/accessb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flow.access.access_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032org.onflow.protobuf.accessZ.github.com/onflow/flow/protobuf/go/flow/access'
  _PINGREQUEST._serialized_start=294
  _PINGREQUEST._serialized_end=307
  _PINGRESPONSE._serialized_start=309
  _PINGRESPONSE._serialized_end=323
  _GETLATESTBLOCKHEADERREQUEST._serialized_start=325
  _GETLATESTBLOCKHEADERREQUEST._serialized_end=373
  _GETBLOCKHEADERBYIDREQUEST._serialized_start=375
  _GETBLOCKHEADERBYIDREQUEST._serialized_end=414
  _GETBLOCKHEADERBYHEIGHTREQUEST._serialized_start=416
  _GETBLOCKHEADERBYHEIGHTREQUEST._serialized_end=463
  _BLOCKHEADERRESPONSE._serialized_start=465
  _BLOCKHEADERRESPONSE._serialized_end=579
  _GETLATESTBLOCKREQUEST._serialized_start=581
  _GETLATESTBLOCKREQUEST._serialized_end=652
  _GETBLOCKBYIDREQUEST._serialized_start=654
  _GETBLOCKBYIDREQUEST._serialized_end=716
  _GETBLOCKBYHEIGHTREQUEST._serialized_start=718
  _GETBLOCKBYHEIGHTREQUEST._serialized_end=788
  _BLOCKRESPONSE._serialized_start=790
  _BLOCKRESPONSE._serialized_end=892
  _GETCOLLECTIONBYIDREQUEST._serialized_start=894
  _GETCOLLECTIONBYIDREQUEST._serialized_end=932
  _COLLECTIONRESPONSE._serialized_start=934
  _COLLECTIONRESPONSE._serialized_end=1001
  _SENDTRANSACTIONREQUEST._serialized_start=1003
  _SENDTRANSACTIONREQUEST._serialized_end=1076
  _SENDTRANSACTIONRESPONSE._serialized_start=1078
  _SENDTRANSACTIONRESPONSE._serialized_end=1115
  _GETTRANSACTIONREQUEST._serialized_start=1117
  _GETTRANSACTIONREQUEST._serialized_end=1152
  _GETTRANSACTIONBYINDEXREQUEST._serialized_start=1154
  _GETTRANSACTIONBYINDEXREQUEST._serialized_end=1217
  _GETTRANSACTIONSBYBLOCKIDREQUEST._serialized_start=1219
  _GETTRANSACTIONSBYBLOCKIDREQUEST._serialized_end=1270
  _TRANSACTIONRESULTSRESPONSE._serialized_start=1272
  _TRANSACTIONRESULTSRESPONSE._serialized_end=1369
  _TRANSACTIONSRESPONSE._serialized_start=1371
  _TRANSACTIONSRESPONSE._serialized_end=1443
  _TRANSACTIONRESPONSE._serialized_start=1445
  _TRANSACTIONRESPONSE._serialized_end=1515
  _TRANSACTIONRESULTRESPONSE._serialized_start=1518
  _TRANSACTIONRESULTRESPONSE._serialized_end=1764
  _GETACCOUNTREQUEST._serialized_start=1766
  _GETACCOUNTREQUEST._serialized_end=1802
  _GETACCOUNTRESPONSE._serialized_start=1804
  _GETACCOUNTRESPONSE._serialized_end=1865
  _GETACCOUNTATLATESTBLOCKREQUEST._serialized_start=1867
  _GETACCOUNTATLATESTBLOCKREQUEST._serialized_end=1916
  _ACCOUNTRESPONSE._serialized_start=1918
  _ACCOUNTRESPONSE._serialized_end=1976
  _GETACCOUNTATBLOCKHEIGHTREQUEST._serialized_start=1978
  _GETACCOUNTATBLOCKHEIGHTREQUEST._serialized_end=2049
  _EXECUTESCRIPTATLATESTBLOCKREQUEST._serialized_start=2051
  _EXECUTESCRIPTATLATESTBLOCKREQUEST._serialized_end=2121
  _EXECUTESCRIPTATBLOCKIDREQUEST._serialized_start=2123
  _EXECUTESCRIPTATBLOCKIDREQUEST._serialized_end=2207
  _EXECUTESCRIPTATBLOCKHEIGHTREQUEST._serialized_start=2209
  _EXECUTESCRIPTATBLOCKHEIGHTREQUEST._serialized_end=2301
  _EXECUTESCRIPTRESPONSE._serialized_start=2303
  _EXECUTESCRIPTRESPONSE._serialized_end=2341
  _GETEVENTSFORHEIGHTRANGEREQUEST._serialized_start=2343
  _GETEVENTSFORHEIGHTRANGEREQUEST._serialized_end=2431
  _GETEVENTSFORBLOCKIDSREQUEST._serialized_start=2433
  _GETEVENTSFORBLOCKIDSREQUEST._serialized_end=2495
  _EVENTSRESPONSE._serialized_start=2498
  _EVENTSRESPONSE._serialized_end=2709
  _EVENTSRESPONSE_RESULT._serialized_start=2570
  _EVENTSRESPONSE_RESULT._serialized_end=2709
  _GETNETWORKPARAMETERSREQUEST._serialized_start=2711
  _GETNETWORKPARAMETERSREQUEST._serialized_end=2740
  _GETNETWORKPARAMETERSRESPONSE._serialized_start=2742
  _GETNETWORKPARAMETERSRESPONSE._serialized_end=2790
  _GETLATESTPROTOCOLSTATESNAPSHOTREQUEST._serialized_start=2792
  _GETLATESTPROTOCOLSTATESNAPSHOTREQUEST._serialized_end=2831
  _PROTOCOLSTATESNAPSHOTRESPONSE._serialized_start=2833
  _PROTOCOLSTATESNAPSHOTRESPONSE._serialized_end=2892
  _GETEXECUTIONRESULTFORBLOCKIDREQUEST._serialized_start=2894
  _GETEXECUTIONRESULTFORBLOCKIDREQUEST._serialized_end=2949
  _EXECUTIONRESULTFORBLOCKIDRESPONSE._serialized_start=2951
  _EXECUTIONRESULTFORBLOCKIDRESPONSE._serialized_end=3044
  _ACCESSAPI._serialized_start=3047
  _ACCESSAPI._serialized_end=5568
# @@protoc_insertion_point(module_scope)
