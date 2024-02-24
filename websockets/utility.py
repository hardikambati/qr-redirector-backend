from django.core.signing import Signer
from django.contrib.auth import get_user_model
from django.conf import settings

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# custom
from . import utility


User = get_user_model()
signer = Signer(settings.SECRET_KEY)


def encrypt_channel_id(channel_id: str) -> str:
    """
    encrypt text using django secret key
    """
    value = signer.sign(channel_id)
    print(f'[ENCODED] {value}')
    return value


def decrypt_channel_id(channel_id: str) -> str:
    """
    decrypt text using django secret key
    """
    value = signer.unsign(channel_id)
    print(f'[DECODED] {value}')
    return value


def encrpyted_channel_id(channel_name: str) -> str:
    """
    channel id is in format 'specific.xyz'
    this function extracts the xyz part and encrypts it
    """
    specific, channel_id = channel_name.split('.')
    value = encrypt_channel_id(channel_id)
    return value


def send_message_to_channel(token: str, message: dict) -> bool:
    """
    sends message to consumer websocket channel
    """
    channel_layer = get_channel_layer()
    decrypted_channel_id = utility.decrypt_channel_id(channel_id=token)

    try:
        async_to_sync(channel_layer.send)(
            f'specific.{decrypted_channel_id}',
            {
                'type': 'redirect_event',
                'message': message
            }
        )
        return True
    except Exception as e:
        print(f'[INFO] error in sending message')
        print(f'[INFO] {e}')
        return False
    