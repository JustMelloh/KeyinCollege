var number = 17; 

function isPrime(number) {
    if (number <= 1) {
        return false;
    }
    for (var i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) {
            return false;
        }
    }
    return true;
}

if (isPrime(number)) {
    console.log(number + ' is a prime number.');
} else {
    console.log(number + ' is not a prime number.');
}