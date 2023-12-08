from google.cloud import translate_v2 as translate
from conf import conf
import html


def translate_text(text):
    key_path = conf['translate_credentials']

    client = translate.Client.from_service_account_json(key_path)

    result = client.translate(
        text,
        target_language='he'
    )

    return html.unescape(result['translatedText'])


if __name__ == '__main__':
    arab_text = """
    اللواء المحلل العسكري فايز دويري:
قوات الاحتلال حتى لحظه تسيطير فقط على مناطق زراعيه لا اكثر،،
    """
    print(translate_text(arab_text))
