# 📰 오늘의 이슈 TOP 5 — 트렌드 랭킹 웹페이지

> AI가 취합한 최신 뉴스 트렌드를 1~5위 랭킹으로 보여주는 인터랙티브 정적 웹페이지입니다.

## 🌟 주요 기능

- **TOP 5 랭킹 카드** — 관심도 점수 기반 순위 표시
- **카테고리 필터** — 정치·사회 / 보안·IT / 경제 / AI·기술 / 글로벌
- **인터랙티브 차트** — 막대 / 레이더 / 도넛 차트 전환
- **카드 클릭 확장** — 배경 설명 및 핵심 포인트 상세 보기
- **실시간 뉴스 티커** — 상단 스크롤 뉴스 헤드라인
- **공유 버튼** — 클립보드 URL 복사
- **다크 모드 디자인** — 현대적이고 전문적인 UI

## 📁 파일 구조

```
news-ranking/
└── index.html   # 단일 HTML 파일 (CSS + JS 포함)
```

## 🚀 GitHub Pages 배포 방법

### 1단계: GitHub 저장소 생성

1. [GitHub](https://github.com)에 로그인합니다.
2. 우측 상단 `+` 버튼 → **New repository** 클릭
3. Repository name: `news-ranking` (또는 원하는 이름)
4. **Public** 선택 (GitHub Pages 무료 사용)
5. **Create repository** 클릭

### 2단계: 파일 업로드

**방법 A — 웹 인터페이스 (간단)**
1. 생성된 저장소 페이지에서 **"uploading an existing file"** 클릭
2. `index.html` 파일을 드래그하거나 선택
3. **Commit changes** 클릭

**방법 B — Git 명령어 (터미널)**
```bash
# 저장소 클론
git clone https://github.com/YOUR_USERNAME/news-ranking.git
cd news-ranking

# 파일 복사 후 업로드
cp /path/to/index.html .
git add index.html
git commit -m "feat: 오늘의 이슈 TOP 5 웹페이지 추가"
git push origin main
```

### 3단계: GitHub Pages 활성화

1. 저장소 → **Settings** 탭 클릭
2. 좌측 메뉴 → **Pages** 클릭
3. **Source** 섹션에서 `Deploy from a branch` 선택
4. Branch: `main` / Folder: `/ (root)` 선택
5. **Save** 클릭

### 4단계: 배포 확인

약 1~2분 후 아래 주소에서 웹페이지를 확인할 수 있습니다:

```
https://YOUR_USERNAME.github.io/news-ranking/
```

## 🔄 콘텐츠 업데이트 방법

`index.html` 파일 내 `newsData` 배열을 수정하면 됩니다:

```javascript
const newsData = [
  {
    rank: 1,
    category: "security",      // 카테고리 (security/politics/economy/tech/global)
    categoryLabel: "보안·IT",  // 표시 라벨
    tagClass: "tag-security",  // CSS 클래스
    date: "2026.04.29",        // 날짜
    title: "뉴스 제목",         // 제목
    summary: "요약 내용",       // 요약
    score: 98,                 // 관심도 점수 (0~100)
    trend: "up",               // 트렌드 (up/down/same)
    trendText: "▲ 급상승",     // 트렌드 텍스트
    hashtags: ["#태그1"],      // 해시태그 배열
    detail: {
      background: "배경 설명",
      keyPoints: ["포인트1", "포인트2"],
      source: "https://원문URL"
    }
  },
  // ... 나머지 4개 항목
];
```

## 📋 기술 스택

| 항목 | 내용 |
|------|------|
| 언어 | HTML5, CSS3, Vanilla JavaScript |
| 차트 | Chart.js 4.4.2 (CDN) |
| 폰트 | Noto Sans KR (Google Fonts) |
| 배포 | GitHub Pages (무료) |

## 📄 라이선스

MIT License — 자유롭게 수정 및 배포 가능합니다.
