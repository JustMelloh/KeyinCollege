// QAP 5 written By Liam Philpott


fetch('Family.json')
  .then(Results => Results.json())
  .then(Family => {
     Family.foreach (person => {
          Hobbies(Family);
     });
  })

  function Hobbies(Family) {
     switch(Family.Hobbies){
          case "Procastinating":
               console.log(`${Family.Name} You should really stop delaying things till the last minute!`);
               break;
          case "Reading":
               console.log(`${Family.Name} Loves to read Fantasy books, specifically Tolkein!`);
          break;
          case "Annoying Brothers":
               console.log (`${Family.Name} Should really stop annoying his brothers...`);
     }
  }

  fetch(`HeroesRES.json`)
     .then(Response => Response.json())
     .then(Hero => {
          console.log(Hero[0].HeroName);
          Status.forEach(Status => {
               console.log(Status);
          });
     })

     function Status(Hero) {
          switch(Hero.Status) {
               case "Alive":
                    console.log(`${Hero.HeroName} is Active, and on the job!`);
                    break;
               case "Dead":
                    console.log (`${Hero.HeroName} will likely be back next Issue...`);
                    break;
               case "On Vacation":
                    console.log(`${Hero.HeroName} job is never done! Back to work!`);
                    break;
               default:
                    console.log(`${Hero.HeroName} lets be honest here... Theres no rest for a DC Hero...`);
          }
     };