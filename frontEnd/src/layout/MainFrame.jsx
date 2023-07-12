import React from 'react';
import Home from '../pages/Home';
import ContentFrame from './ContentFrame';
import NavBar from '../components/NavBar';
import { Outlet } from 'react-router-dom';
import SideBarFrame from './SideBarFrame';

export default function MainFrame() {
	return (
		<div
			className='mainfraim flex flex-row h-screen bg-slate-900 
		 '>
			<SideBarFrame>
				<NavBar />
			</SideBarFrame>
			<ContentFrame />
		</div>
	);
}
