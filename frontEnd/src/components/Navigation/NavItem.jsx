import React from 'react';
import { Link } from 'react-router-dom';

export default function NavItem({ to, name }) {
	return (
		<div className='capitalize my-2 px-9 w-full border-l-2 hover:text-gray-600 hover:border-l-orange-500 '>
			<Link to={to}>{name}</Link>
		</div>
	);
}
