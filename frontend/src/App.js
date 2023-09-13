//import logo from './logo.svg';
//import './App.css';

import Crud from "./pages/Crud";
import Login from './pages/Login';

import { createBrowserRouter, RouterProvider } from "react-router-dom"

const router = createBrowserRouter( [
  {
    path: "login",
    element: <Login />
  },
  {
    path: "crud",
    element: <Crud />
  }
])

function App() {
  
  return (
    
    /*<>
      <Crud />
    </>*/
    
    /*
    <>
        <div className="App">
          <header className="App-header">
            <Login />
          </header>
        </div>
      
      
    </>*/

    <RouterProvider router={router} />
    
  );
  
}

export default App;
