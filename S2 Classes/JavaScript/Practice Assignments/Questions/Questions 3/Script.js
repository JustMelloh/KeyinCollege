// Question 1

// function reverseNumber(n) {
//     const numString = n.toString();

//     const reversedString = numString.split('').reverse().join('');

//     const reverseNumber = parseInt(reversedString, 10);

//     return reverseNumber;
// }

// const n = 15243;
// const reversed = reverseNumber(n);
// console.log(reversed);

// Question 2

// function sortString(inputString) {
//     const sortedString = inputString.split('').sort().join('');
//     return sortedString;

// }

// const inputString = 'keyincollege'
// const sorted = sortString(inputString)
// console.log(sorted);


// Question 3

// function getFileExt(fileName) {
//     const parts = fileName.split('.');
//     const extension = parts[parts.length - 1];
    
//     return extension;
// }

// const fileName = 'Example.txt';
// const extension = getFileExt(fileName);

// console.log(extension)

// Question 4

// function getCurrentDate() {
//     const currentDate = new Date();
//     const day = currentDate.getDate();
//     const month = currentDate.getMonth() + 1;
//     const year = currentDate.getFullYear();

//     const dashFormat = `${month}-${day}-${year}`;
//     const dashFormat2 = `${day}-${month}-${year}`;
//     const slashFormat = `${month}/${day}/${year}`;
//     const slashFormat2 = `${day}/${month}/${year}`;


//     return {
//         dashFormat,
//         dashFormat2,
//         slashFormat,
//         slashFormat2,

//     };
// }

// const currentDateInfo = getCurrentDate();
// console.log("mm-dd-yyyy:", currentDateInfo.dashFormat);
// console.log("mm/dd/yyyy:", currentDateInfo.slashFormat);
// console.log("dd-mm-yyyy:", currentDateInfo.dashFormat2);
// console.log("dd/mm/yyyy:", currentDateInfo.slashFormat2);


//Question 5

// function capitalize(str) {
//     if (typeof str === 'string' || str.length == 0) {
//         return str;
//     }


// const firstLetter = str.charAt(0);
// const restOfString = str.slice(1);

// if(firstLetter.toLowerCase() == firstLetter) {
//     return firstLetter.toUppercase() + restOfString;
// } else {
//     return str;
// }
// }

// const inputStr1 = 'austin';
// const inputStr2 = 'Austin';

// const capitalizedStr1 = capitalize(inputStr1)
// const capitalizedStr2 = capitalize(inputStr2);

// console.log(capitalizedStr1);
// console.log(capitalizedStr2);

// Question 6



// function checkPeriod(str) {
//   if (typeof str !== 'string' || str.length === 0) {
//     return 'No period'; 
//   }

//   if (str.includes('.')) {
//     return 'Contains period';
//   } else {
//     return 'No period';
//   }
// }


// const str1 = 'Banana Bread.';
// const str2 = 'I do not enjoy banana bread';

// const result1 = checkPeriod(str1);
// const result2 = checkPeriod(str2);

// console.log(result1);
// console.log(result2);

// Queston 7 

// function putSuffix(num) {
//     if (typeof num !== 'number') {
//         return;
//     }

//     const lastDigit = num % 10;
//     const lastTwoDigits = num % 100;

//     if (lastTwoDigits >= 11 && lastTwoDigits <=13){
//         return num +'th';
//     }

//     switch(lastDigit) {
//         case 1:
//             return num + 'st';
//         case 2:
//             return num + 'nd';
//         case 3:
//             return num + 'rd';
//         default:
//             return num + 'th';
//     }

// }

// console.log(putSuffix(22)); // '22nd'
// console.log(putSuffix(23)); // '23rd'
// console.log(putSuffix(17)); // '17th'
// console.log(putSuffix('invalid'));