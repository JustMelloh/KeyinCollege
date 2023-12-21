document.addEventListener('DOMContentLoaded', function() {
    var portfolioButton = document.getElementById('portfolioButton');
    var portfolioText = document.querySelector('.portfolio-text');
    var portfolioMoreButton = document.getElementById('portfolioMoreButton');
    var portfolioMoreText = document.querySelector('.portfolio-moreTxt');

    // Hide the elements initially
    portfolioText.classList.add('hidden');
    portfolioMoreText.classList.add('hidden');

    portfolioButton.addEventListener('click', function() {
        portfolioText.classList.toggle('hidden');
    });

    portfolioMoreButton.addEventListener('click', function() {
        portfolioMoreText.classList.toggle('hidden');
    });
});