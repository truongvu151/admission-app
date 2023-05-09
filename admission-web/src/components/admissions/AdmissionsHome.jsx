import { useEffect, useState } from "react"
import { Button, Card, Container, Row } from "react-bootstrap"
import API, { endpoints } from "../../configs/API"
import Loading from "../../layouts/base/Loading"
import Items from "./Items"
import Header from "../../layouts/header/Header"
import SearchBar from "../search/SearchBar"
import Footer from "../../layouts/footer/Footer"
import Banner from "../../layouts/header/Banner"
import Main from "../../layouts/body/main"


const AdmissionsHome = () => {
    return (
        <>
            <Header />
            <Banner />
            <SearchBar />
            <Main />
            <Footer />
        </>

    )
}

export default AdmissionsHome