import axios from "axios"

const API_URL = "http://localhost:8000/api/";

export const getDisasters = () => {
    return axios.get(`${API_URL}disasters/`);
};

export const getAlerts = () => {
    return axios.get(`${API_URL}alerts/`);
};

export const getLocations = () => {
    return axios.get(`${API_URL}locations/`);
};
