import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App.';
import "./styles.css";

const root = createRoot(document.getElementById('root'));

root.render(
    <React.StrictMode>
        <App /> {/* Genera la vista a partir de los elementos de react .jsx, es lo único que hay que poner */}
    </React.StrictMode>
);