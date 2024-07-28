// Load environment variables from .env file
require("dotenv").config();
const { OpenAIApi, Configuration } = require("openai");

// Initialize OpenAI API client
const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

// Function to generate text using OpenAI API
async function generateText(prompt) {
  try {
    const response = await openai.createCompletion({
      model: "text-davinci-003", // You can change the model as needed
      prompt: prompt,
      max_tokens: 50,
    });
    return response.data.choices[0].text.trim();
  } catch (error) {
    console.error("Error generating text:", error);
    return null;
  }
}

// Example usage
const prompt = "Once upon a time";
generateText(prompt).then((generatedText) => {
  console.log("Generated Text:", generatedText);
});
