import React from 'react';
import { Link } from 'react-router-dom';


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
		<nav className='navbar  flex items-start justify-between h-full flex-row fixed '>
			<ul className=' text-black font-semibold items-start flex-col '>
				{navigation.map((nav, index) => (
					<li key={index} className='w-full hover:bg-neutral-focus hover:text-white  py-3 px-5 rounded-md'>
						<Link to={nav.to} className=' capitalize'>
							{nav.name}
						</Link>
					</li>
				))}
			</ul>
		</nav>
	);
}
