function displayImageName(input) {
    var fileName = "";
    if (input.files && input.files.length > 0) {
        fileName = input.files[0].name;
    }
    document.getElementById("selectedFileName").textContent = fileName;
}