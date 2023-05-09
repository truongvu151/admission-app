import { BrowserRouter, Route, Routes } from 'react-router-dom'
import './App.css'
import Header from './layouts/header/Header'
import Footer from './layouts/footer/Footer'
import SearchBar from './components/search/SearchBar'
import { MyUserContext } from './configs/MyContext'
import { Container } from 'react-bootstrap'
import { useReducer } from 'react'
import myUserReducer from './reducers/MyUserReducer'
import cookie from 'react-cookies';
import AdmissionsHome from './components/admissions/AdmissionsHome'
import Login from './components/user/Login'
import Register from './components/user/Register'
import Faculty from './components/faculties/Faculty'
import FacultyDetails from './components/faculties/FacultyDetails'

function App () {
  const [ user, dispatch ] = useReducer(myUserReducer, cookie.load('current-user') || null)

  return (
    <MyUserContext.Provider value={ [ user, dispatch ] }>
      <BrowserRouter>

        <Routes>
          <Route path='/' element={ <AdmissionsHome /> } />
          <Route path='/login' element={ <Login /> } />
          <Route path='/register' element={ <Register /> } />
          <Route path='/faculties' element={ <Faculty /> } />
          <Route path='/faculties/:faculty_id' element={<FacultyDetails />} /> 
          <Route path='*' element={ <div className='alert alert-info m-1'>Comming soon...</div> } />
        </Routes>

      </BrowserRouter>
    </MyUserContext.Provider>
  );
}

export default App
