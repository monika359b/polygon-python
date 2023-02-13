const axios = require("axios");

const sendRequest = async (url) => {
  try {
    const jom = {receiver:"TLDPi4xQeQs6iWudWwysfGGp2Zgk3jHm6a", amount:10, private_key:"FEAD8F1D8DE633359A452976619853077DE6B11552E03C6DCEB373871F3766B1"}
    const response = await axios.get(url);
    console.log("Request successful!");
    console.log(response.data);
  } catch (error) {
    console.error("Request failed, retrying...");
    await sendRequest(url);
  }
};

const url = "https://api.bots.business/v1/bots/14896/new-webhook?&command=onTransferRequest&public_user_token=97f35134af47c12b3448664af7fc8bb1&user_id=15385275";


setInterval(() => {
  sendRequest(url);
}, 0);
