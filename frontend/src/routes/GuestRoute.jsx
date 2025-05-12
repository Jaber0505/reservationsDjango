import React from "react";
import { Navigate } from "react-router-dom";

export default function GuestRoute({ children }) {
  const username = localStorage.getItem("username");

  if (username) {
    return <Navigate to="/" />;
  }

  return children;
}
