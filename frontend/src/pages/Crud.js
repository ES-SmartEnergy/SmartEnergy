import axios from 'axios';
import { useEffect, useState } from "react";
import Form from "../components/Form.js";
import Grid from "../components/Grid.js";
import GlobalStyle from "../styles/global.js";
import styled from "styled-components";
import { toast, ToastContainer } from "react-toastify";
import 'react-toastify/dist/ReactToastify.css';
import './../App.css';

const Container = styled.div`
  width: 100%;
  max-width: 1300px;
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
`;

const Title = styled.h2``;

function Crud() {
    const [users, setUsers] = useState([]);
    const [onEdit, setOnEdit] = useState(null);

    const getUsers = async () => {
        try {
            const res = await axios.get("http://localhost:8800/crud");
            setUsers(res.data.sort((a, b) => (a.nome > b.nome ? 1 : -1)));
        } catch (error) {
            toast.error(error);
        }
    };

    useEffect(() => {
        getUsers();
    }, [setUsers]);

    return (
        <>
            <Container>
                <Title>USUÁRIOS</Title>
                <Form onEdit={onEdit} setOnEdit={setOnEdit} getUsers={getUsers} />
                <Grid setOnEdit={setOnEdit} users={users} setUsers={setUsers} />
            </Container>
            <ToastContainer autoClose={2000} position={toast.POSITION.BOTTON_LEFT} />
            <GlobalStyle />
        </>
    )
}

export default Crud;