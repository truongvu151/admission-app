import { useState, useEffect } from 'react';
import API, { endpoints } from '../../configs/API';
import { Carousel, Col, Container, Image, Row } from 'react-bootstrap';


const ImageSlider = () => {
  const [images, setImages] = useState([]);
  
  useEffect(() => {
    // Fetch images from your API
    const loadImages = async () => {
            let res = await API
                .get(endpoints[ 'banners' ])
            setImages(res.data)
        }

        loadImages()
  }, []);
  

  return (
    <Container fluid>
          <Row className="max-height">
            <Col xs={10} className="mx-auto div-col">
              <Carousel>
            { images.map((data) => (
                <Carousel.Item key={data.id}>
                  <Image
                    className="d-block w-100"
                    src= {data.image}
                    alt= {data.name}
                    fluid
                    style={{ objectFit: "cover" }}
                  />
                  
                </Carousel.Item>
            ))}
              </Carousel>
            </Col>
          </Row>
    </Container>
 
  );
}

export default ImageSlider;