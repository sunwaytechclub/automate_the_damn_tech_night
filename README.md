# Automate The Damn Tech Night 😡

> _No more hassles on publishing it! 🥳_

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## 🤨 About <a name = "about"></a>

The steps are usually:

1. Getting the speaker profile and image
2. Generate the poster
3. Make the write-up
4. Post it in our Telegram, Facebook, Instagram
5. Sending emails for further marketing channels
6. \*Share the post to specific Facebook groups

It will usually take up much time for each step: because I am lazy!

So... let's automate it!

## 🤩 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Not yet written
```

### Installing

A step by step series of examples that tell you how to get a development env running.

```
Not yet written
```

Finally there will be an example output :P

## 🔨 Usage <a name = "usage"></a>

### Back-end

- [Create new speaker](#createnewspeaker)
- [Create new event](#createnewevent)

#### Create new speaker <a name = "createnewspeaker"></a>

##### Request

URL: `/api/v1/speaker/`

Method: `POST`

Content Type: `multipart/form-data`

body:

```bash
name=<speaker name>
position=<speaker desired display experiences>
avatar=<speaker profile picture>
```

##### Response

```json
{
  "id": 4,
  "name": "Rain Chai",
  "position": "Head of Marketing",
  "avatar": "http://localhost:8000/media/speakers/Rain_chai.png"
}
```

---

#### Create new event <a name = "createnewevent"></a>

##### Request

URL: `/api/v1/event/`

Method: `POST`

Content Type: `application/json`

body:

```json
{
  "episode": 3,
  "datetime": "2021-02-01T09:22:43Z",
  "topic": [
    {
      "speaker": 4,
      "title": "hehehe",
      "hook": "How I wish there's a way to manage Telegram chat automatically... 🤔",
      "why": "huhuhu",
      "what": "hohohoh"
    }
  ]
}
```

##### Response

```json
{
  "id": 9,
  "episode": 3,
  "datetime": "2021-02-01T09:22:43Z",
  "poster": "/media/poster/event/3_DT74pxb.jpg",
  "topic": [
    {
      "id": 9,
      "speaker": {
        "id": 4,
        "name": "Rain Chai",
        "position": "head of marketing",
        "avatar": "/media/speakers/Group_99_iPRATzI.png"
      },
      "hook": "How I wish there's a way to manage Telegram chat automatically... 🤔",
      "title": "hehehe",
      "why": "huhuhu",
      "what": "hohohoh",
      "poster": "/media/poster/speaker/3-Rain_Chai.jpg"
    }
  ]
}
```

## 📝 Todo <a name = "todo"></a>

- [x] Generate poster with event and speaker details
- [ ] Automate social media posting
- [ ] Automate emailing to departments
