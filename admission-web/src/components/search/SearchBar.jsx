import { Button, Container, Form, FormControl } from 'react-bootstrap'
import './search.css'

const SearchBar = () => {
    return (
        <Container>
            <Form className="d-flex bg-gray-200 p-5">
                <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                <Button variant="outline-success enroll-btn" >Tìm</Button>
            </Form>
        </Container>
    )
}

export default SearchBar