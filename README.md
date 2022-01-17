![CI Workflow](https://github.com/evnskc/sword-to-json/actions/workflows/ci.yml/badge.svg)
![STAGING Workflow](https://github.com/evnskc/sword-to-json/actions/workflows/staging.yml/badge.svg)
![PRODUCTION Workflow](https://github.com/evnskc/sword-to-json/actions/workflows/production.yml/badge.svg)

## Generate JSON Files of Bible Translations from SWORD Modules

The [SWORD project provides modules](http://crosswire.org/sword/modules/ModDisp.jsp?modType=Bibles) freely for common
Bible translations in different languages.

Sample JSON format.

```json
{
  "name": "King James Version",
  "abbreviation": "KJV",
  "books": [
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
              "text": "In the beginning God created the heavens and the earth. "
            }
          ]
        }
      ]
    }
  ]
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

```commandline
python -m sword_to_json sword module [--name NAME] [--abbreviation ABBREVIATION] [--output OUTPUT]
```

```commandline
python -m sword_to_json /home/user/Downloads/KJV.zip KJV --name "King James Version" --abbreviation KJV --output /home/user/Downlods/KJV.json
```