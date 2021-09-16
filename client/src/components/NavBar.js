import React, { useContext } from 'react'
import { Navbar, Container, Nav } from 'react-bootstrap'
import { Link } from 'react-router-dom';
import PetsIcon from '@material-ui/icons/Pets';
import UserContext from '../context/UserContext';
import PersonIcon from '@material-ui/icons/Person';
import { titleCase } from '../helpers';

function NavBar() {
    const {user, setUser} = useContext(UserContext);

    return (
        <Navbar bg="dark" variant="dark" expand="lg">
        <Container>
            <Navbar.Brand>
                <Link to='/' style={{ textDecoration: 'none', fontWeight: 'bold', color: 'white' }}>
                    <PetsIcon style={{ fontSize: 40 }}/> Pick-A-Boo
                </Link>
            </Navbar.Brand>
            <Nav className="me-auto">
                <Nav.Link as={Link} to="/">Home</Nav.Link>
            </Nav>
            
            
            <Nav >               
                {Object.entries(user).length  ?
                    <>
                        <Nav.Link><PersonIcon /> {titleCase(user.user)}</Nav.Link>   
                                     
                        <Nav.Link as={Link} to="/logout">Logout</Nav.Link>
                    
                    </>
                :
                <Nav.Link as={Link} to="/login">Login</Nav.Link>}
            </Nav>

        </Container>
        </Navbar>
    )
}

export default NavBar
