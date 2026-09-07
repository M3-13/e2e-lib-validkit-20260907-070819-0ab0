# validkit

Eine kleine, eigenständige Python-Bibliothek mit neun voneinander unabhängigen,
reinen Prüf- und Normalisierungsfunktionen: `is_valid_email`, `luhn_check`,
`is_valid_iban`, `is_valid_isbn13`, `normalize_phone`, `strip_accents`,
`mask_secret`, `slugify` und `clamp`. Alle Funktionen sind sauber typannotiert,
melden ungültige Eingaben mit aussagekräftigen Fehlern und kommen ohne externe
Abhängigkeiten, CLI, UI oder Netzwerkzugriff aus — es wird ausschließlich die
Python-Standardbibliothek verwendet.

## Tech-Stack

- **Sprache**: Python (≥ 3.9)
- **Framework**: keins (reine Bibliothek)
- **Testing**: pytest
- **Build**: `pyproject.toml` mit setuptools
- **Laufzeitabhängigkeiten**: keine (nur Standardbibliothek)

## Installation

```bash
pip install -e .
```

## Tests ausführen

```bash
pytest
```

## Verwendung

```python
from validkit import (
    is_valid_email,
    luhn_check,
    is_valid_iban,
    is_valid_isbn13,
    normalize_phone,
    strip_accents,
    mask_secret,
    slugify,
    clamp,
)
```

Für jede der neun Funktionen gibt es genau ein Beispiel mit Eingabe und
erwarteter Ausgabe.

### `is_valid_email(text: str) -> bool`

Prüft, ob ein Text eine syntaktisch gültige E-Mail-Adresse ist.

```python
is_valid_email("user@example.com")
# -> True
```

### `luhn_check(digits: str) -> bool`

Validiert eine Ziffernfolge anhand des Luhn-Algorithmus.

```python
luhn_check("79927398713")
# -> True
```

### `is_valid_iban(text: str) -> bool`

Prüft eine IBAN (Modulo-97-Rest 1, Leerzeichen werden toleriert).

```python
is_valid_iban("DE89370400440532013000")
# -> True
```

### `is_valid_isbn13(text: str) -> bool`

Prüft eine ISBN-13 (Bindestriche/Leerzeichen werden toleriert).

```python
is_valid_isbn13("978-3-16-148410-0")
# -> True
```

### `normalize_phone(text: str, country_code: str) -> str`

Normalisiert eine Telefonnummer auf das E.164-Format.

```python
normalize_phone("+49 170 1234567", "DE")
# -> "+491701234567"
```

### `strip_accents(text: str) -> str`

Entfernt diakritische Zeichen.

```python
strip_accents("café")
# -> "cafe"
```

### `mask_secret(text: str, keep: int = 4) -> str`

Maskiert einen Text und lässt die letzten `keep` Zeichen sichtbar.

```python
mask_secret("geheimnis", keep=4)
# -> "*****nnis"
```

### `slugify(text: str) -> str`

Erzeugt aus einem Text einen URL-tauglichen Slug.

```python
slugify("Héllo Wörld!")
# -> "hello-world"
```

### `clamp(value, low, high) -> float | int`

Hält einen Wert innerhalb des Intervalls `[low, high]`.

```python
clamp(15, 0, 10)
# -> 10
```

## Fehlerkonvention

- Falscher Typ → `TypeError`.
- Unpassender Wert → `ValueError`.
- Die bool-Funktionen (`is_valid_email`, `luhn_check`, `is_valid_iban`,
  `is_valid_isbn13`) liefern bei gültigem `str`-Typ, aber inhaltlich ungültiger
  Eingabe `False` statt `ValueError`.
- Regex-Funktionen (`is_valid_email`, `normalize_phone`, `slugify`) prüfen vor
  der Regex `len(text) <= 10000`, sonst `ValueError`.

## Funktionsübersicht

| Funktion | Beschreibung |
| --- | --- |
| `is_valid_email` | E-Mail-Validierung |
| `luhn_check` | Luhn-Prüfziffer-Validierung |
| `is_valid_iban` | IBAN-Validierung |
| `is_valid_isbn13` | ISBN-13-Validierung |
| `normalize_phone` | Telefonnummer-Normalisierung (E.164) |
| `strip_accents` | Diakritika entfernen |
| `mask_secret` | Geheimnisse maskieren |
| `slugify` | Slug-Erzeugung |
| `clamp` | Wert auf Intervall begrenzen |
