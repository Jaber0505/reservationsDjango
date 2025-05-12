import React, { useEffect, useState } from 'react';

export default function Home() {
  const [username, setUsername] = useState(null);

  useEffect(() => {
    const storedUsername = localStorage.getItem("username");
    setUsername(storedUsername);
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Portail de réservation</h1>
      {username ? (
        <h2>Bienvenue, {username} !</h2>
      ) : (
        <p>Veuillez vous connecter ou vous inscrire.</p>
      )}
    </div>
  );
}
