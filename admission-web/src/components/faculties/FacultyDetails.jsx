import { useEffect, useState } from "react"
import API, { endpoints } from "../../configs/API"
import { useParams } from "react-router-dom"
import Header from "../../layouts/header/Header"
import { Container } from "react-bootstrap"
import Footer from "../../layouts/footer/Footer"


const FacultyDetails = () => {
    const [ faculty, setFaculty ] = useState([])
    const { faculty_id } = useParams()

    useEffect(() => {
        const loadFaculty = async () => {
            let res = await API
                .get(endpoints[ 'faculties-details' ](faculty_id))
            console.info(res.data)
            setFaculty(res.data)
        }

        loadFaculty()
    }, [ faculty_id ])

    return (
        <>
            <Header />
            <Container className="p-4">
                <div>
                    {/* { faculty.videos.map(k => {
                        return <div key={k.id}>
                            <video src={ k.url } width="600" height="300" controls="controls" />
                        </div>
                    }) } */}

                    <h1 className="text-center text-success">{ faculty.name }</h1>
                    <p dangerouslySetInnerHTML={ { __html: faculty.description } }></p>
                </div>

            </Container>
            <Footer />
        </>
    )
}

export default FacultyDetails