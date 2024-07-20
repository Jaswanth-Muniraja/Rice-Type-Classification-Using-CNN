// function previewImage() {
//     var preview = document.getElementById('preview-image');
//     var file = document.getElementById('image-input').files[0];
//     var reader = new FileReader();

//     reader.onloadend = function () {
//         preview.src = reader.result;
//         preview.style.display = 'block';
//     }

//     if (file) {
//         reader.readAsDataURL(file);
//     } else {
//         preview.src = '';
//         preview.style.display = 'none';
//     }
// }

// function classifyRice() {
//     var imageInput = document.getElementById('image-input');
//     var file = imageInput.files[0];

//     if (file) {
//         var formData = new FormData();
//         formData.append('image', file);

//         fetch('/classify', {
//             method: 'POST',
//             body: formData
//         })
//         .then(response => response.json())
//         .then(data => {
//             document.getElementById('rice-type').textContent = data.rice_type;
//             document.getElementById('result-container').style.display = 'block';
//         })
//         .catch(error => {
//             console.error('Error:', error);
//         });
//     } else {
//         alert('Please select an image to classify.');
//     }
// }