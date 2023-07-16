import React from 'react';
import { Link } from 'react-router-dom';
import NavItem from './NavItem';

export default function NavBar() {
	const navigation = [
		{
			to: '/',
			name: 'Home',
		},
		{
			to: 'dashboard',
			name: 'dashboard',
		},
		{
			to: 'statistics',
			name: 'statistics',
		},
		{
			to: 'updates',
			name: 'updates',
		},
		{
			to: 'create',
			name: 'create',
		},
	];

	return (
		<nav className='navbar  flex items-start justify-between h-full flex-col'>
			<ul className=' text-black font-semibold items-start flex-col '>
				{navigation.map((nav, index) => (
					<li key={index} className='w-full bg-purple-500 my-1'>
						<Link to={nav.to} className=''>
							{nav.name}
						</Link>
					</li>
				))}
			</ul>
			<div className='flex justify-center w-full'>
				<div className='avatar online rounded-full bg-zinc-500'>
					<div className='w-10 h-10 rounded-full'></div>
				</div>
			</div>
		</nav>
	);
}
