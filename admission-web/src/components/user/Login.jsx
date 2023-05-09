import { useContext, useState } from "react"
import { Button, Col, Container, Form, Row } from "react-bootstrap"
import cookie from "react-cookies"
import { Navigate } from "react-router-dom"
import API, { authAPI, endpoints } from "../../configs/API"
import { MyUserContext } from "../../configs/MyContext"
import ErrorAlert from "../../layouts/base/ErrorAlert"
import InputItem from "../../layouts/base/InputItem"
import Loading from "../../layouts/base/Loading"
import Header from "../../layouts/header/Header"
import Footer from "../../layouts/footer/Footer"

const Login = () => {
    const [ username, setUsername ] = useState("")
    const [ password, setPassword ] = useState("")
    const [ loading, setLoading ] = useState(false)
    const [ err, setErr ] = useState()
    const [ user, dispatch ] = useContext(MyUserContext)

    const login = (evt) => {
        evt.preventDefault()

        const process = async () => {
            try {
                let res = await API.post(endpoints[ 'login' ], {
                    "username": username,
                    "password": password,
                    "client_id": "EKho5hbl5jlA17rucOSMeoPGK1uS01W7G5e2Q9z0",
                    "client_secret": "2VuzRtTWGHNGMk1B8qYDtZi6jfRWP2md3MwZ27YENpUdpsvsXo2Es0XgkS9j95vyRYf1xa2U1DujkRSKCSxulAvJtD6vVPK7ILZMvuEJuqRriBhGI11MMpyV9xyipFNk",
                    "grant_type": "password"
                })

                cookie.save('access-token', res.data.access_token)

                let user = await authAPI().get(endpoints[ 'current-user' ])
                cookie.save('current-user', user.data)

                dispatch({
                    "type": "login",
                    "payload": user.data
                })
            } catch (ex) {
                console.error(ex)
                setErr('Username hoặc Password không hợp lệ!')
            } finally {
                setLoading(false)
            }
        }

        if (username === "" || password === "")
            setErr("Phải nhập username và password!")
        else {
            setLoading(true)
            process()
        }
    }

    if (user !== null)
        return <Navigate to="/" />



    return (
        <>
            <Header />
            <Container>
                <Row className="justify-content-md-center m-4">
                    <Col xs={ 12 } md={ 6 }>

                        <h1 className="text-center text-success">ĐĂNG NHẬP</h1>
                        { err ? <ErrorAlert err={ err } /> : "" }
                        <Form onSubmit={ login } className="mb-3">
                            <InputItem label="Tên đăng nhập" type="text" value={ username } setValue={ e => setUsername(e.target.value) } />
                            <InputItem label="Mật khẩu" type="password" value={ password } setValue={ e => setPassword(e.target.value) } />

                            { loading ? <Loading /> : <Button variant="primary" type="submit">Đăng nhập</Button> }
                        </Form>

                    </Col>
                </Row>
            </Container>

            <Footer />
        </>

    )
}

export default Login