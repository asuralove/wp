

from google.cloud import translate_v2
translate_client = translate_v2.Client()

# export GOOGLE_APPLICATION_CREDENTIALS="/Users/mtdp/Downloads/tough-bearing-263013-dca7f13b193a.json"

def translate(text):
    # Translates some text into Russian
    translation = translate_client.translate(text, target_language='en')
        
    result = translation['translatedText']
    # 标题，描述，内容以5个#分割
    res = result.split('#####')
    print(res)
    return res


translate('很好')