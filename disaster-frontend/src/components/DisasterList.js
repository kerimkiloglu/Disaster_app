import React, { useEffect, useState } from 'react';
import { getDisasters } from '../services/api';

const DisasterList = () => {
    const [disasters, setDisasters] = useState([]);

    useEffect(() => {
        getDisasters().then(response => {
            setDisasters(response.data);
        });
    }, []);

    return (
        <div>
            <h1>Disaster List</h1>
            <ul>
                {disasters.map(disaster => (
                    <li key={disaster.id}>{disaster.type} - {disaster.date_occurred}</li>
                ))}
            </ul>
        </div>
    );
};

export default DisasterList;
