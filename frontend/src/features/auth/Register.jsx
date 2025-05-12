import React, { useState } from "react";
import { registerUser, loginUser } from "./authService";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("");

    try {
      await registerUser(formData);

      // 🔒 Connexion automatique après inscription
      await loginUser({
        username: formData.username,
        password: formData.password,
      });

      navigate("/");
    } catch (err) {
      setMessage(err.error || "Une erreur est survenue");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Inscription</h2>
      <form onSubmit={handleSubmit}>
        <input
          name="username"
          type="text"
          placeholder="Nom d'utilisateur"
          onChange={handleChange}
        /><br />
        <input
          name="email"
          type="email"
          placeholder="Email"
          onChange={handleChange}
        /><br />
        <input
          name="password"
          type="password"
          placeholder="Mot de passe"
          onChange={handleChange}
        /><br />
        <button type="submit">S’inscrire</button>
      </form>
      <p>{message}</p>
    </div>
  );
}
