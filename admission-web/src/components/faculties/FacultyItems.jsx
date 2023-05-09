/* eslint-disable react/prop-types */
import { Card, Col } from "react-bootstrap"
import { Link } from "react-router-dom"


const Items = ({obj, type}) => {
    let url = `/faculties/`
    if (type === 'faculty')
        url =  `/faculties/${obj.id}`

    return (
        <Col md={4} xs={12} key={obj.id} className="p-2">
            <Card>
                <Card.Img variant="top" src={obj.image} />
                <Card.Body>
                    <Card.Title>{obj.name}</Card.Title>
                    <Link to={url} className="btn btn-primary">Xem chi tiết</Link>
                </Card.Body>
            </Card>
        </Col>
    )
}

export default Items