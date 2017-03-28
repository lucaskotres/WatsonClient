from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
    username='48668bda-7cdc-4e2c-b98b-61d8498fd93b',
    password='QzdhAsFJLly6',
    version='2017-03-28')

# replace with your own workspace_id
workspace_id = '97f9058e-9f52-4d7c-8bba-bb45d485c071'



@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' iniciou o chat'}, room=room)
    response = conversation.message(workspace_id=workspace_id, message_input={
        'text': 'Ola'})


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)

    response = conversation.message(workspace_id=workspace_id, message_input={
        'text': message['msg']}, context=response['context'])

    print(json.dumps(response, indent=2))
    emit('message', {'msg': 'SuporteBot' + ':' + json.dumps(response, indent=2)}, room=room)
    #emit('message',{'msg': 'SuporteBot' + ':' + json.dumps(response['text'])},room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

