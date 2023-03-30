// Detect phishing website button
const detectButton = document.getElementById('detect-button');

// Event listener for the detect phishing website button
detectButton.addEventListener('click', detectPhishingWebsite);

// Function to detect phishing website
function detectPhishingWebsite() {
  // Show the loading gif
  const loadingGif = document.getElementById('loading-gif');
  loadingGif.style.display = 'block';

  // Send a POST request to the Flask API with the URL and HTML of the current tab
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    const url = tabs[0].url;
    const tabId = tabs[0].id;
    chrome.tabs.executeScript(tabId, { code: 'document.body.innerHTML' }, function (result) {
      const html = result[0];
      const data = { url: url, html: html };
      fetch('http://127.0.0.1:5000/detect', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
        .then(response => response.json())
        .then(data => {
          // Hide the loading gif
          loadingGif.style.display = 'none';

          // Display the result in the popup
          const resultElement = document.getElementById('result');
          console.log(data)
          if (data.prediction == 1) {
            resultElement.innerText = 'This website is safe.';
          } else {
            resultElement.innerText = 'This website may be a phishing website.';
          }
        })
        .catch(error => {
          console.error(error);
        });
    });
  });
}
