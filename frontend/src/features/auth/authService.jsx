import axios from "axios";

const API_BASE_URL = "http://localhost:8000";

export const registerUser = async (userData) => {
  try {
    const response = await axios.post(
      `${API_BASE_URL}/accounts/api/register/`,
      userData,
      {
        headers: {
          "Content-Type": "application/json",
        },
        withCredentials: true, // nécessaire si CSRF ou cookies
      }
    );
    return response.data;
  } catch (error) {
    throw error.response?.data || { error: "Erreur inconnue" };
  }
};

export const loginUser = async (userData) => {
  const response = await axios.post(
    "http://localhost:8000/accounts/api/login/",
    userData
  );
  // stocke token + username
  localStorage.setItem("access_token", response.data.token);
  localStorage.setItem("username", response.data.username);
  return response.data;
};

export const logoutUser = () => {
  localStorage.removeItem("username");
  localStorage.removeItem("access_token");
};