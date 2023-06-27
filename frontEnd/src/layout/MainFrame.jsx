import React from 'react';
import Home from '../pages/Home';
import ContentFrame from './ContentFrame';
import NavBar from '../components/NavBar';
import { Outlet } from 'react-router-dom';
import TopFrame from './TopFrame';

export default function MainFrame() {
	return (
		<div className='mainfraim flex flex-col h-screen'>
			<TopFrame>
				<NavBar />
			</TopFrame>
			<ContentFrame />
		</div>
	);
}
