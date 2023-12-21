document.addEventListener('DOMContentLoaded', function () {
    // Add a click event listener to the button
    var educationMoreButton = document.getElementById('educationMoreButton');
    var educationMoreTxt = document.querySelector('.education-moreTxt');

    educationMoreButton.addEventListener('click', function () {
        // Toggle the display of education details when the button is clicked
        if (educationMoreTxt.style.display === 'none' || educationMoreTxt.style.display === '') {
            educationMoreTxt.style.display = 'block';
        } else {
            educationMoreTxt.style.display = 'none';
        }
    });
});