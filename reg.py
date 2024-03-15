import requests

url = 'https://b-graph.facebook.com/app/validate_registration_data'

headers = {
    'Host': 'b-graph.facebook.com',
    'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
    'X-Fb-Friendly-Name': 'validateRegistrationData',
    'Zero-Rated': '0',
    'X-Fb-Net-Hni': '31002',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G988N Build/NRD90M) [FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/en_US;FBBV/480086274;FBCR/Android;FBMF/samsung;FBBD/samsung;FBDV/SM-G988N;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=1280,height=720};FB_FW/1;FBRV/0;]',
    'X-Fb-Connection-Quality': 'EXCELLENT',
    'Content-Encoding': 'gzip',
    'X-Fb-Connection-Bandwidth': '36025863',
    'X-Fb-Sim-Hni': '31002',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Fb-Connection-Type': 'WIFI',
    'X-Fb-Device-Group': '2924',
    'X-Tigon-Is-Retry': 'False',
    'Priority': 'u=3,i',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-Fb-Http-Engine': 'Liger',
    'X-Fb-Client-Ip': 'True',
    'X-Fb-Server-Cluster': 'True',
}

data = {
    'firstname': 'Sapkota',
    'lastname': 'Hack',
    'allow_local_pw': 'false',
    'session_id': '',
    'consent_standards_test_group': '',
    'play_service_version': '-1',
    'start_completed_timestamp': '1710509198154',
    'start_timestamp': '1710509194778',
    'tos_acquired_timestamp': '1710509241816',
    'name_acquired_timestamp': '1710509206522',
    'birthday_acquired_timestamp': '1710509215989',
    'cp_acquired_timestamp': '1710509228172',
    'pw_acquired_timestamp': '1710509239336',
    'gender_acquired_timestamp': '1710509222168',
    'device_has_previous_login': 'true',
    'is_background': 'false',
    'reg_instance': '63d47606-d9a2-4528-b499-e6b6db13ac7d',
    'format': 'json',
    'attempt_name_fixes': 'false',
    'suggest_names': 'false',
    'ignore_cp_claimed_errors': 'false',
    'locale': 'en_US',
    'client_country_code': 'NP',
    'fb_api_req_friendly_name': 'validateRegistrationData',
    'fb_api_caller_class': 'RegistrationValidateDataFragment',
    'api_key': "",
    'sig': "",
    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
}

try:
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print("Request successful!")
        print("Response:", response.json())
    else:
        print("Request failed with status code:", response.status_code)
except Exception as e:
    print("An error occurred:", e)
