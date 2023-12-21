document.addEventListener("DOMContentLoaded", function () {
	var aboutBtn1 = document.getElementById("aboutBtn1");
	var aboutBox1Text = document.querySelector(".aboutBox1-text");

	var aboutBtn2 = document.getElementById("aboutbtn2");
	var aboutBox2Text = document.querySelector(".aboutBox2-text");

	aboutBtn1.addEventListener("click", function () {
		// Toggle the display of aboutBox1 text when the button is clicked
		aboutBox1Text.style.display =
			aboutBox1Text.style.display === "none" ||
			aboutBox1Text.style.display === ""
				? "block"
				: "none";
	});

	aboutBtn2.addEventListener("click", function () {
		// Toggle the display of aboutBox2 text when the button is clicked
		aboutBox2Text.style.display =
			aboutBox2Text.style.display === "none" ||
			aboutBox2Text.style.display === ""
				? "block"
				: "none";
	});
});
