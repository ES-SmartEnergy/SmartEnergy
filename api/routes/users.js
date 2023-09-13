import  express  from "express";
import {getUsers, addUser, updateUser, deleteUser, autenticarUser} from "../controllers/user.js";

const router = express.Router()

router.get("/crud", getUsers)

router.post("/crud", addUser)

router.put("/crud:id", updateUser)

router.delete("/crud:id", deleteUser)

router.post("/login", autenticarUser)

export default router
