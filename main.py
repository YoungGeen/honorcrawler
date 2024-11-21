import requests
import json


def fetch_app_details(pName):
    url = "https://appmarket-api-drcn.hispace.hihonorcloud.com/market/frameapi/v2/detail/byname/query"

    headers = {
        "accept-encoding": "gzip",
        "androidid": "93a05f81c34f1caa",
        "androidversion": "12",
        "apkver": "160024301",
        "areaid": "CN",
        "caller": "com.hihonor.appmarket",
        "content-length": "1023",
        "content-type": "application/json; charset=UTF-8",
        "flavor": "product",
        "language": "zh-CN",
        "launchtype": "1",
        "magicsysversion": "V417IR release-keys",
        "model": "ALA-AN70",
        "no-ecdh": "1",
        "sysversion": ".0.0",
        "traceid": "a4dea50086304e3992f1e71b4e610f8d",
        "udid": "",
        "uid": "",
        "user-agent": "Dalvik/2.1.0 (Linux; U; Android 12; ALA-AN70 Build/V417IR) com.hihonor.appmarket/160024301",
        "x-uuid": "ee743c05-f2a9-4e22-a3b2-6b3a49bb1f63"
    }

    body = {
        "resId": 0,
        "pName": pName,
        "ver": 0,
        "resType": 1,
        "pkgChannel": -1,
        "subChannel": "",
        "isAd": False,
        "orderSceneFlag": 0,
        "from": "com.hihonor.appmarket",
        "tInfo": {
            "androidId": "93a05f81c34f1caa",
            "udid": "",
            "userId": "",
            "accessToken": "",
            "ageLimit": 2147483647,
            "apkVerName": "16.0.24.301",
            "apkVer": 160024301,
            "chId": "HONOR_01",
            "compatibilityVar": {
                "cpuAbi": "x86_64",
                "bintranslatorEnable": -1,
                "cpuAbilist": "x86_64,arm64-v8a,x86,armeabi-v7a,armeabi",
                "hasHCore": 0
            },
            "cpu": "x86_64",
            "deviceMode": 1,
            "dpi": "480",
            "gaid": "ebfa0e7e-0e57-4aa4-8dcb-f90cdc243483",
            "hman": "HONOR",
            "htype": "ALA-AN70",
            "isDark": False,
            "isDemoType": 0,
            "isH5": 0,
            "isHWRecommend": False,
            "kidsMode": False,
            "isMonkey": 0,
            "isPersonalRecommend": True,
            "randomId": "ded09c2e-4658-49de-b914-702d807350e1",
            "isRecommend": True,
            "language": "zh-CN",
            "magicVersion": ".0.0",
            "marketType": 0,
            "netType": 3,
            "oaid": "",
            "os": 2,
            "osVer": "12",
            "pName": "com.hihonor.appmarket",
            "resolution": "1080x1920",
            "source": "1",
            "spreadModelName": "",
            "terminalType": 1,
            "timestamp": 1732088764489,
            "userType": "0",
            "telecomOper": ""
        }
    }


    response = requests.post(url, headers=headers, json=body)


    if response.status_code == 200:
        return response.json()
    else:
        print(f"请求失败，状态码：{response.status_code}")
        return None


pName = "xx.aaa.bbb"
app_details = fetch_app_details(pName)
if app_details:
    print(json.dumps(app_details, indent=4, ensure_ascii=False))
