import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";


export const Dashboard = () => {
  const { store, actions } = useContext(Context);
  // JS

  return (
    <div className="container text-center">
      <h1 className="text-primary">Dashboard</h1>
      <h2 className="text-danger">{store.user}</h2>
    </div>

  )

}