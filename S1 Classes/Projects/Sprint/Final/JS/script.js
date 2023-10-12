

fetch("monsters.json")
    .then(response => response.json())
    .then(data => {
        console.log("JSON data:", data);


        data.forEach(monster => {
            console.log("Monster:", monster.monster);
            console.log("Notable Drops:", monster["notable drops"]);
        });

       
        function getDescription(monster) {
            return `${monster.monster} - Level: ${monster.level}, Requirements: ${monster.requirements}`;
        }

        function getNotableDrops(monster) {
            return `Notable Drops: ${monster["notable drops"]}`;
        }

        function getMostExpensiveDrop(monster) {
            return `Most Expensive Drop: ${monster["most expensive drop"]}`;
        }

        const outputDiv = document.getElementById("output");
        data.forEach(monster => {
            const description = getDescription(monster);
            const notableDrops = getNotableDrops(monster);
            const mostExpensiveDrop = getMostExpensiveDrop(monster);

            const descriptionParagraph = document.createElement("p");
            descriptionParagraph.textContent = description;
            outputDiv.appendChild(descriptionParagraph);

            const notableDropsParagraph = document.createElement("p");
            notableDropsParagraph.textContent = notableDrops;
            outputDiv.appendChild(notableDropsParagraph);

            const mostExpensiveDropParagraph = document.createElement("p");
            mostExpensiveDropParagraph.textContent = mostExpensiveDrop;
            outputDiv.appendChild(mostExpensiveDropParagraph);
        });
    })