import { useEffect, useState } from "react"
import { useLocation } from "react-router"

const Search=(props)=>{
    const [data,setData]=useState([])
    const {state}=useLocation()
    const baba=state
    console.log(props.bab)
    // useEffect(()=>{
    //     setData(baba.data)
    // })

    return(
        <div>
            <p className="mb-10"></p>
            <div>
                <div>
                    <div className="flex ">
                        {data.map((list)=>(
                        <div class="ml-10 mr-10 flex flex-auto max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
                            <div class="p-5">
                                <a href="#">
                                    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{list}</h5>
                                </a>
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
    )
}
export default Search