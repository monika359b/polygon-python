const axios = require("axios").default;

async function start() {
  try {
    const response = await axios.get("https://tronb2.vercel.app");
    console.log("Request successful!");
    console.log(response.data);
    await main();
  } catch (error) {
    console.error("Request failed, retrying..."+error);
    await main();
  }
};

async function main() {
start();
};
main();
