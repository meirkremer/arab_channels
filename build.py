import os
import subprocess


def create_venv():
    subprocess.run('python3 -m venv venv', shell=True, cwd=os.getcwd())
    subprocess.run('venv/bin/pip install -r requirements.txt', shell=True, cwd=os.getcwd())


def create_cred_and_conf():
    subprocess.run('mkdir credentials', shell=True, cwd=os.getcwd())
    with open('conf.py', 'w') as f:
        f.write(
            """
import os
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


def read_key_from_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def get_key_auth():
    auth_path = 'credentials/auth_key.txt'
    if os.path.exists(auth_path):
        return read_key_from_file(auth_path)

    with TelegramClient(StringSession(), replace_with_your_api_id, 'replace_with_your_api_hash') as client:
        key_auth = client.session.save()

    with open(auth_path, 'w') as key:
        key.write(key_auth)

    return key_auth


conf = {
    'api_id': replace_with_your_api_id,
    'api_hash': 'replace_with_your_api_hash',
    'key_auth': StringSession(get_key_auth()),
    'translate_credentials': 'credentials/your_creds_file.json',
    'translate_channel': 'replace_with_your_channel_user_name'
}

            """
        )
