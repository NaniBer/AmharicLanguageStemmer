import Component1 from "../Components/componen1";

const page1=()=>{
    const [query,setQuery]= useState('')
    const handleClick=(e)=>{
        
        e.preventDefault()
        const formData= new FormData(e.target)
        const data= Object.fromEntries(formData)
        setQuery(data)
    return(
        <div>
             <p>This is Home</p>
<div>
    <div>
<div>
</div>

    </div>
<section class="bg-white dark:bg-[#021931]">
    <div class="grid max-w-screen-xl px-4 py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12">
        <div class="mr-auto place-self-center lg:col-span-7">
            <h1 class="max-w-2xl mb-4 text-4xl font-extrabold tracking-tight leading-none md:text-5xl xl:text-6xl dark:text-white">የምትወዱትን መጹሀፍት ግምገማ ያግኘኡ</h1>
            <p class="max-w-2xl mb-6 font-light text-gray-500 lg:mb-8 md:text-lg lg:text-xl dark:text-gray-400">የፀሀፊዎች እና የተለያዩ መፀሀፍት ጥሩ ግመገማ</p>
       
            <div className="inline-flex items-center justify-center">
            <div className="flex space-x-1">
                <form onSubmit={handleClick}>
                <input
                    type="text"
                    name="query"
                    className="block ml-10 w-100 px-10 py-2 text-yellow-700 bg-white border rounded-full focus:
                    border-yellow-400 focus:ring-yellow-300 focus:outline-none focus:ring focus:ring-opacity-40"
                    placeholder="Search..."
                />
                <button className="px-4 text-white bg-yellow-600 rounded-full ">
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
                </form>
            </div>
        </div>
        </div>
        <div class="hidden lg:mt-0 lg:col-span-5 lg:flex">
             {/* <img src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/hero/phone-mockup.png" alt="mockup"/> */}
            {/* <img src={ require('./images/bookkk.jpg')} alt=""></img> */}
            <img src="/images/girl3.jpg" alt="nop it not working"></img>
        </div>                
    </div>
</section>


</div>
             <Component1/> 
        </div>
        
        
    )
}
}
export default page1

