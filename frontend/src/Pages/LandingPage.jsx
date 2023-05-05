
import { useState } from 'react'
import {useNavigate} from "react-router-dom"


const LandingPage=()=>{
    const [query,setQuery]=useState('')
    // const [list, setList]= useState([])
    const [bab,setBab]=useState([])
    const navigate= useNavigate()
    const handleSearch=async ()=>{
        await fetch('/search',{
            method:'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({"query":query}),
        })
        .then(
            response=> response.json(),
        )
        .then  (
             (data)=>  setBab(data)
        )


    }

    const fileClicked=(list)=>{
        navigate('/details',{state:{file:list}})
    }
    return(
        <div>
<div>
    <div>


    </div>
<section class="bg-white pb-20 dark:bg-[#021931]">
    <div class="grid max-w-screen-xl px-4 py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12">
        <div class="mr-auto place-self-center lg:col-span-7">
            <h1 class="max-w-2xl mb-4 text-4xl font-extrabold tracking-tight leading-none md:text-5xl xl:text-6xl dark:text-white">የምትወዱትን መጹሀፍት ግምገማ ያግኘኡ</h1>
            <p class="max-w-2xl mb-6 font-light text-gray-500 lg:mb-8 md:text-lg lg:text-xl dark:text-gray-400">የፀሀፊዎች እና የተለያዩ መፀሀፍት ጥሩ ግመገማ</p>
       
            <div className="inline-flex items-center justify-center">
            <div className="flex space-x-1">
                
                <input
                    type="text"
                    className="block ml-10 w-100 px-10 py-2 text-yellow-700 bg-white border rounded-full focus:
                    border-yellow-400 focus:ring-yellow-300 focus:outline-none focus:ring focus:ring-opacity-40"
                    placeholder="Search..."
                    onChange={(event)=>setQuery(event.target.value)}
                />
                <button className="px-4 text-white bg-yellow-600 rounded-full " onClick={handleSearch}>
                    <svg
                    
                        xmlns="http://www.w3.org/2000/svg"
                        className="w-5 h-5"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        strokeWidth={2}
                    >
                        <path
                            strokeLinecap="round"
                            strokeLinejoin="round"
                            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                        />
                    </svg>
                </button>
            </div>
        </div>
        </div>
        <div class="hidden lg:mt-0 lg:col-span-5 lg:flex">
             {/* <img src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/phone-mockup.png" alt="mockup"/> */}
            {/* <img src={ require('./images/bookkk.jpg')} alt=""></img> */}
            <img src={ require('../Assests/girl3.jpg')} alt="nop it not working"></img>
        </div>                
    </div>
</section>


</div>

        <div>
            <p className="mb-10"></p>
            <div>
                <div>
                    <div className="flex ">
                        {bab.map((list)=>(
                        <div class="ml-10 mr-10 flex flex-auto max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 cursor-pointer" onClick={()=>fileClicked(list)}>
                            <div class="p-5">

                                    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white" >{list}</h5>

                                <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">እራሴን ላለመሳት መጣር ጀመርኩ። ደሜ ቱቦው እንደተሰበረ የውሀ መስመር ይንፎለላል፤ እንደምንም ከጭለማው ወደ ብርሀኑ መውጣት አለብኝ..ወደ ዋናው መንገድ.</p>
                                <a href="#" class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-yellow-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-yellow-300 dark:bg-yellow-600 dark:hover:bg-yellow-700 dark:focus:ring-yellow-800">
                                    Read more
                                    <svg aria-hidden="true" class="w-4 h-4 ml-2 -mr-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                                </a>
                            </div>
                        </div>
                         ))}
                    </div>
                </div>
            </div>
        </div>


        </div>
        
        
    )
}
export default LandingPage