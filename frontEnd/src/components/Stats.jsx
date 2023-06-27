import React from 'react';
import Dashboard from '../layout/MainFrame';
import fetchData from '../Fetch';

export default function Stats({ value, title, desc, icon }) {
	

	return (
		<>
			<div className='stat'>
				<div className='stat-figure text-secondary animate-pulse font-extrabold '>{icon}</div>
				<div className='stat-title font-extrabold'>{title}</div>
				<div className='stat-value text-primary'>
					{value >= 1000 ? value + 'K' : value}
				</div>
				<div className='stat-desc'>{desc}</div>
			</div>
		</>
	);
}
