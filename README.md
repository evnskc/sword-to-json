[![Test](https://github.com/evnskc/sword-to-json/actions/workflows/test.yml/badge.svg)](https://github.com/evnskc/sword-to-json/actions/workflows/test.yml)
[![Staging](https://github.com/evnskc/sword-to-json/actions/workflows/deploy-staging.yml/badge.svg)](https://github.com/evnskc/sword-to-json/actions/workflows/deploy-staging.yml)
[![Production](https://github.com/evnskc/sword-to-json/actions/workflows/deploy-production.yml/badge.svg)](https://github.com/evnskc/sword-to-json/actions/workflows/deploy-production.yml)
[![PyPI](https://img.shields.io/pypi/v/sword-to-json)](https://pypi.org/project/sword-to-json/)

## Generate JSON Files of Bible Translations from SWORD Modules

The [SWORD project provides modules](http://crosswire.org/sword/modules/ModDisp.jsp?modType=Bibles) freely for common
Bible translations in different languages.

Sample JSON format.

```json
{
  "books": {
    "ot": [
      {
        "number": 1,
        "name": "Genesis",
        "abbreviation": "Gen",
        "chapters": [
          {
            "number": 1,
            "verses": [
              {
                "number": 1,
                "text": "In the beginning God created the heaven and the earth."
              }
            ]
          }
        ]
      }
    ],
    "nt": [
      {
        "number": 40,
        "name": "Matthew",
        "abbreviation": "Matt",
        "chapters": [
          {
            "number": 1,
            "verses": [
              {
                "number": 1,
                "text": "The book of the generation of Jesus Christ, the son of David, the son of Abraham."
              }
            ]
          }
        ]
      }
    ]
  }
}
```

## Installation

1. Using ```pip```

```commandline
pip install sword-to-json
```

2. Using ```poetry```

```commandline
poetry add sword-to-json
```

## Usage

```text
sword-to-json sword module [--output OUTPUT]
```

```commandline
sword-to-json /home/user/Downloads/KJV.zip KJV --output /home/user/Downlods/KJV.json
```