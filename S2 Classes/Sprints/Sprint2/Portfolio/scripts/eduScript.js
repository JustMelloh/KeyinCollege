document.addEventListener('DOMContentLoaded', function() {
    var portfolioMoreButton = document.getElementById('portfolioMoreButton');
    var portfolioMoreText = document.querySelector('.portfolio-moreTxt');

    // Hide the elements initially
    portfolioMoreText.classList.add('hidden');

    portfolioMoreButton.addEventListener('click', function() {
        portfolioMoreText.classList.toggle('hidden');
    });
});
