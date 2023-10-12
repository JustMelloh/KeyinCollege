fetch("characters.json")
  .then((response) => response.json())
  .then((familyguyCharacters) => {
    
    familyguyCharacters.forEach(familyguyCharacters => {
      console.log("Name: ", familyguyCharacters.name);
    });

    function getChildren(familyguyCharacters) {
      return `Children: ${familyguyCharacters["children"]}`;
    }

    function getPartners(familyguyCharacters) {
      return `Partners: ${familyguyCharacters["partners"]}`;
    }

    function GetFirstAppearance(familyguyCharacters) {
      return `First appearance: ${familyguyCharacters["firstEpisodeAppearance"]}`;
    }

    
  });