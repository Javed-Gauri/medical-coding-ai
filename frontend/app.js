async function predictCodes() {
  const notes = document.getElementById('clinicalNotes').value;
  const response = await fetch('YOUR_CLOUD_RUN_URL/predict', {
    method: 'POST',
    body: JSON.stringify({ text: notes })
  });
  document.getElementById('results').innerHTML = await response.text();
}
