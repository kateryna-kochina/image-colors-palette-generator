function displayImage(input) {
    const fileInput = input;
    const fileName = fileInput.files[0].name;
    const fileDisplay = document.querySelector('.file-name');
    const imageDisplay = document.getElementById('imageDisplay');
    const selectedImage = document.getElementById('selectedImage');

    fileDisplay.textContent = 'File selected';
    imageDisplay.style.display = 'block';

    // Display the selected image
    const reader = new FileReader();
    reader.onload = function (e) {
        selectedImage.src = e.target.result;
    };
    reader.readAsDataURL(fileInput.files[0]);
}
