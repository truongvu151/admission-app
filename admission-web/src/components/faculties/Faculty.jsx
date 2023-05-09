/* eslint-disable react/jsx-key */
import { useEffect, useState } from "react"
import { Card, Container, Row } from "react-bootstrap"
import API, { endpoints } from "../../configs/API"
import Header from "../../layouts/header/Header"
import Footer from "../../layouts/footer/Footer"
import FacultyItems from "./FacultyItems"

const Faculty = () => {
    const [ faculties, setFaculties ] = useState([])

    useEffect(() => {
        const loadFaculty = async () => {
            let res = await API
                .get(endpoints[ 'faculties' ])
            setFaculties(res.data)
        }

        loadFaculty()
    }, [])

    return (
        <>
            <Header />
            <Container>
                <Row >
                    {
                        faculties.map(faculty => <FacultyItems key={ faculty.id } obj={ faculty } type="faculty" />)
                    }
                </Row>
            </Container>

            <Footer />
        </>
    )
}

export default Faculty