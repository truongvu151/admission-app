import { Col, Container, Row } from "react-bootstrap"

const Main = () => {
    return (
        <>
            <Container >
                <Row>
                    <Col xs={ 12 } md={ 8 }>
                        <Row>
                            <h2> THÔNG TIN TUYỂN SINH</h2>
                        </Row>
                        <Row>
                            <h2> LICH TƯ VẤN </h2>
                        </Row>
                        <Row>
                            <h2> THÔNG TIN KHOA - NGÀNH</h2>
                            
                        </Row>
                    </Col>
                    <Col xs={ 6 } md={ 4 }>
                        <Row className="">
                          
                        </Row>
                    </Col>
                </Row>
            </Container>
        </>
    )
}

export default Main