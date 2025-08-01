import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
// import "./style.css";
import "./responsive.css";
import App from "./App";
import { Provider } from "react-redux";
import store from "./store";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <Provider store={store}>
    <React.StrictMode>
      <App />
    </React.StrictMode>
  </Provider>
);
