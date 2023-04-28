import "./App.css";
import React from "react";
// import Page1 from "./Pages/Page1";
import FirstPage from "./Pages/FirstPage";
import ResultViewer from "./Pages/ResultViewer";
import search from "./Pages/search";
import searchdetail from "./Pages/searchdetail";

function App() {
  return (
    <div className="App">
      <p className="font-bold">Hello</p>
      <FirstPage />
      <ResultViewer />

      {/* <search />
      <searchdetail /> */}
    </div>
  );
}

export default App;
