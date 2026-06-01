#잡다한 을 넣어둔 파일
from datetime import datetime

def getcurruentDateTime():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')
