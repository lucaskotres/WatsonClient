import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
    username='48668bda-7cdc-4e2c-b98b-61d8498fd93b',
    password='QzdhAsFJLly6',
    version='2016-09-20')

# replace with your own workspace_id
workspace_id = '793ec723-0da4-478f-b8ac-aaa7c9d864ed'

response = dict(status=None)

response = conversation.message(workspace_id=workspace_id, message_input={
    'text': 'ola'})
print(json.dumps(response, indent=2))

response = conversation.message(workspace_id=workspace_id, message_input={
    'text': 'o e3 possui modo demo?'},
                                context=response['context'])
print(json.dumps(response, indent=2))



# When you send multiple requests for the same conversation, include the
# context object from the previous response.
# response = conversation.message(workspace_id=workspace_id, message_input={
# 'text': 'turn the wipers on'},
#                                context=response['context'])
# print(json.dumps(response, indent=2))