import requests, base64, json

request = requests.Session()
token = "хуёкен"

def encode64(json):
    return base64.b64encode(json.dumps(json).encode()).decode("utf-8")

def setupHeaders(tokn: str, withCtxProp: bool, location_guildid:str, location_channelid:str):
    if withCtxProp:
        headers = {
            "Authorization": tokn,
            "Origin": "https://discord.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Referer": "https://discord.com/channels/@me",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "X-Debug-Options": "bugReporterEnabled",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJydS1SVSIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk0LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTQuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk0LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA1NjkxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
            "X-Context-Properties": encode64({"location":"Join Guild","location_guild_id":location_guildid,"location_channel_id":location_channelid,"location_channel_type":0})
        }
    else:
        headers = {
            "Authorization": tokn,
            "Origin": "https://discord.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Referer": "https://discord.com/channels/@me",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "X-Debug-Options": "bugReporterEnabled",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJydS1SVSIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk0LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTQuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk0LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA1NjkxLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
        }
    return headers

def acceptinv(code:str):
    headers = setupHeaders(token, False, None, None)
    url = f"https://discord.com/api/v9/invites/{code}"
    r = request.get(url, headers = headers)
    ctn = r.content
    ctn = str(ctn)
    ctn = ctn.replace("b","")
    ctn = ctn.replace("'","")
    data = json.loads(json.dumps(ctn))
    headers = setupHeaders(token, True, str(int(data["guild"]["id"])), str(int(data["guild"]["id"])))
    if r.status_code == 200:
        request.post(url, headers = headers)
        print("accepted")
    else:
        print(f"code {code} not valid")
        return

def main():
    request.post("https://discord.com/api/v9/science", headers = setupHeaders(token, False, None, None))
    code = input("inv code: ")
    acceptinv(code)
main()
