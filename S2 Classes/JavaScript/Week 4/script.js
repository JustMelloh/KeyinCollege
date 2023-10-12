var csvData = `01321,Alan Smith,519-123-4567,62 inches
01322        ,        James      Lee,     2261234567, 149 cm
01323,                      Kim Thomas       ,5321234567,138cm`;


// Clean the above data and make it look like normal data.
/*

var data = `01321,Alan Smith,519-123-4567,62 inches
            01322,James Lee,226-123-4567,56 inches
            01323,Kim Thomas,532-123-4567,60 inches`;


*/

// 1. Split the string into an array of seperate rows (i.e an array with rows seperated by \n)
// 2. Each row contains information of a user: ID, Name, Phone Number and height, all seperated by commas...
// Split each row into an array with all different fields ... You need to deal with extra and/or no whitespace.




function splitIntoRows(s) {
    return s.split(/\r?\n/);
}

function rowToFields(row) {
    return row.split("/\s*,\s*/");

}

function processCSV(csv){
    //Step 1: Break the CSV into rows.


    let rows = splitIntoRows(csv);

   //Step 2: Split all rows into array of fields...
    //let data = []
    // for(let i = 0; i < rows.length;i++) {
    //     let row = rows[i];
    //     let fields = rowToFields(row);
    //     //console.log(fields);
    //     data.push(fields);
    // }
    // return rows;
    //}

    // for(let row of rows) {
//     let fields = rowToFields(row);
//     data.push(fields);
// }

let data = rows.map((row) => rowToFields(row));

 
console.log(data);
}

var processed = processCSV(csvData);