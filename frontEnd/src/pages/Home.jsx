import React from 'react';
import { Outlet } from 'react-router-dom';
import ContentFrame from '../layout/ContentFrame';
import fetchData from '../Fetch';

export default function Home() {
	return (
		<div className='home capitalize'>
			home
			<p>
				get access to over 1000 students to markrt your product or
				service our service give you easy access to sell and
				advertise you product through emai
			</p>
		</div>
	);
}
