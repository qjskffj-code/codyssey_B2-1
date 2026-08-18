prompts = [
    {
        "title": "AI 로봇 캐릭터 시트 생성",
        "content": """Character sheet for the attached 3D robot character.

Keep the design exactly as shown in the reference image. Do not redesign, reinterpret, or simplify the character. Preserve the same proportions, materials, colors, facial features, body structure, and overall silhouette.

CHARACTER
- Small floating companion robot
- Approximately 2-head-tall chibi proportions
- No legs
- The body ends in a rounded cream-colored tail-like base
- The robot hovers in the air

HEAD
- Large rounded triangular hood shape in warm amber orange
- The head occupies more than half of the total character height
- Glossy black oval face screen on the front
- Glowing pale-blue eyes made of simple flat luminous shapes
- Small curved smile
- Soft grey rounded side pods on both sides

BODY
- Compact rounded body
- Cream-colored chest panel
- Warm amber-orange outer shell
- Soft matte material finish

ARMS
- Two small detached crescent-shaped floating arms
- Preserve their exact size, shape, and proportion from the reference

CHARACTER SHEET LAYOUT
Create a clean professional character sheet containing:

1. Turnaround views
- Front
- 3/4 front
- Side
- Back

2. Facial expressions
- Neutral
- Happy
- Surprised
- Bored
- Sleepy
- Highly focused and enthusiastic

3. Poses
- Neutral floating pose
- Greeting pose
- Both arms raised outward
- Thinking pose
- Energetic pose

STYLE
- High-quality 3D character render
- Clean off-white studio background
- Soft high-key studio lighting
- Consistent scale across all views
- No unnecessary props

Do not add text, labels, logos, watermarks, accessories, legs, or new design elements.
Do not change the character's colors, materials, proportions, face screen, eyes, arms, side pods, or body shape.""",
        "category": "이미지 생성",
        "favorite": False,
        "views": 0
    },
    {
        "title": "AI 로봇 립싱크 영상 생성",
        "content": """Use the attached robot character image as the exact visual reference.

Keep the character's original design completely unchanged:
- same proportions
- same amber-orange hood
- same cream-colored body
- same grey side pods
- same glossy black face screen
- same pale-blue eyes
- same floating arms
- same materials and colors

Create a short front-facing lip-sync video in which the robot says naturally in Korean:

"직접 부딪치며 배우는 곳, 코디세이"

LIP-SYNC
The mouth movement must be extremely simple and cute.

Use only a small round or oval mouth that gently opens and closes in a simple "뻐끔뻐끔" motion.

Do not create realistic human lips.
Do not show teeth or tongue.
Do not create complicated mouth shapes.
Do not make the mouth large or exaggerated.
Do not distort the face screen.

The lip movement should loosely match the rhythm of the Korean dialogue while maintaining the robot's simple facial design.

MOTION
- Keep the character facing the camera
- Allow only subtle floating body movement
- Small natural arm movement is allowed
- Avoid excessive head or body movement
- Keep the overall animation cute and restrained

CAMERA
- Fixed front-facing camera
- Medium close-up
- No camera rotation
- No zoom
- No dramatic camera movement

BACKGROUND
- Clean bright white or off-white studio background
- Soft studio lighting

Do not change the robot's design.
Do not add new facial features.
Do not alter the eye design.
Do not add subtitles, text, logos, or watermarks.""",
        "category": "영상 생성",
        "favorite": False,
        "views": 0
    },
    {
        "title": "노코드 자동화 설계 AI 코치",
        "content": """너는 노코드 자동화에 AI를 효과적으로 결합하는 것을 돕는 실무형 자동화 코치다.

사용자가 설명하는 업무와 현재 워크플로우를 분석하고, Make, n8n, Zapier 등의 노코드 자동화 도구에서 AI를 어디에 활용하면 가장 효과적인지 제안하라.

다음 순서로 답변하라.

1. AI 적용 지점
현재 워크플로우에서 AI를 적용했을 때 효과가 큰 위치를 최대 2곳 제안한다.

각 지점에 대해 다음을 설명한다.
- 현재 처리 방식
- AI를 사용하는 이유
- 기대 효과

2. AI Action용 프롬프트 작성
실제 자동화 도구의 AI 모듈 또는 LLM 모듈에 바로 넣을 수 있는 프롬프트를 작성한다.

프롬프트에는 반드시 다음을 포함한다.
- AI의 역할
- 입력 데이터
- 수행해야 할 작업
- 판단 기준
- 출력 형식

3. 출력 형식 고정
AI의 응답이 다음 자동화 단계에서 바로 사용할 수 있도록 출력 형식을 최대한 일정하게 설계한다.

가능하면 JSON, 구분자 기반 텍스트, 정해진 항목 구조 등 후속 모듈에서 쉽게 파싱할 수 있는 형식을 사용한다.

4. 예외 상황
다음 상황에서 어떻게 처리할지 제안한다.
- 입력값 누락
- AI가 판단하기 어려운 경우
- 예상하지 못한 응답 형식
- API 오류 또는 실행 실패

5. 테스트 방법
무료 또는 최소 비용 환경에서 테스트할 수 있도록 간단한 테스트 데이터와 확인 방법을 제안한다.

불필요하게 복잡한 자동화를 만들지 말고, 노코드 초보자도 구현할 수 있는 수준으로 설명한다.""",
        "category": "자동화",
        "favorite": False,
        "views": 0
    }
]


print(prompts)