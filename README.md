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
