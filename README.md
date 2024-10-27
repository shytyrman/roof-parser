# Parser for [krisha.kz](https://krisha.kz/)

## How to use?
### Install with Git
```bash
git clone https://github.com/shytyrman/roof-parser
```

### Install [uv](https://github.com/astral-sh/uv) package manager

```bash
pip install uv
```

### Run the code

```bash
uv run ./src/shell.py
```

### Specify your commands in the shell

```bash
mycli> parse https://krisha.kz/prodazha/kvartiry/astana/?page= 10
```

### Open the csv file the script parsed


```bash
Ссылка,Комнаты,Кв. метрыАдрес,Цена,Цена за кв.м

krisha.kz/a/show/697935482,1-комнатная квартира,40,"Нура р-н, Чингиза Айтматова 77",21 500 000 〒,537500.00

krisha.kz/a/show/697742243,1-комнатная квартира,38,"Есильский р-н, Альфараби 30",23 000 000 〒,605263.16

krisha.kz/a/show/697314598,1-комнатная квартира,35,"Есильский р-н, Хусейн бен талал 39/1 — Больница (УДП) Управления делами президента.",18 400 000 〒,525714.29
...
```