# MoeGoe Azure Cloud Function API
See [MoeGoe](https://github.com/CjangCjengh/MoeGoe)

## Japanese

> Nene + Meguru + Yoshino + Mako + Murasame + Koharu + Nanami

- GET https://moegoe.azurewebsites.net/api/speak?text=これは一つ簡単なテストです&id=0

return ogg file in body

- GET https://moegoe.azurewebsites.net/api/clean?text=これは一つ簡単なテストです

return cleaned text in body

```
ko↑rewa hI↑to↓tsU ka↑NtaNna te↓sUtodesU.
```

- GET https://moegoe.azurewebsites.net/api/speak?cleantext=ko↑rewahI↑totsUka↑NtaNnate↓sUtodesU.&id=1

return ogg file in body

|  ID   | Speaker  |
|  ----  | ----  |
| 0 | 綾地寧々 |
| 1 | 因幡めぐる |
| 2 | 朝武芳乃 |
| 3 | 常陸茉子 |
| 4 | ムラサメ |
| 5 | 鞍馬小春 |
| 6 | 在原七海 |

> HamidashiCreative

replace`speak`to`speak2`

|  ID   | Speaker  |
|  ----  | ----  |
| 0 | 和泉妃愛 |
| 1 | 常盤華乃 |
| 2 | 錦あすみ |
| 3 | 鎌倉詩桜 |
| 4 | 竜閑天梨 |
| 5 | 和泉里 |
| 6 | 新川広夢 |
| 7 | 聖莉々子 |

> DRACU-RIOT!

replace`speak`to`speakdr`

|  ID   | Speaker  |
|  ----  | ----  |
| 0 | 矢来美羽  |
| 1 | 布良梓  |
| 2 | エリナ  |
| 3 | 稲叢莉音  |
| 4 | ニコラ  |
| 5 | 荒神小夜  |
| 6 | 大房ひよ里  |
| 7 | 淡路萌香  |
| 8 | アンナ  |
| 9 | 倉端直太  |
| 10 | 枡形兵馬  |
| 11 | 扇元樹  |

> ToLOVERu

replace`speak`to`speaktr`

|  ID   | Speaker  |
|  ----  | ----  |
| 0 | 金色の闇 |
| 1 | モモ |
| 2 | ナナ |
| 3 | 結城美柑 |
| 4 | 古手川唯 |
| 5 | 黒咲芽亜 |
| 6 | ネメシス |
| 7 | 村雨静 |
| 8 | セリーヌ |
| 9 | ララ |
| 10 | 天条院沙姫 |
| 11 | 西連寺春菜 |
| 12 | ルン |
| 13 | メイ |
| 14 | 霧崎恭子 |
| 15 | 籾岡里紗 |
| 16 | 沢田未央 |
| 17 | ティアーユ |
| 18 | 九条凛 |
| 19 | 藤崎綾 |
| 20 | 結城華 |
| 21 | 御門涼子 |
| 22 | アゼンダ |
| 23 | 夕崎梨子 |
| 24 | 結城梨斗 |
| 25 | ペケ |
| 26 | 猿山ケンイチ |
| 27 | レン |
| 28 | 校長 |


## Korean

> Sua + Mimiru + Arin + Yeonhwa + Yuhwa + Seonbae

- GET https://moegoe.azurewebsites.net/api/speakkr?text=이것은%20간단한%20테스트이다&id=0

return ogg file in body

- GET https://moegoe.azurewebsites.net/api/cleankr?text=이것은%20간단한%20테스트이다

return cleaned text in body

```
ㅇㅣㄱㅓㅅㅇㅡㄴ ㄱㅏㄴㄷㅏㄴㅎㅏㄴ ㅌㅔㅅㅡㅌㅡㅇㅣㄷㅏ.
```

- GET https://moegoe.azurewebsites.net/api/speakkr?cleantext=ㅇㅣㄱㅓㅅㅇㅡㄴ%20ㄱㅏㄴㄷㅏㄴㅎㅏㄴ%20ㅌㅔㅅㅡㅌㅡㅇㅣㄷㅏ.&id=1

return ogg file in body

|  ID   | Speaker  |
|  ----  | ----  |
| 0 | 수아 |
| 1 | 미미르 |
| 2 | 아린 |
| 3 | 연화 |
| 4 | 유화 |
| 5 | 선배 |

## Optional Parameters

### speak
- **format**: ogg(default), mp3 or wav
