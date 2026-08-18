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


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 프롬프트 수정")
    print("9. 프롬프트 삭제")
    print("10. 조회수 TOP")
    print("11. Markdown 내보내기")
    print("0. 종료")


def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    while True:
        title = input("제목 (0: 취소): ").strip()

        if title == "0":
            print("프롬프트 추가를 취소했습니다.")
            return

        if title:
            break

        print("제목은 비워둘 수 없습니다.")

    while True:
        content = input("내용 (0: 취소): ").strip()

        if content == "0":
            print("프롬프트 추가를 취소했습니다.")
            return

        if content:
            break

        print("내용은 비워둘 수 없습니다.")

    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    print("\n카테고리 선택:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}) {category}")

    print("0) 취소")

    while True:
        category_choice = input("선택: ").strip()

        if category_choice == "0":
            print("프롬프트 추가를 취소했습니다.")
            return

        if category_choice.isdigit():
            number = int(category_choice)

            if 1 <= number <= len(categories):
                category = categories[number - 1]
                break

        print("올바른 카테고리 번호를 입력해주세요.")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "views": 0
    }

    prompts.append(new_prompt)

    print(f"\n'{title}' 프롬프트가 추가되었습니다!")

def show_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']}{favorite_mark}"
        )

    print(f"\n총 {len(prompts)}개의 프롬프트")

def show_by_category():
    print("\n=== 카테고리별 조회 ===")

    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    for index, category in enumerate(categories, start=1):
        print(f"{index}) {category}")

    print("0) 취소")

    while True:
        choice = input("선택: ").strip()

        if choice == "0":
            print("카테고리 조회를 취소했습니다.")
            return

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(categories):
                selected_category = categories[number - 1]
                break

        print("올바른 카테고리 번호를 입력해주세요.")

    filtered_prompts = []

    for prompt in prompts:
        if prompt["category"] == selected_category:
            filtered_prompts.append(prompt)

    print(f"\n=== [{selected_category}] 카테고리 프롬프트 ===")

    if not filtered_prompts:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(filtered_prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""
        print(f"{index}. {prompt['title']}{favorite_mark}")

    print(f"\n총 {len(filtered_prompts)}개의 프롬프트")

def search_prompt():
    print("\n=== 프롬프트 검색 ===")

    keyword = input("검색어 (0: 취소): ").strip()

    if keyword == "0":
        print("검색을 취소했습니다.")
        return

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    results = []

    for prompt in prompts:
        if (
            keyword.lower() in prompt["title"].lower()
            or keyword.lower() in prompt["content"].lower()
        ):
            results.append(prompt)

    print("\n검색 결과:")

    if not results:
        print("검색 결과가 없습니다.")
        return

    for index, prompt in enumerate(results, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""
        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']}{favorite_mark}"
        )

    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")

def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()

    while True:
        choice = input("\n프롬프트 번호 입력 (0: 취소): ").strip()

        if choice == "0":
            print("상세보기를 취소했습니다.")
            return

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(prompts):
                prompt = prompts[number - 1]
                break

        print("올바른 프롬프트 번호를 입력해주세요.")

    prompt["views"] += 1

    favorite_mark = "⭐" if prompt["favorite"] else "없음"

    print("\n────────────────────────────")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {favorite_mark}")
    print(f"조회수: {prompt['views']}")
    print("────────────────────────────")
    print("내용:")
    print(prompt["content"])
    print("────────────────────────────")

def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()

    while True:
        choice = input("\n프롬프트 번호 입력 (0: 취소): ").strip()

        if choice == "0":
            print("즐겨찾기 관리를 취소했습니다.")
            return

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(prompts):
                prompt = prompts[number - 1]
                break

        print("올바른 프롬프트 번호를 입력해주세요.")

    prompt["favorite"] = not prompt["favorite"]

    if prompt["favorite"]:
        print(f"\n'{prompt['title']}' 프롬프트를 즐겨찾기에 추가했습니다!")
    else:
        print(f"\n'{prompt['title']}' 프롬프트의 즐겨찾기를 해제했습니다.")


def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")

    favorite_prompts = []

    for prompt in prompts:
        if prompt["favorite"]:
            favorite_prompts.append(prompt)

    if not favorite_prompts:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(favorite_prompts, start=1):
        print(f"{index}. [{prompt['category']}] {prompt['title']} ⭐")

    print(f"\n총 {len(favorite_prompts)}개의 즐겨찾기")

def edit_prompt():
    print("\n=== 프롬프트 수정 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()

    while True:
        choice = input("\n수정할 프롬프트 번호 입력 (0: 취소): ").strip()

        if choice == "0":
            print("프롬프트 수정을 취소했습니다.")
            return

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(prompts):
                prompt = prompts[number - 1]
                break

        print("올바른 프롬프트 번호를 입력해주세요.")

    print("\n현재 정보")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"내용: {prompt['content']}")

    print("\n새 값을 입력하세요.")
    print("변경하지 않으려면 그냥 Enter를 누르세요.")

    new_title = input("새 제목: ").strip()

    if new_title:
        prompt["title"] = new_title

    new_content = input("새 내용: ").strip()

    if new_content:
        prompt["content"] = new_content

    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    print("\n카테고리 변경")
    print("0) 변경하지 않음")

    for index, category in enumerate(categories, start=1):
        print(f"{index}) {category}")

    while True:
        category_choice = input("선택: ").strip()

        if category_choice == "0" or category_choice == "":
            break

        if category_choice.isdigit():
            category_number = int(category_choice)

            if 1 <= category_number <= len(categories):
                prompt["category"] = categories[category_number - 1]
                break

        print("올바른 카테고리 번호를 입력해주세요.")

    print(f"\n'{prompt['title']}' 프롬프트가 수정되었습니다!")

while True:
    show_menu()

    choice = input("선택: ").strip()

    if choice == "0":
        print("프로그램을 종료합니다.")
        break

    elif choice == "1":
        add_prompt()

    elif choice == "2":
        show_list()

    elif choice == "3":
        show_by_category()

    elif choice == "4":
        search_prompt()

    elif choice == "5":
        show_detail()

    elif choice == "6":
        toggle_favorite()

    elif choice == "7":
        show_favorites()

    elif choice == "8":
        edit_prompt()

    elif choice in ["9", "10", "11"]:
        print("아직 구현되지 않은 기능입니다.")

    else:
        print("올바른 메뉴 번호를 입력해주세요.")