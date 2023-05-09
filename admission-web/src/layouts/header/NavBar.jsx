import { Button, Container, Nav, NavDropdown, Navbar } from "react-bootstrap"
import { Link } from "react-router-dom"
import './HeaderStyle.css'
import { useContext, useEffect, useState } from "react"
import API, { endpoints } from "../../configs/API"
import { MyUserContext } from "../../configs/MyContext"

const NavBar = () => {
    const [ show, setShow ] = useState(false)
    const [ admission_types, setAdmissionTypes ] = useState([])
    const [ user, dispatch ] = useContext(MyUserContext)

    const showDropdown = () => {
        setShow(!show);
    }
    const hideDropdown = () => {
        setShow(false);
    }

    useEffect(() => {
        const loadAdmissionTypes = async () => {
            let res = await API
                .get(endpoints[ 'admission-types' ])
            setAdmissionTypes(res.data)
        }

        loadAdmissionTypes()
    }, [])


    const logout = () => {
        dispatch({
            "type": "logout"
        })
    }

    let userInfo = (
        <Nav>
            <Link className="nav-link text-danger " to="/login"> Đăng nhập</Link>
            <Link className="nav-link text-success " to="/register">Đăng ký</Link>
        </Nav>
    )

    if (user !== null)
        userInfo = (
            <>
                <Link className="nav-link text-danger" to="/">
                    <img src={ user.image } alt={ user.username } width="30" className="rounded-circle" />
                    Chào { user.username }
                </Link>
                <Button className="btn btn-danger" onClick={ logout }> Đăng xuất</Button>
            </>
        )

    return (
        <>
            <Navbar collapseOnSelect sticky="top" expand="lg" className="text-capitalize" style={ { backgroundColor: "#fff" } }>
                <Container>
                    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                    <Navbar.Collapse id="responsive-navbar-nav">
                        <Nav className=" me-auto my-2 my-lg-0"
                            style={ { maxHeight: '100px' } } navbarScroll >
                            <Link className="nav-link active" to="/"> Trang chủ</Link>
                            <NavDropdown title="Thông tin tuyển sinh" menuVariant="light"
                                show={ show }
                                onMouseEnter={ showDropdown }
                                onMouseLeave={ hideDropdown }>
                                { admission_types.map((type) => {
                                    let url = `/?type_id=${type.id}`
                                    return <NavDropdown.Item href={ url } key={ type.id }>{ type.type }</NavDropdown.Item>
                                }) }

                            </NavDropdown>
                            <Link className="nav-link active" to="/faculties"> Thông tin khoa ngành</Link>
                            <Link className="nav-link active" to="/#"> Thông tin tham khảo</Link>
                            <Link className="nav-link active" to="/faq"> Câu hỏi thường gặp</Link>
                            { userInfo }
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </>
    )
}

export default NavBar