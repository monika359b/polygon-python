const axios = require("axios");
const https = require("https");

const sendRequest = async (url) => {
  try {
    const options = {
      url: 'https://botsnow.tech/register.php',
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
      },
      maxRedirects: 0,
      httpsAgent: new https.Agent({
        rejectUnauthorized: false
      })
    };
    const response = await axios(options);
    console.log("Request successful!");
    console.log(response.data);
  } catch (error) {
    console.error("Request failed, retrying..."+error);
    await sendRequest(url);
  }
};

const url = "https://botsnow.tech/register.php";

const startSendingRequests = () => {
  let requestCount = 0;
  const interval = setInterval(() => {
    sendRequest(url);
    requestCount++;
    if (requestCount >= 1) { // Wait for 5 minutes (300000 milliseconds) after 20k requests
      clearInterval(interval);
      console.log(`Sent ${requestCount} requests, waiting for 5 minutes...`);
      requestCount = 0;
      setTimeout(() => {
        startSendingRequests();
      }, 3000000); // Wait for 5 minutes before resuming requests
    }
  }, 0);
};

startSendingRequests();
