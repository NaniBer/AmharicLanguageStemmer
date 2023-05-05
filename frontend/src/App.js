import "./App.css";
import LandingPage from "./Pages/LandingPage";
import Search from "./Pages/Search";
import SearchDetail from "./Pages/SearchDetail";
import { Route, Routes } from "react-router";

function App() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/search" element={<Search />} />
      <Route path="/details" element={<SearchDetail />} />
    </Routes>
  );
}

export default App;
