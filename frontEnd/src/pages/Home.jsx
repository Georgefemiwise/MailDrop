import React from 'react';
import { Outlet } from 'react-router-dom';
import ContentFrame from '../layout/ContentFrame';

export default function Home() {
	return (
		<div className='home'>
			<ContentFrame>jgvfjcfgc</ContentFrame>
			<Outlet />
		</div>
	);
}
