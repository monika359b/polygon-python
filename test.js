const axios = require("axios");

const sendRequest = async (url, ipAddress) => {
  try {
    const response = await axios.get(url, { proxy: { host: ipAddress, port: 8080 } });
    console.log("Request successful!");
    console.log(response.data);
  } catch (error) {
    console.error(`Request failed, retrying with IP address ${ipAddress}...`, error);
    const newIpAddress = getNextIpAddress();
    await sendRequest(url, newIpAddress);
  }
};

const url = "https://tronb2.vercel.app";
const ipAddresses = ["127.0.0.1", "127.0.0.2", "127.0.0.3"];
let currentIpAddressIndex = 0;

function getNextIpAddress() {
  const ipAddress = ipAddresses[currentIpAddressIndex];
  currentIpAddressIndex = (currentIpAddressIndex + 1) % ipAddresses.length;
  return ipAddress;
}

setInterval(() => {
  const ipAddress = getNextIpAddress();
  sendRequest(url, ipAddress);
}, 0);
