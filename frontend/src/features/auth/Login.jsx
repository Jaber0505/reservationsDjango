import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUser } from "./authService";

export default function Login() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({ username: "", password: "" });
  const [message, setMessage] = useState("");

  const handleChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("");

    try {
      const response = await loginUser(formData);
      navigate("/");
    } catch (err) {
      setMessage(err.error || "Erreur de connexion");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Connexion</h2>
      <form onSubmit={handleSubmit}>
        <input name="username" type="text" placeholder="Nom d'utilisateur" onChange={handleChange} /><br />
        <input name="password" type="password" placeholder="Mot de passe" onChange={handleChange} /><br />
        <button type="submit" disabled={!formData.username || !formData.password}>
          Se connecter
        </button>
      </form>
      <p>{message}</p>
    </div>
  );
}
