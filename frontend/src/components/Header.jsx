import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { logoutUser } from "../features/auth/authService";

export default function Header() {
  const navigate = useNavigate();
  const username = localStorage.getItem("username");

  const handleLogout = () => {
    logoutUser();
    navigate("/");
    window.location.reload(); // facultatif pour forcer le rafraîchissement global
  };

  return (
    <header style={{
      display: "flex",
      justifyContent: "space-between",
      alignItems: "center",
      padding: "1rem",
      borderBottom: "1px solid #ccc"
    }}>
      <h3>Portail</h3>
      {username ? (
        <div>
          <span style={{ marginRight: "1rem" }}>Bienvenue, {username}</span>
          <button onClick={handleLogout}>Déconnexion</button>
        </div>
      ) : (
        <div>
          <Link to="/login"><button style={{ marginRight: "0.5rem" }}>Connexion</button></Link>
          <Link to="/register"><button>Inscription</button></Link>
        </div>
      )}
    </header>
  );
}
