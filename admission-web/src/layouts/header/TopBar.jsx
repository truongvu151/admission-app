import { Container, Image, Navbar } from "react-bootstrap"
import { Link } from "react-router-dom"
import './HeaderStyle.css'


const TopBar = () => {
    return (
        <Navbar className="navbar-custom" expand="lg">
            <Container>
                <Image src="src\assets\logo-ou.png" alt="logo" className="logo"/>
                <Link to="/" className="navbar-brand m-custom">
                    <span className="m-brand-text">
                        Cổng thông tin tuyển sinh
                        <br />
                        Trường Đại học Mở Thành phố Hồ Chí Minh
                    </span>
                </Link>
            </Container>
        </Navbar>
    )
}

export default TopBar