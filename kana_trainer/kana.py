# 히라가나와 가타카나 학습용 문자 데이터를 제공한다.
from __future__ import annotations

KanaEntry = tuple[str, str]
MAX_KANA_LEVEL = 4
KANA_LEVEL_LABELS: dict[int, str] = {
    1: "기본",
    2: "탁음·반탁음",
    3: "작은 글자 조합",
    4: "단어 뜻 맞히기",
}


HIRAGANA: tuple[KanaEntry, ...] = (
    ("あ", "a"),
    ("い", "i"),
    ("う", "u"),
    ("え", "e"),
    ("お", "o"),
    ("か", "ka"),
    ("き", "ki"),
    ("く", "ku"),
    ("け", "ke"),
    ("こ", "ko"),
    ("さ", "sa"),
    ("し", "shi"),
    ("す", "su"),
    ("せ", "se"),
    ("そ", "so"),
    ("た", "ta"),
    ("ち", "chi"),
    ("つ", "tsu"),
    ("て", "te"),
    ("と", "to"),
    ("な", "na"),
    ("に", "ni"),
    ("ぬ", "nu"),
    ("ね", "ne"),
    ("の", "no"),
    ("は", "ha"),
    ("ひ", "hi"),
    ("ふ", "fu"),
    ("へ", "he"),
    ("ほ", "ho"),
    ("ま", "ma"),
    ("み", "mi"),
    ("む", "mu"),
    ("め", "me"),
    ("も", "mo"),
    ("や", "ya"),
    ("ゆ", "yu"),
    ("よ", "yo"),
    ("ら", "ra"),
    ("り", "ri"),
    ("る", "ru"),
    ("れ", "re"),
    ("ろ", "ro"),
    ("わ", "wa"),
    ("を", "wo"),
    ("ん", "n"),
)

KATAKANA: tuple[KanaEntry, ...] = (
    ("ア", "a"),
    ("イ", "i"),
    ("ウ", "u"),
    ("エ", "e"),
    ("オ", "o"),
    ("カ", "ka"),
    ("キ", "ki"),
    ("ク", "ku"),
    ("ケ", "ke"),
    ("コ", "ko"),
    ("サ", "sa"),
    ("シ", "shi"),
    ("ス", "su"),
    ("セ", "se"),
    ("ソ", "so"),
    ("タ", "ta"),
    ("チ", "chi"),
    ("ツ", "tsu"),
    ("テ", "te"),
    ("ト", "to"),
    ("ナ", "na"),
    ("ニ", "ni"),
    ("ヌ", "nu"),
    ("ネ", "ne"),
    ("ノ", "no"),
    ("ハ", "ha"),
    ("ヒ", "hi"),
    ("フ", "fu"),
    ("ヘ", "he"),
    ("ホ", "ho"),
    ("マ", "ma"),
    ("ミ", "mi"),
    ("ム", "mu"),
    ("メ", "me"),
    ("モ", "mo"),
    ("ヤ", "ya"),
    ("ユ", "yu"),
    ("ヨ", "yo"),
    ("ラ", "ra"),
    ("リ", "ri"),
    ("ル", "ru"),
    ("レ", "re"),
    ("ロ", "ro"),
    ("ワ", "wa"),
    ("ヲ", "wo"),
    ("ン", "n"),
)

HIRAGANA_MARKS: tuple[KanaEntry, ...] = (
    ("が", "ga"),
    ("ぎ", "gi"),
    ("ぐ", "gu"),
    ("げ", "ge"),
    ("ご", "go"),
    ("ざ", "za"),
    ("じ", "ji"),
    ("ず", "zu"),
    ("ぜ", "ze"),
    ("ぞ", "zo"),
    ("だ", "da"),
    ("ぢ", "ji"),
    ("づ", "zu"),
    ("で", "de"),
    ("ど", "do"),
    ("ば", "ba"),
    ("び", "bi"),
    ("ぶ", "bu"),
    ("べ", "be"),
    ("ぼ", "bo"),
    ("ぱ", "pa"),
    ("ぴ", "pi"),
    ("ぷ", "pu"),
    ("ぺ", "pe"),
    ("ぽ", "po"),
)

KATAKANA_MARKS: tuple[KanaEntry, ...] = (
    ("ガ", "ga"),
    ("ギ", "gi"),
    ("グ", "gu"),
    ("ゲ", "ge"),
    ("ゴ", "go"),
    ("ザ", "za"),
    ("ジ", "ji"),
    ("ズ", "zu"),
    ("ゼ", "ze"),
    ("ゾ", "zo"),
    ("ダ", "da"),
    ("ヂ", "ji"),
    ("ヅ", "zu"),
    ("デ", "de"),
    ("ド", "do"),
    ("バ", "ba"),
    ("ビ", "bi"),
    ("ブ", "bu"),
    ("ベ", "be"),
    ("ボ", "bo"),
    ("パ", "pa"),
    ("ピ", "pi"),
    ("プ", "pu"),
    ("ペ", "pe"),
    ("ポ", "po"),
)

HIRAGANA_YOON: tuple[KanaEntry, ...] = (
    ("きゃ", "kya"),
    ("きゅ", "kyu"),
    ("きょ", "kyo"),
    ("しゃ", "sha"),
    ("しゅ", "shu"),
    ("しょ", "sho"),
    ("ちゃ", "cha"),
    ("ちゅ", "chu"),
    ("ちょ", "cho"),
    ("にゃ", "nya"),
    ("にゅ", "nyu"),
    ("にょ", "nyo"),
    ("ひゃ", "hya"),
    ("ひゅ", "hyu"),
    ("ひょ", "hyo"),
    ("みゃ", "mya"),
    ("みゅ", "myu"),
    ("みょ", "myo"),
    ("りゃ", "rya"),
    ("りゅ", "ryu"),
    ("りょ", "ryo"),
    ("ぎゃ", "gya"),
    ("ぎゅ", "gyu"),
    ("ぎょ", "gyo"),
    ("じゃ", "ja"),
    ("じゅ", "ju"),
    ("じょ", "jo"),
    ("びゃ", "bya"),
    ("びゅ", "byu"),
    ("びょ", "byo"),
    ("ぴゃ", "pya"),
    ("ぴゅ", "pyu"),
    ("ぴょ", "pyo"),
)

KATAKANA_YOON: tuple[KanaEntry, ...] = (
    ("キャ", "kya"),
    ("キュ", "kyu"),
    ("キョ", "kyo"),
    ("シャ", "sha"),
    ("シュ", "shu"),
    ("ショ", "sho"),
    ("チャ", "cha"),
    ("チュ", "chu"),
    ("チョ", "cho"),
    ("ニャ", "nya"),
    ("ニュ", "nyu"),
    ("ニョ", "nyo"),
    ("ヒャ", "hya"),
    ("ヒュ", "hyu"),
    ("ヒョ", "hyo"),
    ("ミャ", "mya"),
    ("ミュ", "myu"),
    ("ミョ", "myo"),
    ("リャ", "rya"),
    ("リュ", "ryu"),
    ("リョ", "ryo"),
    ("ギャ", "gya"),
    ("ギュ", "gyu"),
    ("ギョ", "gyo"),
    ("ジャ", "ja"),
    ("ジュ", "ju"),
    ("ジョ", "jo"),
    ("ビャ", "bya"),
    ("ビュ", "byu"),
    ("ビョ", "byo"),
    ("ピャ", "pya"),
    ("ピュ", "pyu"),
    ("ピョ", "pyo"),
)

CONFUSING_PAIRS: dict[str, tuple[tuple[str, str, str], ...]] = {
    "hiragana": (
        ("し", "つ", "し는 왼쪽 열림 / つ는 오른쪽 열림"),
        ("そ", "ん", "そ는 점이 붙고, ん은 짧게 끝"),
        ("ぬ", "め", "ぬ=고리+꼬리 / め=고리 단단히 닫힘"),
        ("ね", "れ", "ね=막대+배(고리) / れ=고리 없음"),
        ("わ", "れ", "わ 끝에 작은 점 느낌 / れ는 크게 휨"),
    ),
    "katakana": (
        ("シ", "ツ", "シ는 왼쪽 열림 / ツ는 오른쪽 열림"),
        ("ソ", "ン", "ソ는 점이 붙고, ン은 짧게 끝"),
        ("ヌ", "メ", "ヌ=고리+꼬리 / メ=고리 단단히 닫힘"),
        ("ネ", "レ", "ネ=막대+배(고리) / レ=고리 없음"),
        ("ワ", "レ", "ワ 끝에 작은 점 느낌 / レ는 크게 휨"),
    ),
}

READING_EXAMPLES: dict[str, tuple[tuple[str, str, str, str], ...]] = {
    "hiragana": (
        ("きょう", "kyou", "쿄우", "오늘/오늘날; 今日"),
        ("しゃしん", "shashin", "샤신", "사진"),
        ("りょこう", "ryokou", "료코-", "여행"),
        ("にゃん", "nyan", "냥/냥~", "고양이 울음 흉내"),
        ("おちゃ", "ocha", "오챠", "차"),
    ),
    "katakana": (
        ("キョウ", "kyou", "쿄우", "오늘/오늘날; 今日"),
        ("シャシン", "shashin", "샤신", "사진"),
        ("リョコウ", "ryokou", "료코우", "여행"),
        ("ニャン", "nyan", "냥/냥~", "고양이 울음 흉내"),
        ("オチャ", "ocha", "오챠", "차"),
    ),
}

SOKUON_EXAMPLES: dict[str, tuple[tuple[str, str, str, str], ...]] = {
    "hiragana": (
        ("がっこう", "gakkou", "가(ㄲ)꼬-", "학교"),
        ("きって", "kitte", "킷테", "우표"),
        ("ちょっと", "chotto", "춋토/춋또", "조금"),
        ("べっさつ", "bessatsu", "벳사츠", "별책"),
    ),
    "katakana": (
        ("ガッコウ", "gakkou", "가(ㄲ)꼬우", "학교"),
        ("キッテ", "kitte", "킷테", "우표"),
        ("チョット", "chotto", "춋토/춋또", "조금"),
        ("ベッサツ", "bessatsu", "벳사츠", "별책"),
    ),
}

WORD_MEANING_EXAMPLES: dict[str, tuple[tuple[str, str, str, str], ...]] = {
    "hiragana": READING_EXAMPLES["hiragana"] + SOKUON_EXAMPLES["hiragana"] + (
        ("あさ", "asa", "아사", "아침"),
        ("ひる", "hiru", "히루", "낮/점심"),
        ("よる", "yoru", "요루", "밤"),
        ("いま", "ima", "이마", "지금"),
        ("あした", "ashita", "아시타", "내일"),
        ("きのう", "kinou", "키노우", "어제"),
        ("まいにち", "mainichi", "마이니치", "매일"),
        ("ともだち", "tomodachi", "토모다치", "친구"),
        ("せんせい", "sensei", "센세이", "선생님"),
        ("がくせい", "gakusei", "가쿠세이", "학생"),
        ("こども", "kodomo", "코도모", "아이"),
        ("おとな", "otona", "오토나", "어른"),
        ("おんな", "onna", "온나", "여자"),
        ("おとこ", "otoko", "오토코", "남자"),
        ("ひと", "hito", "히토", "사람"),
        ("いぬ", "inu", "이누", "개"),
        ("ねこ", "neko", "네코", "고양이"),
        ("とり", "tori", "토리", "새"),
        ("さかな", "sakana", "사카나", "생선/물고기"),
        ("やま", "yama", "야마", "산"),
        ("かわ", "kawa", "카와", "강"),
        ("うみ", "umi", "우미", "바다"),
        ("そら", "sora", "소라", "하늘"),
        ("あめ", "ame", "아메", "비"),
        ("ゆき", "yuki", "유키", "눈"),
        ("かぜ", "kaze", "카제", "바람"),
        ("はな", "hana", "하나", "꽃"),
        ("みず", "mizu", "미즈", "물"),
        ("ひ", "hi", "히", "불"),
        ("つき", "tsuki", "츠키", "달"),
        ("ほし", "hoshi", "호시", "별"),
        ("くも", "kumo", "쿠모", "구름"),
        ("いえ", "ie", "이에", "집"),
        ("へや", "heya", "헤야", "방"),
        ("まち", "machi", "마치", "마을/거리"),
        ("みせ", "mise", "미세", "가게"),
        ("えき", "eki", "에키", "역"),
        ("みち", "michi", "미치", "길"),
        ("くるま", "kuruma", "쿠루마", "자동차"),
        ("でんしゃ", "densha", "덴샤", "전철/기차"),
        ("じてんしゃ", "jitensha", "지텐샤", "자전거"),
        ("ほん", "hon", "혼", "책"),
        ("かみ", "kami", "카미", "종이"),
        ("え", "e", "에", "그림"),
        ("てがみ", "tegami", "테가미", "편지"),
        ("つくえ", "tsukue", "츠쿠에", "책상"),
        ("いす", "isu", "이스", "의자"),
        ("かばん", "kaban", "카반", "가방"),
        ("とけい", "tokei", "토케이", "시계"),
        ("かさ", "kasa", "카사", "우산"),
        ("くつ", "kutsu", "쿠츠", "신발"),
        ("ふく", "fuku", "후쿠", "옷"),
        ("ぼうし", "boushi", "보우시", "모자"),
        ("め", "me", "메", "눈(신체)"),
        ("みみ", "mimi", "미미", "귀"),
        ("くち", "kuchi", "쿠치", "입"),
        ("て", "te", "테", "손"),
        ("あし", "ashi", "아시", "발/다리"),
        ("からだ", "karada", "카라다", "몸"),
        ("こころ", "kokoro", "코코로", "마음"),
        ("こえ", "koe", "코에", "목소리"),
        ("なまえ", "namae", "나마에", "이름"),
        ("ことば", "kotoba", "코토바", "말/언어"),
        ("ごはん", "gohan", "고한", "밥/식사"),
        ("あさごはん", "asagohan", "아사고한", "아침밥"),
        ("ひるごはん", "hirugohan", "히루고한", "점심밥"),
        ("ばんごはん", "bangohan", "반고한", "저녁밥"),
        ("りんご", "ringo", "링고", "사과"),
        ("みかん", "mikan", "미칸", "귤"),
        ("たまご", "tamago", "타마고", "달걀"),
        ("にく", "niku", "니쿠", "고기"),
        ("やさい", "yasai", "야사이", "채소"),
        ("くだもの", "kudamono", "쿠다모노", "과일"),
        ("おかね", "okane", "오카네", "돈"),
        ("じかん", "jikan", "지칸", "시간"),
        ("でんわ", "denwa", "덴와", "전화"),
        ("しごと", "shigoto", "시고토", "일/직업"),
        ("べんきょう", "benkyou", "벤쿄우", "공부"),
        ("あそび", "asobi", "아소비", "놀이"),
        ("うた", "uta", "우타", "노래"),
        ("おどり", "odori", "오도리", "춤"),
        ("えいが", "eiga", "에이가", "영화"),
        ("おんがく", "ongaku", "온가쿠", "음악"),
        ("てんき", "tenki", "텐키", "날씨"),
        ("きもち", "kimochi", "키모치", "기분"),
        ("びょうき", "byouki", "뵤우키", "병"),
        ("くすり", "kusuri", "쿠스리", "약"),
        ("びょういん", "byouin", "뵤우인", "병원"),
        ("だいがく", "daigaku", "다이가쿠", "대학교"),
        ("きょうしつ", "kyoushitsu", "쿄우시츠", "교실"),
        ("としょかん", "toshokan", "토쇼칸", "도서관"),
        ("こうえん", "kouen", "코우엔", "공원"),
        ("こうばん", "kouban", "코우반", "파출소"),
        ("くうこう", "kuukou", "쿠우코우", "공항"),
        ("りょうり", "ryouri", "료우리", "요리"),
        ("しお", "shio", "시오", "소금"),
        ("さとう", "satou", "사토우", "설탕"),
        ("あじ", "aji", "아지", "맛"),
        ("ちず", "chizu", "치즈", "지도"),
        ("にもつ", "nimotsu", "니모츠", "짐/수하물"),
    ),
    "katakana": READING_EXAMPLES["katakana"] + SOKUON_EXAMPLES["katakana"] + (
        ("アイス", "aisu", "아이스", "아이스크림/얼음"),
        ("アパート", "apaato", "아파토", "아파트"),
        ("アニメ", "anime", "아니메", "애니메이션"),
        ("アルバイト", "arubaito", "아루바이토", "아르바이트"),
        ("イベント", "ibento", "이벤토", "이벤트"),
        ("インターネット", "intaanetto", "인타넷토", "인터넷"),
        ("エアコン", "eakon", "에아콘", "에어컨"),
        ("エレベーター", "erebeetaa", "에레베타", "엘리베이터"),
        ("オフィス", "ofisu", "오피스", "사무실"),
        ("カード", "kaado", "카도", "카드"),
        ("カメラ", "kamera", "카메라", "카메라"),
        ("カレンダー", "karendaa", "카렌다", "달력"),
        ("カレー", "karee", "카레", "카레"),
        ("ギター", "gitaa", "기타", "기타"),
        ("クラス", "kurasu", "쿠라스", "반/수업"),
        ("クリスマス", "kurisumasu", "쿠리스마스", "크리스마스"),
        ("ケーキ", "keeki", "케키", "케이크"),
        ("コーヒー", "koohii", "코히", "커피"),
        ("コンビニ", "konbini", "콘비니", "편의점"),
        ("コンピューター", "konpyuutaa", "콘퓨타", "컴퓨터"),
        ("サッカー", "sakkaa", "삭카", "축구"),
        ("サラダ", "sarada", "사라다", "샐러드"),
        ("サンドイッチ", "sandoicchi", "산도잇치", "샌드위치"),
        ("シャツ", "shatsu", "샤츠", "셔츠"),
        ("シャワー", "shawaa", "샤와", "샤워"),
        ("スーパー", "suupaa", "수파", "슈퍼마켓"),
        ("スカート", "sukaato", "스카토", "치마"),
        ("スキー", "sukii", "스키", "스키"),
        ("スクール", "sukuuru", "스쿠루", "학교/스쿨"),
        ("スケジュール", "sukejuuru", "스케주루", "일정"),
        ("スプーン", "supuun", "스푼", "숟가락"),
        ("スポーツ", "supootsu", "스포츠", "스포츠"),
        ("スマホ", "sumaho", "스마호", "스마트폰"),
        ("セーター", "seetaa", "세타", "스웨터"),
        ("センター", "sentaa", "센타", "센터"),
        ("タクシー", "takushii", "타쿠시", "택시"),
        ("チーズ", "chiizu", "치즈", "치즈"),
        ("チケット", "chiketto", "치켓토", "표/티켓"),
        ("チョコ", "choko", "초코", "초콜릿"),
        ("テーブル", "teeburu", "테부루", "탁자"),
        ("テレビ", "terebi", "테레비", "텔레비전"),
        ("テスト", "tesuto", "테스토", "시험"),
        ("テニス", "tenisu", "테니스", "테니스"),
        ("ドア", "doa", "도아", "문"),
        ("トイレ", "toire", "토이레", "화장실"),
        ("トラック", "torakku", "토락쿠", "트럭"),
        ("ドラマ", "dorama", "도라마", "드라마"),
        ("ニュース", "nyuusu", "뉴수", "뉴스"),
        ("ネクタイ", "nekutai", "네쿠타이", "넥타이"),
        ("ノート", "nooto", "노토", "노트"),
        ("パーティー", "paatii", "파티", "파티"),
        ("バス", "basu", "바스", "버스"),
        ("パソコン", "pasokon", "파소콘", "개인용 컴퓨터"),
        ("パン", "pan", "판", "빵"),
        ("ピアノ", "piano", "피아노", "피아노"),
        ("ビール", "biiru", "비루", "맥주"),
        ("ピザ", "piza", "피자", "피자"),
        ("ビデオ", "bideo", "비데오", "비디오"),
        ("ファイル", "fairu", "화이루", "파일"),
        ("フォーク", "fooku", "포쿠", "포크"),
        ("プール", "puuru", "푸루", "수영장"),
        ("ベッド", "beddo", "벳도", "침대"),
        ("ペット", "petto", "펫토", "반려동물"),
        ("ペン", "pen", "펜", "펜"),
        ("ホテル", "hoteru", "호테루", "호텔"),
        ("ボール", "booru", "보루", "공"),
        ("ポケット", "poketto", "포켓토", "주머니"),
        ("ポスト", "posuto", "포스토", "우체통"),
        ("マスク", "masuku", "마스쿠", "마스크"),
        ("メール", "meeru", "메루", "이메일"),
        ("メニュー", "menyuu", "메뉴", "메뉴"),
        ("モデル", "moderu", "모데루", "모델"),
        ("ラジオ", "rajio", "라지오", "라디오"),
        ("レストラン", "resutoran", "레스토란", "식당/레스토랑"),
        ("レポート", "repooto", "레포토", "보고서"),
        ("ワイン", "wain", "와인", "와인"),
        ("アクセス", "akusesu", "아쿠세스", "접근/접속"),
        ("アドレス", "adoresu", "아도레스", "주소"),
        ("アプリ", "apuri", "아푸리", "앱"),
        ("アルバム", "arubamu", "아루바무", "앨범"),
        ("イメージ", "imeeji", "이메지", "이미지"),
        ("ウイルス", "uirusu", "우이루스", "바이러스"),
        ("エンジン", "enjin", "엔진", "엔진"),
        ("オレンジ", "orenji", "오렌지", "오렌지"),
        ("ガイド", "gaido", "가이도", "안내/가이드"),
        ("ガラス", "garasu", "가라스", "유리"),
        ("キャンプ", "kyanpu", "캰푸", "캠프"),
        ("クッキー", "kukkii", "쿳키", "쿠키"),
        ("クラブ", "kurabu", "쿠라부", "동아리/클럽"),
        ("ゲーム", "geemu", "게무", "게임"),
        ("コピー", "kopii", "코피", "복사"),
        ("ゴルフ", "gorufu", "고루후", "골프"),
        ("ジュース", "juusu", "주스", "주스"),
        ("スープ", "suupu", "수푸", "수프"),
        ("スーツ", "suutsu", "수츠", "정장"),
        ("ストーブ", "sutoobu", "스토부", "난로"),
        ("タオル", "taoru", "타오루", "수건"),
        ("ダンス", "dansu", "단스", "춤/댄스"),
        ("データ", "deeta", "데타", "데이터"),
        ("パスポート", "pasupooto", "파스포토", "여권"),
    ),
}

PARTICLES: tuple[dict[str, object], ...] = (
    {
        "particle": "は",
        "reading": "wa",
        "meaning": "은/는",
        "note": "주제를 표시하며 발음은 하가 아니라 와.",
        "examples": ("わたしは学生です。", "これはペンです。"),
    },
    {
        "particle": "が",
        "reading": "ga",
        "meaning": "이/가",
        "note": "주어, 처음 등장하는 정보, 강조에 자주 쓴다.",
        "examples": ("ねこがいます。", "だれが来ますか？"),
    },
    {
        "particle": "を",
        "reading": "o",
        "meaning": "을/를",
        "note": "목적어를 표시하며 발음은 오.",
        "examples": ("パンを食べます。", "映画を見ます。"),
    },
    {
        "particle": "の",
        "reading": "no",
        "meaning": "의 / ~의 것 / 소유·소속",
        "note": "A의 B, 내 것 같은 소유 관계를 나타낸다.",
        "examples": ("わたしの本。", "これはだれのですか？"),
    },
    {
        "particle": "に",
        "reading": "ni",
        "meaning": "에 / 에게",
        "note": "시간, 도착점, 대상을 나타낸다.",
        "examples": ("3時に来ます。", "学校に行きます。", "先生に聞きます。"),
    },
    {
        "particle": "で",
        "reading": "de",
        "meaning": "에서 / 로",
        "note": "행동이 일어나는 장소나 수단을 나타낸다.",
        "examples": ("学校で勉強します。", "バスで行きます。"),
    },
    {
        "particle": "へ",
        "reading": "e",
        "meaning": "~로",
        "note": "방향을 나타내며 보통 에처럼 발음한다.",
        "examples": ("日本へ行きます。",),
    },
    {
        "particle": "と",
        "reading": "to",
        "meaning": "와/과 / ~라고",
        "note": "대상 연결이나 말·생각의 인용에 쓴다.",
        "examples": ("友だちと行きます。", "「行きたい」と言いました。"),
    },
    {
        "particle": "も",
        "reading": "mo",
        "meaning": "도",
        "note": "추가의 의미를 나타낸다.",
        "examples": ("わたしも学生です。", "これもおいしい。"),
    },
    {
        "particle": "から / まで",
        "reading": "kara / made",
        "meaning": "부터 / 까지",
        "note": "시작점과 끝점을 나타낸다.",
        "examples": ("9時から5時まで働きます。",),
    },
    {
        "particle": "ね / よ",
        "reading": "ne / yo",
        "meaning": "공감·확인 / 정보 전달",
        "note": "ね는 그쵸? 맞죠? 느낌, よ는 알려줄게/강하게 말함.",
        "examples": ("いい天気ですね。", "これ、おいしいですよ。"),
    },
)

BEGINNER_PATTERNS: tuple[str, ...] = (
    "わたしは ○○です.",
    "○○が あります/います.",
    "○○を します/食べます/見ます.",
    "○○に 行きます / ○時に.",
    "○○で.",
)


def get_kana(script: str, *, level: int | None = None) -> tuple[KanaEntry, ...]:
    normalized = script.strip().lower()
    selected_level = 3 if level is None else level
    if selected_level not in KANA_LEVEL_LABELS:
        raise ValueError("level must be 1, 2, 3, or 4")
    if selected_level == 4:
        raise ValueError("level 4 is a word meaning stage")

    if normalized == "hiragana":
        if selected_level == 1:
            return HIRAGANA
        if selected_level == 2:
            return HIRAGANA + HIRAGANA_MARKS
        return HIRAGANA + HIRAGANA_MARKS + HIRAGANA_YOON
    if normalized == "katakana":
        if selected_level == 1:
            return KATAKANA
        if selected_level == 2:
            return KATAKANA + KATAKANA_MARKS
        return KATAKANA + KATAKANA_MARKS + KATAKANA_YOON
    raise ValueError("script must be 'hiragana' or 'katakana'")


def get_kana_level_label(level: int) -> str:
    if level not in KANA_LEVEL_LABELS:
        raise ValueError("level must be 1, 2, 3, or 4")
    return KANA_LEVEL_LABELS[level]


def pair_by_romaji(*, level: int | None = None) -> dict[str, tuple[str, str]]:
    katakana_by_romaji = {romaji: symbol for symbol, romaji in get_kana("katakana", level=level)}
    return {
        romaji: (hiragana, katakana_by_romaji[romaji])
        for hiragana, romaji in get_kana("hiragana", level=level)
        if romaji in katakana_by_romaji
    }


def get_confusing_pairs(script: str) -> tuple[tuple[str, str, str], ...]:
    normalized = script.strip().lower()
    if normalized not in CONFUSING_PAIRS:
        raise ValueError("script must be 'hiragana' or 'katakana'")
    return CONFUSING_PAIRS[normalized]


def get_reading_examples(script: str) -> tuple[tuple[str, str, str, str], ...]:
    normalized = script.strip().lower()
    if normalized not in READING_EXAMPLES:
        raise ValueError("script must be 'hiragana' or 'katakana'")
    return READING_EXAMPLES[normalized]


def get_sokuon_examples(script: str) -> tuple[tuple[str, str, str, str], ...]:
    normalized = script.strip().lower()
    if normalized not in SOKUON_EXAMPLES:
        raise ValueError("script must be 'hiragana' or 'katakana'")
    return SOKUON_EXAMPLES[normalized]


def get_word_meaning_examples(script: str) -> tuple[tuple[str, str, str, str], ...]:
    normalized = script.strip().lower()
    if normalized not in WORD_MEANING_EXAMPLES:
        raise ValueError("script must be 'hiragana' or 'katakana'")
    return WORD_MEANING_EXAMPLES[normalized]


def get_particles() -> tuple[dict[str, object], ...]:
    return PARTICLES


def get_beginner_patterns() -> tuple[str, ...]:
    return BEGINNER_PATTERNS
