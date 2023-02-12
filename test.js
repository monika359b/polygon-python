const axios = require("axios");

const sendRequest = async (url) => {
  try {
    const response = await axios.get(url);
    console.log("Request successful!");
    console.log(response.data);
  } catch (error) {
    console.error("Request failed, retrying...");
    await sendRequest(url);
  }
};

const url = "https://app.bots.business/build/main.js";

setInterval(() => {
  sendRequest(url);
}, 0);
