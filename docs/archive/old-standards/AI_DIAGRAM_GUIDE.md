> **보관 문서(2026-10-28, D-147).** 더 이상 기준이 아닙니다. 원고 기준은 book-kit/book/PLAYBOOK.md와 BOOK_SPEC.md, 하위 에이전트 정의는 .claude/agents/(book-kit에서 동기화)를 따릅니다. 옛 결정의 근거를 찾을 때만 읽습니다.

# AI 다이어그램, 일러스트 생성 가이드(참고 자료)

- 받은 날: 2026-10-18(작가 제공)
- 용도: 다른 세션에서도 참고할 수 있도록 원문을 보관합니다. 이미지 생성 AI(Midjourney, Stable Diffusion 등)로 다이어그램이나 장 삽화를 만들 때의 프롬프트와 절차를 담고 있습니다.
- 이 책과의 관계: 이 책의 그림은 FIGURE_STYLE.md가 우선합니다. 아래 원문 가운데 아이콘, 3D와 아이소메트릭, 그러데이션, 영어 라벨, 비유 삽화, 제품 아이콘(AWS, Cisco 등)은 이 책의 그림 원칙(D-017, D-092, D-095, D-096)과 다르므로, 이 책의 그림에는 적용하지 않습니다.
- 아래는 받은 원문 그대로입니다.

---

PART 1. IT 도서용 AI 다이어그램 프레임워크 설계 가이드

기술 서적의 다이어그램은 화려함보다 구조의 명확성과 정보의 위계가 최우선입니다. 챕터별 핵심 기술 유형에 맞춘 프롬프트 템플릿과 스타일 가이드라인입니다.

## 1. 아키텍처 다이어그램 (Architecture Diagram)

- 시스템의 전체적인 구조, 레이어, 컴포넌트 간의 물리적/논리적 배치 관계를 설명할 때 사용합니다.

🎨 스타일 가이드

- 시각적 레이아웃: 3층 구조(SaaS-PaaS-IaaS) 또는 다층 레이어(Client-API-Backend-DB)의 명확한 수평/수직 분할.
- 오브젝트 스타일: 미니멀한 2D 플랫 아이콘, 아이소메트릭(Isometric) 3D 그리드(구조가 복잡한 경우).
- 조합 규칙: 컴포넌트 간 경계선은 명확해야 하며, 배경과 오브젝트가 겹치지 않아야 함.

📝 프롬프트 템플릿 (Prompt Template)

[영문 프롬프트]
```
A clean, minimalist 2D vector architecture diagram of a cloud computing system. 3-tier layering architecture: Client layer, Microservices API layer, and Distributed Database layer. Flat design, clean lines, corporate tech icon style. Isolated on a solid white background. No realistic shadows, no photographic texturing, high contrast, schematic design, technical publication quality --ar 16:9
```
[한글 번역 및 변형 가이드]
"클라우드 컴퓨팅 시스템의 깔끔하고 미니멀한 2D 벡터 아키텍처 다이어그램. 클라이언트, 마이크로서비스 API, 분산 DB 레이어로 구성된 3계층 구조. 플랫 디자인, 깔끔한 선, 기업 기술 아이콘 스타일. 순수 흰색 배경에 고립됨. 사실적인 그림자 없음, 고대비, 기술 서적 출판 품질."

## 2. 데이터 흐름도 (Data Flow Diagram / Pipeline)

- 데이터가 생성되어 수집, 가공, 저장, 분석되는 시계열적 흐름과 파이프라인을 설명할 때 사용합니다.

🎨 스타일 가이드

- 시각적 레이아웃: 왼쪽에서 오른쪽(Left-to-Right)으로 흐르는 단방향 또는 순환형 흐름.
- 오브젝트 스타일: 노드(Node)와 화살표(Connector) 중심의 링크 다이어그램 스타일. 흐름의 세기를 나타내는 선 굵기 제어.
- 조합 규칙: 데이터 소스, 처리 엔진, 저장소의 아이콘 형태가 명확히 구분되어야 함.

📝 프롬프트 템플릿 (Prompt Template)

[영문 프롬프트]
```
An enterprise data pipeline flowchart, left-to-right directional data flow diagram. Showing Data Source, Kafka Stream, Spark Processing Engine, and Cloud Data Warehouse nodes. Connected by clean vector arrows. Infographic style, blueprint technical drawing aesthetics, 2D flat, minimalist. Solid white background, high readability --ar 16:9
```
[한글 번역 및 변형 가이드]
"엔터프라이즈 데이터 파이프라인 순서도, 좌측에서 우측으로 향하는 데이터 흐름도. 데이터 소스, 카프카 스트림, 스파크 엔진, 클라우드 데이터 웨어하우스 노드 표시. 깔끔한 벡터 화살표로 연결됨. 인포그래픽 스타일, 청사진 기술 도면 미학, 2D 플랫. 흰색 배경, 높은 가독성."

## 3. 시스템 구성도 및 네트워크 토폴로지 (System & Network Topology)

- 인프라 구성, 가상 네트워크(VPC), 서브넷, 방화벽, 로드 밸런서 등의 배치와 보안 경계를 설명할 때 사용합니다.

🎨 스타일 가이드

- 시각적 레이아웃: 보안 그룹이나 서브넷을 나타내는 바운더리 박스(Boundary Box) 중심 구성.
- 오브젝트 스타일: AWS/Azure/GCP 스타일의 표준화된 인프라 토폴로지 아이콘 세트 느낌 반영.
- 조합 규칙: 외부망(Public)과 내부망(Private)의 시각적 격리 영역이 뚜렷해야 함.

📝 프롬프트 템플릿 (Prompt Template)

[영문 프롬프트]
```
A technical network topology diagram, secure infrastructure setup. Showing a Load Balancer distributing traffic to multiple EC2 instances inside a private subnet boundary box, guarded by a firewall icon. Clean vector schematics, Cisco or AWS style icon design language, flat 2D layout. Stark white background, no text placeholder blobs --ar 16:9
```
[한글 번역 및 변형 가이드]
"기술 네트워크 토폴로지 다이어그램, 보안 인프라 설정. 방화벽 아이콘과 프라이빗 서브넷 박스 내부의 여러 EC2 인스턴스로 트래픽을 분산하는 로드 밸런서 표시. 깔끔한 벡터 도면, AWS 스타일 아이콘 디자인, 플랫 2D 레이아웃. 순백색 배경."

---

PART 2. IT 기술서적 전문 AI 일러스트 생성 가이드북

책의 장(Chapter)이 시작할 때 들어가는 챕터 삽화(Chapter Illustration)나 개념을 비유적으로 표현하는 일러스트는 독자의 피로도를 낮추고 도서의 브랜드 아이덴티티를 확립합니다.

## 1. 일관성 있는 레이아웃 및 구도 (Layout & Grid)

AI로 매번 다른 이미지를 생성하더라도 책 전체에서 통일감을 주기 위한 레이아웃 제어 플러그인 및 기법입니다.

- 네거티브 스페이스(여백) 확보: 일러스트 내부에 타이틀 텍스트나 장 번호를 삽입할 수 있도록 공간을 비워두어야 합니다. 프롬프트에 Asymmetric composition, copy space on the left/right를 명시합니다.
- 통일된 뷰포트 एंगल (Camera Angle):
  - 개념 비유형: 정면(Frontal view) 또는 30도 측면 뷰로 통일.
  - 추상 기술형: 등각 투영법(Isometric view)으로 통일하여 기하학적이고 안정적인 느낌 전달.

[추천 레이아웃 유형]
1. 분할형 (Split): 좌측 30% 추상 오브젝트 + 우측 70% 여백 (텍스트용)
2. 하단 배치형 (Bottom-heavy): 하단에 기술 요소 배치 + 상단 그라데이션 여백

## 2. 기술 서적 전용 컬러 팔레트 (Color Palette)

인쇄(CMYK)와 화면(RGB) 모두에서 가독성이 높고, 이성적인 신뢰감을 주는 색상 조합을 사용합니다. AI 프롬프트 마지막에 아래의 컬러 토큰을 강제 지정합니다.

| 스타일 유형 | 추천 키워드 (Prompt Keywords) | 주요 색상 구성 (HEX 예시) | 활용 챕터 |
|---|---|---|---|
| Tech Enterprise | Deep Navy, Cyan, Slate Gray, Pure White background | #0A192F, #00B4D8, #E2E8F0 | 아키텍처, 클라우드, 보안 |
| Developer Warm | Charcoal, Muted Amber, Warm Ochre, Off-white background | #1A1A1A, #FFB703, #F8F9FA | 프론트엔드, 프로그래밍 기초 |
| Cyber Infrastructure | Matte Black, Neon Emerald, Steel Gray (어두운 테마용) | #121212, #00E676, #455A64 | DevOps, 리눅스 시스템 커널 |

## 3. 텍스트 가독성 및 AI 텍스트 왜곡 제어 (Text Readability)

AI 일러스트 생성 시 가장 큰 문제는 의미 없는 문자(Gibberish)가 텍스트처럼 깨져서 그려지는 현상입니다. 이를 방지하고 도서에 실제 텍스트를 얹기 위한 프로세스입니다.

- 프롬프트 제어 (무문자 최적화): 프롬프트 내에 글자 생성 소지를 원천 차단합니다.
  - 긍정 프롬프트 포함어: No text, letters, or numbers, Clean blank labels, Iconography without text
  - 부정 프롬프트(Negative Prompt) 필수어: text, typography, font, words, gibberish, letters, signature, watermark
- 포스트 프로덕션(후가공) 프로세스:
  1. AI 생성: 글자가 없는 순수 다이어그램/일러스트 베이스 이미지를 고해상도(Vectorization 또는 Upscaling)로 생성합니다.
  2. 레이어 분리: Figma 또는 Adobe Illustrator로 이미지를 가져옵니다.
  3. 폰트 브랜딩: 기술 서적용 표준 폰트(예: 프리텐다드, 나눔고딕 코딩, D2Coding)를 사용하여 AI가 비워둔 노드 위에 텍스트를 직접 타이핑하여 얹습니다.

---

PART 3. 일관성 있는 챕터 삽화 제작 프로세스 (SOP)

도서 한 권에 들어가는 10~15개 챕터의 삽화를 한 사람이 그린 것처럼 유지하기 위한 4단계 워크플로우입니다.

[Step 1: 마스터 스타일 정의] ➔ [Step 2: 시드(Seed) 값 고정] ➔ [Step 3: 이미지 투 이미지 활용] ➔ [Step 4: 벡터화 및 인쇄 검수]

## 1단계: 마스터 스타일 시트(Master Style Sheet) 정의

- 책의 메인 컨셉이 될 이미지 1장을 완벽하게 뽑아냅니다.
- 예시 스타일 지정: Flat vector illustration, Corporate Memphis style, tech concept, clean lines, 3-color palette (Navy, Orange, Light Gray), white background --seed 123456

## 2단계: 시드(Seed) 및 캐릭터/오브젝트 고정

- Midjourney의 --seed [번호] 기능이나 Stable Diffusion의 동일 시드 설정을 통해 이미지의 질감, 선의 두께, 빛의 방향을 전 챕터에 걸쳐 고정합니다.
- 특정 마스코트나 캐릭터가 반복 등장해야 한다면 Inpaint 기능이나 InsightFace 등을 활용해 얼굴/형태 일관성을 유지합니다.

## 3단계: 이미지 투 이미지(Image-to-Image) 및 레퍼런스 활용

- 1장에서 성공한 마스터 이미지를 URL 레퍼런스로 입력(Midjourney --sref URL)하거나, 베이스 이미지로 레이아웃을 제공하여 다음 챕터 이미지를 변형 생성합니다.
- 예: 1장(서버) 이미지 구조를 유지한 채, 2장(데이터베이스) 콘셉트로 변경 요청.

## 4단계: 벡터화(Vectorization) 및 인쇄 사양 검수

- AI가 생성한 고해상도 PNG/JPG 파일은 출판 인쇄 시 깨질 수 있습니다.
- 벡터 변환: Vectorizer.ai 혹은 Adobe Illustrator의 Image Trace(이미지 추적) 기능을 이용하여 SVG/EPS 파일로 변환합니다.
- 색상 영역 변환: RGB로 생성된 이미지를 인쇄용 CMYK(Coated FOGRA39 등)로 변환 후, 탁해진 색상이 없는지 감리 및 보정 단계를 거칩니다.
