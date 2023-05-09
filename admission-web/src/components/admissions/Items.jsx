/* eslint-disable react/prop-types */
import { Card, Col } from "react-bootstrap"
import { Link } from "react-router-dom"


const Items = ({obj, type}) => {
    let url = `/admissions/`
    if (type === 'admissions')
        url =  `/admissions/${obj.id}`

    return (
        <Col md={3} xs={12} key={obj.id} className="p-2">
            <Card>
                <Card.Img variant="top" src={obj.image} />
                <Card.Body>
                    <Card.Title>{obj.title}</Card.Title>
                    <Link to={url} className="btn btn-primary">Xem chi tiết</Link>
                </Card.Body>
            </Card>
        </Col>
    )
}

export default Items