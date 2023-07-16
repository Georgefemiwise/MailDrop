import React from 'react';
import { Outlet } from 'react-router-dom';
import ContentFrame from '../layout/ContentFrame';
import fetchData from '../Fetch';

export default function Home() {
	return (
		<div className='home '>
			<h1 className='capitalize font-bold text-3xl'>home</h1>

			<p className='  my-4'>
				Get access to over 1000 students to market your product or
				service
				<br />
				our service give you easy access to sell and advertise you
				product through email
			</p>

			<small className='animate animate-pulse  text-red-500'>
				Logged in user should  not have this as a navigation option
			</small>
		</div>
	);
}
