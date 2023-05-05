import { useLocation } from "react-router"
import { useState, useEffect } from "react";

    import React from 'react';

const SearchDetail=()=>{
    const {state}= useLocation()
    const file=state
    const file_name=file.file
    console.log(file_name)
    const [fileContent, setFileContent] = useState('');

    useEffect(() => {
        fetch('/read',{
            method:'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({"file_name":file_name}),
        })
        .then(
            response=> response.json(),
        )
        .then  (
             data=>setFileContent(data)
        )
},[])






    return(

        <div>
            


             <p className="mb-10"></p>
<div>
    <div>
  

 
<div className="ml-10 mr-10">




<div class="w-full p-4 text-center bg-white border border-yellow-200 rounded-lg shadow sm:p-8 mr=5 dark:bg-gray-800 dark:border-gray-700">
<div class="flex flex-col items-center mr-5 pb-10">
        <img class="w-24 h-24 mb-3 rounded-full shadow-lg" src="/images/girl3.jpg" alt="Bonnie image"/>
        <h5 class="mb-1 text-xl font-medium text-gray-900 dark:text-white">{file_name} </h5>

      
    </div>
    <p class="mb-5 text-base text-gray-500 sm:text-lg dark:text-gray-400">{fileContent}</p>
   
</div>

</div>


        


    </div>



</div>

        </div>
        
        
    )
}
export default SearchDetail