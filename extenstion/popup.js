document.getElementById('fileForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const file1 = document.getElementById('file1').files[0];
    const file2 = document.getElementById('file2').files[0];
  
    if (!file1 || !file2) {
      alert('Please select both files.');
      return;
    }
  
    const formData = new FormData();
    formData.append('file1', file1);
    formData.append('file2', file2);
  
    fetch('http://localhost:5000/upload', {
      method: 'POST',
      body: formData
    })
    .then(response => response.text())
    .then(data => {
      alert('Files uploaded successfully!');
    })
    .catch(error => {
      console.error('Error:', error);
      alert('Failed to upload files.');
    });
  });
  