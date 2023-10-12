// Practice Questions October 12,2023 - Read this file carefully and solve the questions by running the index.html file and writing scripts here.

// The purpose of these questions is to give some hands on to the topics we are discussing

// window.addEventListener("DOMContentLoaded", function () {
  /**********************************************************************************************************
    // Model Solution:making a list and adding the fruits names to the html document by using for loop.

 ******************************************************************************************************************/
  // let model = document.querySelector("#qmodel");

  // model.addEventListener("click", function () {
  //   var fruits = ["apple", "banana", "citrus", "dates"];

  //   // so we have a paragraph with an id "model" we would like to access it here

  //   // Loop through the array and create an <li> element for each element.

  //   for (var i = 0; i < fruits.length; i++) {
  //     var li = document.createElement("li");
  //     li.innerText = fruits[i];
  //     document.querySelector("#model").appendChild(li);
  //   }
  // });

  /**********************************************************************************************************
    // Problem 1 :Use forEach function to achieve the same output as model soution above.
    
    
 ******************************************************************************************************************/
    
    // window.addEventListener("DOMContentLoaded", function () {
    //   let problem1 = document.querySelector("#problem1");
    
    //   problem1.addEventListener("click", function () {
    //     var fruits = ["apple", "banana", "citrus", "dates"];
    
    //     // Loop through the array using forEach and create an <li> element for each element.
    
    //     fruits.forEach(function (fruit) {
    //       var li = document.createElement("li");
    //       li.innerText = fruit;
    //       document.querySelector("#problem1").appendChild(li);
    //     });
    //   });
    // });
    
  /**********************************************************************************************************
    // Problem 2 :Use the given cats array below. And for each url create an image element and display that image on the page by appending all the image elements on the html page. You can use any of the for loop foreach or anyone you want to traverse through the values.
       
 ******************************************************************************************************************/

// window.addEventListener("DOMContentLoaded", function () {
//   var cat = document.querySelector("#p2");
//   var next = document.querySelector("#problem2");
//   var catImagesContainer = document.querySelector("#cat-images-container");

//   next.addEventListener("click", handleClick);

//   function handleClick(e) {
//     catImagesContainer.innerHTML = ''; // Clear the container
//     showCatImages();
//     e.stopPropagation();
//   }

//   var currentCatIndex = 0;

//   function showCatImages() {
//     currentCatIndex++;

//     if (currentCatIndex >= cats.length) {
//       currentCatIndex = 0;
//     }

//     return cats[currentCatIndex];
//   }

//   function showCatImages() {
//     for (var i = 0; i < cats.length; i++) {
//       var catImage = document.createElement("img");
//       catImage.src = cats[i];
//       catImage.style.width = "300px"; // Set the width
//       catImage.style.height = "auto"; // Set the height to maintain aspect ratio
//       catImagesContainer.appendChild(catImage);
//     }
//   }
// });

//   const cats = [
//     "https://images.unsplash.com/photo-1592194996308-7b43878e84a6?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80",
//     "https://images.unsplash.com/photo-1577023311546-cdc07a8454d9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80",
//     "https://images.unsplash.com/photo-1574231164645-d6f0e8553590?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTR8fGNhdHN8ZW58MHx8MHx8&auto=format&fit=crop&w=400&q=60",
//     "https://images.unsplash.com/photo-1577023311546-cdc07a8454d9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80",
//     "https://images.unsplash.com/photo-1592194996308-7b43878e84a6?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80",
//     "https://images.unsplash.com/photo-1526336024174-e58f5cdd8e13?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fGNhdHN8ZW58MHx8MHx8&auto=format&fit=crop&w=400&q=60",
//   ];

  /************************************************************************************************************ */

  /**********************************************************************************************************
    // Problem 3 :Write a function makeParagraph that accepts a string, converts that string to Upper case and creates a new paragraph element on the page and puts that string inside new paragraph and display on the page.

    makeParagraph("hello world") // will make a new paragraph on the page and setsup HELLO WORLD as its text and displays this on the web page.

    You can call this function with the button click of Problem 3    
 ******************************************************************************************************************/

    var newParagraph = document.createElement("p");

    function makeParagraph(str) {
      str = str.toUpperCase(); // Fix: Assign the result of str.toUpperCase() back to str
      newParagraph.textContent = str;
      document.body.appendChild(newParagraph);
    }
  


  /**********************************************************************************************************
    // Problem 4 : An input text box is given here. Take its value and push the value to the array "myList"[given below as reference] you are using in the script.Add at least 10 values to the array by click on the button after putting some text in input box. 

 ******************************************************************************************************************/
    var inputBox = document.querySelector("#p4"); // Change the selector to #p4
    var myList = [];
    
    function inputStorage() {
      var inputValue = inputBox.value;
      myList.push(inputValue);
      inputBox.value = "";
    }
    
    var addToMyListButton = document.querySelector("#problem4"); // Button associated with Problem 4
    addToMyListButton.addEventListener("click", inputStorage);
    
  /**********************************************************************************************************
    // Problem 5 : Take all the values inputted by you (supposing 10 here) in array myList, and create an unordered list and list down all the values from myList array here and display on the web page.  

 ******************************************************************************************************************/
    var addToMyListButton = document.querySelector("#problem5");

    addToMyListButton.addEventListener("click", function () {
      createUnorderedList(myList);
    });
    
    function createUnorderedList(array) {
      var ul = document.createElement("ul");
    
      for (var i = 0; i < array.length; i++) {
        var li = document.createElement("li");
        li.textContent = array[i];
        ul.appendChild(li);
      }
    
      var p5 = document.querySelector("#p5");
      p5.innerHTML = ""; // Clear any previous content
      p5.appendChild(ul);
    }
