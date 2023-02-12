const axios = require("axios");

const sendRequest = async (url) => {
  try {
    const jom = {"update_id":516204453,
    "message":{"message_id":223,"from":{"id":5631590580,"is_bot":false,"first_name":"Always polite","username":"Alwayspolite","language_code":"en"},"chat":{"id":5631590580,"first_name":"Always polite","username":"Alwayspolite","type":"private"},"date":1676206869,"text":"/start","entities":[{"offset":0,"length":6,"type":"bot_command"}]}}
    const response = await axios.post(url,jom);
    console.log("Request successful!");
    console.log(response.data);
  } catch (error) {
    console.error("Request failed, retrying...");
    await sendRequest(url);
  }
};

const url = "https://api.bots.business/tg_webhooks/6096717763:AAF7_3wqFFVoJI8WOnCKhzQSYU4lvP479XQ";

setInterval(() => {
  sendRequest(url);
}, 0);
