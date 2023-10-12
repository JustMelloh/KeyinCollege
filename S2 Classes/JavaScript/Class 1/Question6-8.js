var table = 15;
for(var i = 1;i <=10;i++) {
    var resure = table * i;
    
    console.log(table + "X" + i + "=" + result);
}

for (var i = 1; i <= 100; i++) {
    if (i % 2 === 0) {
        console.log(i + ' is even');
    } else {
        console.log(i + ' is odd');
    }
}

var sumOfEven = 0;

for (var i = 1; i <= 100; i++) {
    if (i % 2 === 0) {
        sumOfEven += i;
    }
}

console.log('Sum of all even numbers from 1 to 100 is: ' + sumOfEven);