fetch('/champs.json')
  .then(response => response.json())
  .then(data => {
    const targetChampion = "Ahri"; 

    for (let x = 0; x < data.length; x++) {
      if (data[x].name === targetChampion) {
        const summary = `The age of ${data[x].name} is ${data[x].age} \nthey hail from ${data[x].origin}\nAppearance: ${data[x].appearance}, Abilities: ${data[x].abilities}`;

        console.log(summary);
        break; // Once we found the target character, we stop the loop
      }
    }
  });
  fetch('/champs.json')
  .then(response => response.json())
  .then(data => {
    const targetChampion = "Garen"; 

    for (let x = 0; x < data.length; x++) {
      if (data[x].name === targetChampion) {
        const summary = `The age of ${data[x].name} is ${data[x].age} \nthey hail from ${data[x].origin}\nAppearance: ${data[x].appearance}, Abilities: ${data[x].abilities}`;

        console.log(summary);
        break; 
      }
    }
  });
  fetch('/champs.json')
  .then(response => response.json())
  .then(data => {
    const targetChampion = "Jinx"; 

    for (let x = 0; x < data.length; x++) {
      if (data[x].name === targetChampion) {
        const summary = `The age of ${data[x].name} is ${data[x].age} \nthey hail from ${data[x].origin}\nAppearance: ${data[x].appearance}, Abilities: ${data[x].abilities}`;

        console.log(summary);
        break; 
      }
    }
  });
  fetch('/champs.json')
  .then(response => response.json())
  .then(data => {
    const targetChampion = "Yasuo"; 

    for (let x = 0; x < data.length; x++) {
      if (data[x].name === targetChampion) {
        const summary = `The age of ${data[x].name} is ${data[x].age} \nthey hail from ${data[x].origin}\nAppearance: ${data[x].appearance}, Abilities: ${data[x].abilities}`;

        console.log(summary);
        break;
      }
    }
  });
