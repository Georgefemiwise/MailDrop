import React from 'react';
import { Outlet } from 'react-router-dom';

export default function ContentFrame() {
	return (
		<div
			className={`content container flex flex-1 py-5 px-20 justify-center border `}>
			<Outlet />
		</div>
	);
}

// import React, { useEffect, useState } from 'react';
// import Navbar from './components/NavBar';
// import Stats from './components/Stats';
// import StudentForm from './components/StudentDetails/StudentForm';
// import Table from './components/StudentDetails/Table';
// import { Routes, Route, Outlet, Link } from "react-router-dom";

// export default function App() {
// 	return (
// 		<>
// 			<div className='flex flex-col justify-center items-center'>
// 				<Navbar />
// 				{/* <Stats />
// 			<Table/> */}
// 				<StudentForm />
// 			</div>
// 		</>
// 	);
// }
