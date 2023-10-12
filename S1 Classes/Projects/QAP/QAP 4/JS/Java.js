class MotelCustomer {
  constructor(name, birthDate, gender, roomPreferences, paymentMethod, mailingAddress, phoneNumber, checkInDate, checkOutDate) {
    this.name = name;
    this.birthDate = birthDate;
    this.gender = gender;
    this.roomPreferences = roomPreferences;
    this.paymentMethod = paymentMethod;
    this.mailingAddress = mailingAddress;
    this.phoneNumber = phoneNumber;
    this.checkInDate = checkInDate;
    this.checkOutDate = checkOutDate;
  }

  // Calculate age.
  getAge() {
    const today = new Date();
    const birthDate = new Date(this.birthDate);
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
      age--;
    }
    return age;
  }

  // Calculate the stay duration.
  getDurationOfStay() {
    const checkIn = new Date(this.checkInDate);
    const checkOut = new Date(this.checkOutDate);
    const durationInMilliseconds = checkOut - checkIn;
    const durationInDays = Math.floor(durationInMilliseconds / (1000 * 60 * 60 * 24));
    return durationInDays;
  }

  // Get the information of the customer.
  getCustomerInfo() {
    return `
      Customer Name: ${this.name}
      Age: ${this.getAge()}
      Gender: ${this.gender}
      Room Preferences: ${this.roomPreferences.join(', ')}
      Payment Method: ${this.paymentMethod}
      Mailing Address: ${this.mailingAddress.street}, ${this.mailingAddress.city}, ${this.mailingAddress.province}, ${this.mailingAddress.postal}
      Phone Number: ${this.phoneNumber}
      Check-in Date: ${this.checkInDate}
      Check-out Date: ${this.checkOutDate}
      Duration of Stay: ${this.getDurationOfStay()} days
    `;
  }
}

// Example
const customer = new MotelCustomer(
  "Austin",
  "1998-01-24",
  "Male",
  ["Non-smoking room", "King-size bed"],
  "Credit Card",
  {
    street: "122B Baker Street",
    city: "Palm Springs",
    province: "Banana",
    postal: "a2n1x0"
  },
  "555-123-4567",
  "2023-07-20",
  "2023-07-27"
);

const customerInfo = customer.getCustomerInfo();
console.log(customerInfo);
