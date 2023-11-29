// JS for Dog API


// Fetch Dog API
document.addEventListener("DOMContentLoaded", () => {
  fetch("https://dog.ceo/api/breeds/list/all")
    .then((response) => response.json())
    .then((data) => {
      const breeds = Object.keys(data.message);
      const selectElement = document.getElementById("breed-list");


      // Get Dog Breeds

      breeds.forEach((breed) => {
        const option = document.createElement("option");
        option.value = breed;
        option.text = breed;
        selectElement.appendChild(option);
      });
    })
    .catch((error) => {
      console.error("Error Fetching Breeds - ", error);
    });

  document
    .getElementById("dog-form")
    .addEventListener("submit", function (event) {
      event.preventDefault();
    // Breed and #Photos 
      const selectedBreed = document.getElementById("breed-list").value;
      const numOfPhotos = document.getElementById("number").value;

      fetch(
        `https://dog.ceo/api/breed/${selectedBreed}/images/random/${numOfPhotos}`
      )
        .then((response) => response.json())
        .then((data) => {
            // List Images through "image-container"
          const images = data.message;
          const imageContainer = document.getElementById("image-container");

          imageContainer.innerHTML = "";

          images.forEach((image) => {
            const imgElement = document.createElement("img");
            imgElement.src = image;
            imgElement.alt = selectedBreed;
            imageContainer.appendChild(imgElement);
          });
        })
        .catch((error) => {
          console.error("Error Fetching Images - ", error);
        });
    });
});
