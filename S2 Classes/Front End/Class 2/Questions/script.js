    // /// Question 1

    //
    // var r = 5;

    // var a = Math.PI * r * r;

    // console.log("Area of Circle: "+ a);

    // /// Question 2

    // function roll(sides = 6) {
    //     const result = Math.floor(Math.random() * sides) + 1;
    //     return result;
    // }

    // const result1 = roll();
    // const result2 = roll(21);

    // console.log("Roll 1: ", result1);
    // console.log("Roll 2: ", result2);

    // Question 3

    //    function convertToCelcius(fahrenheit) {
    //        var celsius = (fahrenheit - 32) * (5/9);
    //        return celsius;
    //    }

    //    var fahrenheit = 32;
    //    var celsius = convertToCelcius(fahrenheit);
    //    console.log(fahrenheit + " F is " + celsius + "C");
        
    //Question 4

    // function convert(value, scale) {
    //   if (scale === "F") {
    //        var celsius = (value - 32) * (5/9);
    //        return celsius.toFixed(2) + "C";
    
    //  } else if (scale === "C") {
    //        var fahrenheit = (value)
    //        return fahrenheit.toFixed(2) + "F";

    //        } else {
    //        return "Invalid scale."
    //    }
    // }

    // var temperature = 30;
    // var scale = "F"
    // var result = convert(temperature, scale)
    // console.log(result)

    //Question 5

//     function isUnder(){
//         for (var i = 0; i < arguments.length; i++) {
//             if (arguments[i] >= 50) {
//                 return false;
//             }
    
//     }
//     return true;
// }
// var result = isUnder(1, 2, 4, 6, 30, 40, 30) ;
// console.log(result)

    // Question 6

    // function sumValue(...numbers) {
    //     return numbers.reduce((total, num) => total + num, 0)
        

    // }

    // console.log(sumValue(1,2,3));
        
    
    // Question 7

    // function multipleThree(number) {
    //     return number % 3 === 0;
    // }

    // console.log(multipleThree(9));
    // console.log(multipleThree(7));