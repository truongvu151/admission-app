/* eslint-disable react-refresh/only-export-components */
import axios from "axios";
import cookie from "react-cookies";

export const endpoints = {
    "admission-types": "/admission-types/",
    "banners": "/banners/",
    "admissions-home": (admission_type_id) => `/admission-types/${admission_type_id}/admissions/`,
    "admissions": "/admissions/",
    "admissions-details": (admission_id) => `/lessons/${admission_id}/`,
    "login": "/o/token/",
    "current-user": "/users/current-user/",
    "register": "/users/",
    "faculties": "/faculties/",
    "faculties-details": (faculty_id) => `/faculties/${faculty_id}/`,

}

export const authAPI = () => axios.create({
    baseURL: "http://127.0.0.1:8000/",
    headers: {
        "Authorization": `Bearer ${cookie.load("access-token")}`
    }
})

export default axios.create({
    baseURL: "http://127.0.0.1:8000/"
})