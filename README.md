# Silhouette

### 개인 프로젝트
<br/><br/>
### 😊 프로젝트 개요

---

![home](https://github.com/yongjun-shin/silhouette/assets/73512218/21e8e720-9b89-4b25-ba8e-e8df5f5ab9c6)


- 개인이 가지고 있는 옷을 외우는 것이 불가능하고, 특히 옷장을 보아도 무슨 옷이 있는지 한눈에 들어오지 않기 때문에 ‘내가 가진 옷을 웹 상의 옷장에서 관리하면 좋겠다’ 라는 생각에서 실행한 프로젝트입니다.

[기대 효과]

- 효율적인 옷 관리로 만족도 상승.
<br/><br /><br /><br />
### 🎢 과정

---

1. 서비스 기획
2. UI/UX 설계
3. 데이터베이스 구축
4. 웹 구현
<br/><br /><br /><br />
### 🛠 서비스 기능

---

1. 회원가입, 로그인 기능
2. 옷, 악세서리, 신발 추가 및 삭제 기능
    - 옷, 악세서리, 신발과 같이 세 개의 카테고리로 나누어서 추가 및 삭제 가능합니다.
    - 새로운 아이템 추가시 사진 파일 함께 등록하여 같은 이름의 옷을 이미지 직접 보며 구분 가능합니다.
3.  마이페이지
    - 현재 옷장에 외투, 상의, 신발 등이 몇 개씩 존재하는지 직관적으로 확인 가능하도록 구현했습니다.
4. (추후 구현)
    a. Weather 페이지
        - 날씨 API를 이용해서 오늘의 날씨를 제공합니다. 옷을 고를 때 참고할 수 있도록 도와줍니다.
        - 옷을 고를 때 가장 밀접하게 연관이 되어 있는 것이 날씨입니다.
        - 물론 집에서도 창문을 통해 현재의 날씨를 확인 가능하지만, 오후에 비나 눈이 올 수 있는 경우 때문에 날씨를 NAVER나 날씨 앱을 통해 확인해야 합니다. Silhouette 서비스 내에서  옷 고르기와 날씨를 동시에 해결하여 번거로움을 최소화하는 것이 목표입니다.
    b. Gallery 페이지
        - 오늘 입고 나갈 옷을 고르고, 어떤 약속으로 인해 나가는지를 간단히 기록할 수 있는 페이지 입니다.
        - 핸드폰의 gallery에서 사진을 보며 추억하듯이 어떤 약속에 어떤 옷을 입고 나갔는지를 기록함으로써 추억을 회상할 수 있도록 도와주는 페이지입니다.
    c. Trend 페이지
        - 옷 관련 종류가 유행에 굉장히 민감한데 요즘 어떤 옷이 유행하는지 볼 수 있게 도와주는 페이지입니다.
        - 어떤 방식으로 구현해야 할지 고민중에 있습니다.
            ex) 무신사와 같은 패션 플랫폼의 상위 랭크 보여주기
<br/><br /><br /><br />

### 📘 Stacks

---

<div>
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white" />
    <img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=HTML5&logoColor=white" />
    <img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=CSS3&logoColor=white" />
    <img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=Figma&logoColor=white" />
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white" />
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white" />
</div>
<br/><br /><br /><br />

### 📈 구현

---

1. 로그인 → 메뉴 탭 → Closet 으로 이동하여  옷장의 옷 보기, 옷 추가, 옷 삭제가 가능합니다.
    
    ![menu](https://github.com/yongjun-shin/silhouette/assets/73512218/ede7a838-c144-4730-9a5d-818d3651b4a9)

    ![closet](https://github.com/yongjun-shin/silhouette/assets/73512218/3ced1eff-bf5f-4578-9efd-fefc059267fb)

    - 순서대로 의류, 악세서리, 신발 보관함입니다. 우선 의류 보관함으로 이동하겠습니다.

    ![clothes](https://github.com/yongjun-shin/silhouette/assets/73512218/efe3c050-1b1b-49c9-a73b-d0d1f280d5ee)

    - 현재 옷장에 있는 옷들을 볼 수 있습니다. add 버튼을 눌러보겠습니다.

    ![add](https://github.com/yongjun-shin/silhouette/assets/73512218/905d7604-fead-40ba-8638-0b1a96746c86)

    - 위 양식대로 입력 후 Add 버튼을 클릭하면 DB에 데이터가 추가되고 옷장에 바로 새로운 옷이 추가됩니다.

    ![modal_clothes](https://github.com/yongjun-shin/silhouette/assets/73512218/7ae84c3f-ae85-441b-9496-eb8ea553176e)

    - 또한, 옷장에서 이름 부분을 클릭하면 해당 옷에 해당되는 이미지를 확인할 수 있습니다.
<br /><br />
2. 마이페이지에서 현재 보관중인 옷, 악세서리, 신발의 수를 직관적으로 확인할 수 있습니다.

    ![mypage](https://github.com/yongjun-shin/silhouette/assets/73512218/7abfa4bd-47ca-43ce-aadb-e9e605d044fb)

