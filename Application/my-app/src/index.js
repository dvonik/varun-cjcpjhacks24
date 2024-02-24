import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {openDatabase} from 'react-native-sqlite-storage';

var db = openDatabase( {
  name: 'User DataBase',
  location: 'default'
});
const insertData = async() => {
  const query_insert = 'INSERT INTO users {name, mobileNO, password} VALUES {?, ?, ?}';
  const params = ['Xyz',  '123456789', '123'];

  try {
    (await db).executeSql(query_insert, params);
  } catch (err) {
    console.log('err', err);
  }
};

const updateData = async() => {
  const query_update = 'UPDATE users SET mobileNo = ? WHERE id = ?';
  const params = ['9879879879', '1'];

  try {
    (await db).executeSql(query_update, params);

  } catch (err) {
    console.log('err', err);
  }

  try {
    (await db).executeSql(query_insert, params);
  } catch (err) {
    console.log('err', err);
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
