document.getElementById("prompt-form").addEventListener("submit", function(event) {
  event.preventDefault();

  const to = document.getElementById("to").value;
  const tone = document.getElementById("tone").value;
  const reason1 = document.getElementById("reason-1").value;
  const reason2 = document.getElementById("reason-2").value;
  const reason3 = document.getElementById("reason-3").value;
  const additionalContext = document.getElementById("additional-context").value;
  const intendedResult = document.getElementById("intended-result").value;

  // Use the input values to generate the email
  fetch("https://api.openai.com/v1/text-davinci/generate", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${api_key}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      prompt: `Please write a ${tone} email to ${to} about ${reason1} and ${reason2} and ${reason3}. Here is some extra context: ${additionalContext}. I hope to achieve ${intendedResult} with this email.`,
      max_tokens: 2048,
    }),
  })
  .then(response => response.json())
  .then(result => {
    console.log(result["text"]);
  });
});