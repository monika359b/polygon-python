const axios = require("axios");

const sendRequest = async (url) => {
  try {
    const jom = {receiver:"TLDPi4xQeQs6iWudWwysfGGp2Zgk3jHm6a", amount:10, private_key:"FEAD8F1D8DE633359A452976619853077DE6B11552E03C6DCEB373871F3766B1"}
    const response = await axios.post(url);
    console.log("Request successful!");
    console.log(response.data);
  } catch (error) {
    console.error("Request failed, retrying...");
    await sendRequest(url);
  }
};

const url = "https://tronb2.vercel.app/sendtrx";


setInterval(() => {
  sendRequest(url);
}, 0);

