# -*- coding: utf-8 -*-
from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
import json
from watson_developer_cloud import ConversationV1

import logging
logging.basicConfig(filename='elipsewatsonchat.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                            datefmt='%d/%m/%y %H:%M:%S',
                            level=logging.DEBUG)


logging.getLogger().addHandler(logging.StreamHandler())


conversation = ConversationV1(
    username='48668bda-7cdc-4e2c-b98b-61d8498fd93b',
    password='QzdhAsFJLly6',
    version='2017-03-28')

# replace with your own workspace_id
workspace_id = '97f9058e-9f52-4d7c-8bba-bb45d485c071'

response = dict(status=None)

@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' iniciou o chat'}, room=room)
    response = conversation.message(workspace_id=workspace_id)
    logging.debug(json.dumps(response, indent=2, ensure_ascii=False, encoding="utf-8"))
    emit('message', {'msg': 'SuporteBot' + ':' + json.dumps(response['output']['text'], indent=2, ensure_ascii=False)}, room=room)

@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)

    global response
    try:
        response = conversation.message(workspace_id=workspace_id, message_input={
        'text': message['msg']}, context=response['context'])
        logging.debug(json.dumps(response, indent=2,ensure_ascii=False, encoding="utf-8"))


    except:
        response = conversation.message(workspace_id=workspace_id, message_input={
        'text': message['msg']})
        logging.debug(json.dumps(response, indent=2,ensure_ascii=False, encoding="utf-8"))

    #emit('message', {'msg': 'Intenção' + ':' + json.dumps(response['intents'], indent=2)}, room=room)
    emit('message', {'msg': 'SuporteBot' + ':' + json.dumps(response['output']['text'], indent=2, ensure_ascii=False)}, room=room)
    #emit('message', {'msg': 'ErrorLog' + ':' + json.dumps(response['output']['log_messages'], indent=2)}, room=room)

@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)