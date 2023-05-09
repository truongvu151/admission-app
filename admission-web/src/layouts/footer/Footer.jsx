import { Container, Row, Col } from "react-bootstrap"
import { FaEnvelope, FaFax, FaMapMarker, FaPhoneAlt } from "react-icons/fa";
import './footerStyle.css'


const Footer = () => {
  return (
    <footer className="bg-light py-3 fixed">
      <Container>
        <Row>
          <Col xs={12} md={3} className="mb-3 mb-md-0">
            <h5 className=""> Ho Chi Minh City </h5>
            <h5 className=""> OPEN UNIVERSITY </h5>
            <ul className="list-unstyled ">
              <li>
                <FaMapMarker /> 35-37 Hồ Hảo Hớn, P.Cô Giang, Q1, Tp.HCM
              </li>
              <li>
                <FaPhoneAlt />  028.39207627; 08.39300072
              </li>
              <li>
                <FaFax />   Hotline: 1800585884
              </li>
              <li>
                 <FaEnvelope />  tuyensinh@ou.edu.vn
              </li>
            </ul>
          </Col>
          <Col xs={12} md={5}>
            <h5>Các cơ sở trực thuộc</h5>
            <ul className="list-unstyled">
                <li><b>Cơ sở 1:</b> 97 Võ Văn Tần P6 Q3 Tp.HCM</li>
                <li><b>Cơ sở 2:</b> 35-37 Hồ Hảo Hớn, Phường Cô Giang, Quận 1, Tp. Hồ Chí Minh.</li>
                <li><b>Cơ sở 3:</b> 371 Nguyễn Kiệm, Phường 3, Quận Gò Vấp, Tp. Hồ Chí Minh.</li>
                <li><b>Cơ sở 4:</b> 02  Mai Thị Lựu, Phường Đa Kao, Quận 1, Tp. Hồ Chí Minh.</li>
                <li><b>Cơ sở 5:</b> 68 Lê Thị Trung, Tp.Thủ Dầu Một, Tỉnh Bình Dương.</li>
                <li><b>Cơ sở 6:</b> Phường Long Bình Tân, Tp. Biên Hòa, Tỉnh Đồng Nai.</li>
            </ul>
          </Col>
          <Col xs={12} md={4}>
            
          </Col>
        </Row>
        <hr />
        <p className="text-center mb-0">
          © {new Date().getFullYear()} Đại học Mở thành phố Hồ Chí Minh
        </p>
      </Container>
    </footer>
  );
};

export default Footer;
