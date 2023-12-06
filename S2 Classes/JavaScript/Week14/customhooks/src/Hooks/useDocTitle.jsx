// This hook will read the title of the document and return both 
// Variables and a setter function. Reading the title and changing the title of the document.

// Variable [num] , Setter function [setNum]
// const [num, setNum] = useState(0);


import { useState, useEffect } from 'react';

const useDocTitle = ({title}) => {

    const [docTitle,setDocTitle] = useState(title);

    useEffect(()=>{
        document.title = docTitle;
    }, [docTitle]);

    return [docTitle, setDocTitle];


};

export default useDocTitle;