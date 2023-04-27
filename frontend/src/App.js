import "./App.css";
import Page1 from "./Pages/page1";
import search from "./Pages/search";
import searchdetail from "./Pages/searchdetail";



function App() {
  return (
    <div className="App">
      <p className="font-bold"></p>
      <Page1 />
      <search />
      <searchdetail />
    </div>
  );
}

export default App;
