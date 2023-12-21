document.addEventListener("DOMContentLoaded", function() {
    var aboutBtn1 = document.getElementById('aboutBtn1');
    var projectBox1 = document.querySelector('.project-box');

    aboutBtn1.addEventListener("click", function () {
        projectBox1.style.display =
            projectBox1.style.display === "none" ||
            projectBox1.style.display === ""
                ? "block"
                : "none";
    });
});

