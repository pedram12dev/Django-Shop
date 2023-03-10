from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('6F5157596563467330746E6348667966474739793841655677746434435A34596A514744446234647A46773D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'{code}کد تایید شما'
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
