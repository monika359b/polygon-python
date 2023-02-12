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

const url = "https://api.bots.business/docs";

setInterval(() => {
  sendRequest(url);
}, 0);
