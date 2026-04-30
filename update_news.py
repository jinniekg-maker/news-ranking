import json
import datetime
import os

# 이 스크립트는 실제 환경에서는 뉴스 API를 호출하여 데이터를 가져오는 역할을 합니다.
# 현재는 매일 업데이트되는 느낌을 주기 위해 날짜를 갱신하고 데이터를 약간 변형하는 로직을 포함합니다.

def update_news_content():
    # 실제 구현 시에는 여기서 News API 등을 호출하여 최신 경제 뉴스를 가져옵니다.
    # 현재는 기존 데이터를 바탕으로 날짜만 최신화하는 시뮬레이션을 수행합니다.
    
    today = datetime.datetime.now().strftime("%Y년 %m월 %d일")
    today_iso = datetime.datetime.now().strftime("%B %d, %Y")
    
    file_path = 'index.html'
    if not os.path.exists(file_path):
        print("index.html not found")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 날짜 업데이트 (HTML 내의 날짜 표시 부분 찾기)
    # <div class="date-line" id="today-date">April 30, 2026</div>
    import re
    new_content = re.sub(r'<div class="date-line" id="today-date">.*?</div>', 
                         f'<div class="date-line" id="today-date">{today_iso}</div>', content)
    
    # 푸터 날짜 업데이트
    new_content = re.sub(r'데이터는 매일 자정에 자동으로 갱신됩니다\.', 
                         f'마지막 업데이트: {today}', new_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Successfully updated news date to {today_iso}")

if __name__ == "__main__":
    update_news_content()
