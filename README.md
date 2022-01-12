![CI Workflow](https://github.com/evnskc/sword-to-json/actions/workflows/ci.yml/badge.svg)

![STAGING Workflow](https://github.com/evnskc/sword-to-json/actions/workflows/staging.yml/badge.svg)

![CI Workflow](https://github.com/evnskc/sword-to-json/actions/workflows/production.yml/badge.svg)

## Generate JSON Files of Bible Translations from SWORD Modules

The [SWORD project provides modules](http://crosswire.org/sword/modules/ModDisp.jsp?modType=Bibles) freely for common
Bible translations in different languages.

Sample JSON format.

```
{
  "name": "King James Version",
  "abbreviation": "KJV",
  "books": [
    {
      "name": "Genesis",
      "abbreviation": "Gen",
      "chapters": [
        {
          "number": 1,
          "verses": [
            {
              "number": 1,
              "text": "In the beginning God created the heavens and the earth. "
            },
            
            ...
          ]
        },
        
        ...
      ]
    }
  ]
}

```