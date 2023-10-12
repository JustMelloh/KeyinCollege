var number = 28;

function isPerfectNumber(number) {
    var sum = 0;
    for (var i = 1; i < number; i++) {
        if (number % i === 0) {
            sum += i;
        }
    }
    return sum === number;
}

if (isPerfectNumber(number)) {
    console.log(number + ' is a perfect number.');
} else {
    console.log(number + ' is not a perfect number.');
}